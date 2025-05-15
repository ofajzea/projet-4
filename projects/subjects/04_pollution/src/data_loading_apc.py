from pathlib import Path
from scipy.interpolate import griddata
import os

import pandas as pd
from datetime import datetime
from sklearn.decomposition import PCA

import huggingface_hub
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import h5netcdf
import matplotlib.pyplot as plt
import numpy as np

# ===========================================
# affichage données centré sur la France  NO2
# ===========================================

def interpolate_and_plot_france_NO2():
    filename = "C:/Users/PC/Desktop/09_05_2025_bis.nc"
    cwd = Path(__file__).resolve().parents[1]
    file_nc = cwd / filename

    ds = xr.open_dataset(file_nc, group="PRODUCT")

    no2 = ds["nitrogendioxide_tropospheric_column"]
    qa = ds["qa_value"]

    # Filtrage qualité
    no2_filtered = no2.where(qa > 0.75).values.squeeze()
    lat = ds["latitude"].values.squeeze()
    lon = ds["longitude"].values.squeeze()

    # Filtrage France (approx : lat 41-51, lon -5 à 10)
    mask_france = (lat >= 47) & (lat <= 50) & (lon >= 1) & (lon <= 4)
    lat_f = lat[mask_france]
    lon_f = lon[mask_france]
    no2_f = no2_filtered[mask_france]

    # Interpolation sur une grille régulière
    
    grid_lat, grid_lon = np.mgrid[47:50:200j, 1:4:200j]
    grid_no2 = griddata(
        (lat_f, lon_f),
        no2_f,
        (grid_lat, grid_lon)
        #method="linear"
    )
        
    # Affichage
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})
    #ax.set_extent([-5, 10, 41, 51])
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    c = ax.pcolormesh(grid_lon,grid_lat, grid_no2, cmap="plasma", shading="auto", vmin=0, vmax=1e-4)
    fig.colorbar(c, ax=ax, label="NO₂ tropospheric column [mol/m²]")
    ax.set_title("Interpolation NO₂ - Zone France")
    plt.show()

#interpolate_and_plot_france_NO2()

# ===========================================
# Moyennage des jeux de données et crétaion d'une nouvelle carte NO2
# ===========================================

def compute_average_no2_map():
    data_dir = Path(__file__).resolve().parents[1] / "C:/Users/josema/Desktop/NO2_paris"
    nc_files = list(data_dir.glob("*.nc"))

    # Grille régulière pour interpolation (France)
    grid_lat, grid_lon = np.mgrid[48:49.5:200j, 1:4:200j]
    accumulated_no2 = np.zeros_like(grid_lat)
    count_valid = np.zeros_like(grid_lat)
    n=0

    # === CONFIGURATION ===
    dossier_donnees = "./donnees_no2/"
    zone_paris = {
        "lat_min": 48.7,
        "lat_max": 49.1,
        "lon_min": 2.2,
        "lon_max": 2.5,}

    
    # === STOCKAGE DES RÉSULTATS ===
    dates = []
    moyennes_no2 = []

    for file in nc_files:
        n+=1
        print(n)
        try:    
            ds = xr.open_dataset(file, group="PRODUCT")

            no2 = ds["nitrogendioxide_tropospheric_column"]
            qa = ds["qa_value"]

            no2_filtered = no2.where(qa > 0.75).values.squeeze()
            lat = ds["latitude"].values.squeeze()
            lon = ds["longitude"].values.squeeze()

            # Masque géographique ile de France 

            mask = (lat >= 48) & (lat <= 49.5) & (lon >= 1) & (lon <= 4)
            lat_f = lat[mask]
            lon_f = lon[mask]
            no2_f = no2_filtered[mask]

            # Masque géographique Paris + 1ère couronne
            masque_1 = (
                (lat >= zone_paris["lat_min"]) & (lat <= zone_paris["lat_max"]) &
                (lon >= zone_paris["lon_min"]) & (lon <= zone_paris["lon_max"]))


            
            # Moyenne des valeurs valides
            no2_zone = no2_filtered[masque_1]
            if no2_zone.size > 0:
                moyenne = np.nanmean(no2_zone)
                moyennes_no2.append(moyenne)
            else:
                moyennes_no2.append(np.nan)

            
            if len(no2_f) < 10:
                print(f"{file.name}: trop peu de points valides, ignoré.")
                continue

            dates.append(n)

            interp = griddata(
                (lat_f, lon_f), no2_f,
                (grid_lat, grid_lon),
                method="linear"
            )

            # Ajout à la somme et au compteur
            valid_mask = ~np.isnan(interp)
            accumulated_no2[valid_mask] += interp[valid_mask]
            count_valid[valid_mask] += 1

        except Exception as e:
            print(f"Erreur avec {file.name} : {e}")

    # Moyenne finale
    mean_no2 = np.divide(accumulated_no2, count_valid, out=np.full_like(accumulated_no2, np.nan), where=count_valid > 0)
   

    villes_idf = [
                {"nom": "Paris", "latitude": 48.8566, "longitude": 2.3522},
                {"nom": "Boulogne-Billancourt", "latitude": 48.8356, "longitude": 2.2417},
                {"nom": "Saint-Denis", "latitude": 48.9362, "longitude": 2.3574},
                {"nom": "Argenteuil", "latitude": 48.9472, "longitude": 2.2467},
                {"nom": "Montreuil", "latitude": 48.8638, "longitude": 2.4485},
                {"nom": "Nanterre", "latitude": 48.8924, "longitude": 2.2066},
                {"nom": "Créteil", "latitude": 48.7904, "longitude": 2.4556},
                {"nom": "Mantes-la-Jolie", "latitude": 48.9900, "longitude": 1.7167},
                {"nom": "Poissy", "latitude": 48.9291, "longitude": 2.0404},
                {"nom": "Conflans-Sainte-Honorine", "latitude": 48.9984, "longitude": 2.0991},
                {"nom": "Rambouillet", "latitude": 48.6436, "longitude": 1.8345},
                {"nom": "Évry-Courcouronnes", "latitude": 48.6328, "longitude": 2.4402},
                {"nom": "Massy", "latitude": 48.7304, "longitude": 2.2727},
                {"nom": "Saint-Denis", "latitude": 48.9362, "longitude": 2.3574},
                {"nom": "Aulnay-sous-Bois", "latitude": 48.9382, "longitude": 2.4945},
                {"nom": "Versailles", "latitude": 48.8014, "longitude": 2.1301},]

    # Affichage
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})
    #ax.set_extent([-5, 10, 41, 51])

    for ville in villes_idf:
        ax.plot(ville["longitude"], ville["latitude"], marker='o', color='red', markersize=5, transform=ccrs.PlateCarree())
        ax.text(ville["longitude"] + 0.02, ville["latitude"] + 0.01, ville["nom"],fontsize=7, transform=ccrs.PlateCarree())

    ax.coastlines()
    ax.add_feature(cfeature.STATES.with_scale('10m'), linestyle=":")
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    ax.add_feature(cfeature.RIVERS)
    c = ax.pcolormesh(grid_lon, grid_lat, mean_no2, cmap="plasma", shading="auto", vmin=0, vmax=1e-4)
    fig.colorbar(c, ax=ax, label="NO₂ [mol/m²]")
    ax.set_title("Carte concentration de NO₂ sur la France")
    plt.tight_layout()
    plt.show()
    
    # === TRACÉ DE L'ÉVOLUTION ===
    plt.figure(figsize=(10, 5))
    plt.plot(dates, moyennes_no2, linestyle='-', color='blue')
    plt.show()


