from pathlib import Path
from scipy.interpolate import griddata
import os

import huggingface_hub
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import h5netcdf
import matplotlib.pyplot as plt
import numpy as np

# ===========================================
# affichage données NO2
# ===========================================

def interpolate_and_plot_france_NO2():
    filename = "D:/projet teledetec/DL/avril 2025_france/S5P_NRTI_L2__NO2____20250401T112636_20250401T113136_38690_03_020800_20250401T120543.nc"
    cwd = Path(__file__).resolve().parents[1]
    file_nc = cwd / filename

    ds = xr.open_dataset(file_nc, group="PRODUCT")

    no2 = ds["nitrogendioxide_tropospheric_column"]
    qa = ds["qa_value"]

    # Filtrage qualité
    no2_filtered = no2.where(qa > 0.75).values.squeeze()
    lat = ds["latitude"].values.squeeze()
    lon = ds["longitude"].values.squeeze()
    # Aplatir les tableaux
    lat_flat = lat.flatten()
    lon_flat = lon.flatten()
    no2_flat = no2_filtered.flatten()

    mask_france = (lat_flat >= 41) & (lat_flat <= 51) & (lon_flat >= -5) & (lon_flat <= 10) #France

    lat_f = lat_flat[mask_france]
    lon_f = lon_flat[mask_france]
    no2_f = no2_flat[mask_france]

    # Interpolation sur une grille régulière
    
    grid_lat, grid_lon = np.mgrid[41:51:200j, -5:10:200j]
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
    c = ax.pcolormesh(grid_lon,grid_lat, grid_no2, cmap="viridis_r", shading="auto", vmin=0, vmax=1e-4)
    fig.colorbar(c, ax=ax, label="NO₂ tropospheric column [mol/m²]")
    ax.set_title("Interpolation NO₂ - Zone France")
    plt.show()

#interpolate_and_plot_france_NO2()

# ===========================================
# Moyennage des jeux de données et crétaion d'une nouvelle carte NO2
# ===========================================

def compute_average_no2_map():
    data_dir = Path(__file__).resolve().parents[1] / "E:/projet teledetec/DL/2022"
    nc_files = list(data_dir.glob("*.nc"))

    # Grille régulière pour interpolation 
    grid_lat, grid_lon = np.mgrid[48.1:49.3:200j, 1.4:3.7:200j]  #[42:52:1000j, -5:10:1000j]
    accumulated_no2 = np.zeros_like(grid_lat)
    count_valid = np.zeros_like(grid_lat)

    #boucle de traitement pour chaque set
    for file in nc_files:
        try:
            ds = xr.open_dataset(file, group="PRODUCT")

            no2 = ds["nitrogendioxide_tropospheric_column"]
            qa = ds["qa_value"]

            no2_filtered = no2.where(qa > 0.75).values.squeeze() #filtre sur la qualité des donnees
            lat = ds["latitude"].values.squeeze()
            lon = ds["longitude"].values.squeeze()

            #filtrage zone géographique
            mask =(lat >= 48.1) & (lat <= 49.3) & (lon >= 1.4) & (lon <= 3.7)  # (lat >= 42) & (lat <= 52) & (lon >= -5) & (lon <= 10)
            lat_f = lat[mask]
            lon_f = lon[mask]
            no2_f = no2_filtered[mask]

            #condition si trop peu de donnees dans la zone 
            if len(no2_f) < 10:
                print(f"{file.name}: trop peu de points valides, ignoré.")
                continue

            
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
    
    #Liste des villes pour l'IDF
    villes_idf = [
                {"nom": "Paris", "latitude": 48.8566, "longitude": 2.3522},
                {"nom": "Argenteuil", "latitude": 48.9472, "longitude": 2.2467},
                {"nom": "Rambouillet", "latitude": 48.6436, "longitude": 1.8345},
                {"nom": "Évry-Courcouronnes", "latitude": 48.6328, "longitude": 2.4402},
                {"nom": "Mantes-la-Jolie", "latitude": 48.9833, "longitude": 1.71667},
                {"nom": "Cergy", "latitude": 49.0333, "longitude": 2.0666},
                {"nom": "Melun", "latitude": 48.5333, "longitude": 2.6666},
                {"nom": "Versailles", "latitude": 48.8014, "longitude": 2.1301},]
    
    # Affichage
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})
    #ax.set_extent([-5, 10, 41, 51])
    for ville in villes_idf:
        ax.plot(ville["longitude"], ville["latitude"], marker='o', color='red', markersize=5, transform=ccrs.PlateCarree())
        ax.text(ville["longitude"] + 0.02, ville["latitude"] + 0.01, ville["nom"],fontsize=7, transform=ccrs.PlateCarree())

    ax.coastlines()
    ax.add_feature(cfeature.STATES.with_scale('10m'), linestyle=":") #affichage frontriere departement 
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    ax.add_feature(cfeature.RIVERS) #affichage fleuve 
    c = ax.pcolormesh(grid_lon, grid_lat, mean_no2, cmap="viridis_r", shading="auto", vmin=0, vmax=1e-4)
    fig.colorbar(c, ax=ax, label="NO₂ [mol/m²]")
    ax.set_title("Carte concentration de NO₂, Ile de France Année: 2022")
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
   compute_average_no2_map()


# ===========================================
# Moyennage des jeux de données et crétaion d'une nouvelle carte co
# ===========================================

def compute_average_co_map():
    data_dir = Path(__file__).resolve().parents[1] / "C:/Users/PC/Desktop/CO_données"
    nc_files = list(data_dir.glob("*.nc"))

    # Grille régulière pour interpolation (canada)
    grid_lat, grid_lon = np.mgrid[41:80:800j, -141:-52:1000j] #Canada
    accumulated_co = np.zeros_like(grid_lat)
    count_valid = np.zeros_like(grid_lat)

    for file in nc_files:
        try:
            ds = xr.open_dataset(file, group="PRODUCT")

            co = ds["carbonmonoxide_total_column"]
            qa = ds["qa_value"]

            co_filtered = co.where(qa > 0.75).values.squeeze()
            lat = ds["latitude"].values.squeeze()
            lon = ds["longitude"].values.squeeze()

            mask = (lat >= 41) & (lat <= 84) & (lon >= -141) & (lon <= -52)
            lat_canada = lat[mask]
            lon_canada = lon[mask]
            co_c = co_filtered[mask]

            if len(co_c) < 10:
                print(f"{file.name}: trop peu de points valides, ignoré.")
                continue

            interp = griddata(
                (lat_canada, lon_canada), co_c,
                (grid_lat, grid_lon),
                method="linear"
            )

            # Ajout à la somme et au compteur
            valid_mask = ~np.isnan(interp)
            accumulated_co[valid_mask] += interp[valid_mask]
            count_valid[valid_mask] += 1

        except Exception as e:
            print(f"Erreur avec {file.name} : {e}")

    # Moyenne finale
    mean_co = np.divide(accumulated_co, count_valid, out=np.full_like(accumulated_co, np.nan), where=count_valid > 0)

    # Affichage
    fig, ax = plt.subplots(figsize=(15, 10), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    c = ax.pcolormesh(grid_lon, grid_lat, mean_co, cmap="plasma", shading="auto", vmin=0, vmax=0.1)
    fig.colorbar(c, ax=ax, label="CO [mol/m²]")
    ax.set_title("Carte concentration de CO sur le Canada")
    plt.tight_layout()
    plt.show()

#if __name__ == "__main__":
   #compute_average_co_map()