#if __name__ == "__main__":
   #compute_average_no2_map()


# ===========================================
# ACP
# ===========================================


# === CONFIGURATION GÉOGRAPHIQUE (Paris + petite couronne) ===
zone_paris = {
"lat_min": 48.7,
"lat_max": 49.1,
"lon_min": 2.2,
"lon_max": 2.5,
}

# === DOSSIER DES POLLUANTS ===
racine_dossier = "C:/Users/josema/Desktop/données_paris"
polluants = ["NO2", "CO", "SO2", "formaldehyde","CH4"]

# === DICTIONNAIRE POUR STOCKER LES DONNÉES ===
donnees = {}

# === EXTRACTION DES DONNÉES POUR CHAQUE POLLUANT ===
for polluant in polluants:
    dossier = os.path.join(racine_dossier, polluant)
    valeurs_journalieres = {}

    for fichier in sorted(os.listdir(dossier)):
        if fichier.endswith(".nc"):
            chemin = os.path.join(dossier, fichier)
            try:
                ds = xr.open_dataset(chemin, group="PRODUCT")
                lat = ds["latitude"].values
                lon = ds["longitude"].values
                data = ds[list(ds.data_vars)[0]].values # prend la première variable
                qa = ds["qa_value"].values if "qa_value" in ds else np.ones_like(data)

                # Masques qualité + zone géographique
                mask_geo = (
                        (lat >= zone_paris["lat_min"]) & (lat <= zone_paris["lat_max"]) &
                        (lon >= zone_paris["lon_min"]) & (lon <= zone_paris["lon_max"]))
                mask = (qa > 0.75) & mask_geo
                moyenne = np.nanmean(data[mask]) if np.any(mask) else np.nan

                # Extraction de la date (depuis nom de fichier ou metadata)
                try:
                    date_str = ds.time.values.astype(str)
                    date = datetime.strptime(date_str[:10], "%Y-%m-%d")
                except:
                    date = datetime.strptime(fichier[:8], "%Y%m%d") # ex: 20200415
                    valeurs_journalieres[date] = moyenne

            except Exception as e:
                print(f"Erreur avec {chemin} : {e}")

    donnees[polluant] = pd.Series(valeurs_journalieres)


for k in donnees:
    donnees[k].index=pd.to_datetime(donnees[k].index).date



# === COMBINAISON DES SÉRIES TEMPORELLES EN UN SEUL TABLEAU ===
df = pd.DataFrame(donnees)
print(df.isna().sum())

df = df.dropna() # on ne garde que les dates avec toutes les valeurs

# === PCA ===
X = df.values
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# === AFFICHAGE ===
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c='blue', edgecolor='k')
for i, date in enumerate(df.index):
    plt.text(X_pca[i, 0], X_pca[i, 1], date.strftime("%d-%m"), fontsize=8)

plt.title("Analyse en Composantes Principales (ACP) sur les polluants")
plt.xlabel("Composante principale 1")
plt.ylabel("Composante principale 2")
plt.grid(True)
plt.tight_layout()
plt.show()