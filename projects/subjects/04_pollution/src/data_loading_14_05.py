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
# affichage données centré sur la France  NO2
# ===========================================

def interpolate_and_plot_france_NO2():
    filename = "C:/Users/josema/Desktop/DATA/NO2/S5P_OFFL_L2__NO2____20240501T115126_20240501T133256_33938_03_020600_20240504T082905.nc"
    cwd = Path(__file__).resolve().parents[1]
    file_nc = cwd / filename

    ds = xr.open_dataset(file_nc, group="PRODUCT")

    no2 = ds["nitrogendioxide_tropospheric_column"]
    qa = ds["qa_value"]

    # Filtrage qualité
    no2_filtered = no2.where(qa > 0.50).values.squeeze()
    lat = ds["latitude"].values.squeeze()
    lon = ds["longitude"].values.squeeze()
    # Aplatir les tableaux
    lat_flat = lat.flatten()
    lon_flat = lon.flatten()
    no2_flat = no2_filtered.flatten()

    # Appliquer un masque sur la France
    mask_france = (lat_flat >= 41) & (lat_flat <= 51) & (lon_flat >= -5) & (lon_flat <= 10)

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
    ax.add_feature(cfeature.STATES.with_scale('10m'), linestyle=":")
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    c = ax.pcolormesh(grid_lon,grid_lat, grid_no2, cmap="viridis_r", shading="auto", vmin=0, vmax=1e-4)
    fig.colorbar(c, ax=ax, label="NO₂ tropospheric column [mol/m²]")
    ax.set_title("Interpolation NO₂ - Zone France")
    plt.show()

interpolate_and_plot_france_NO2()

# ===========================================
# Moyennage des jeux de données et crétaion d'une nouvelle carte NO2
# ===========================================

def compute_average_no2_map():
    data_dir = Path(__file__).resolve().parents[1] / "C:/Users/josema/Desktop/DATA/N2O"
    nc_files = list(data_dir.glob("*.nc"))

    # Grille régulière pour interpolation (France)
    grid_lat, grid_lon = np.mgrid[41:51:200j, -5:10:200j]
    accumulated_no2 = np.zeros_like(grid_lat)
    count_valid = np.zeros_like(grid_lat)

    for file in nc_files:
        try:
            ds = xr.open_dataset(file, group="PRODUCT")

            no2 = ds["nitrogendioxide_tropospheric_column"]
            qa = ds["qa_value"]

            # Filtrage qualité
            no2_filtered = no2.where(qa > 0.50).values.squeeze()
            lat = ds["latitude"].values.squeeze()
            lon = ds["longitude"].values.squeeze()

            # Aplatir les tableaux
            lat_flat = lat.flatten()
            lon_flat = lon.flatten()
            no2_flat = no2_filtered.flatten()


            mask =  (lat_flat >= 41) & (lat_flat <= 51) & (lon_flat >= -5) & (lon_flat <= 10)
            lat_f = lat_flat[mask]
            lon_f = lon_flat[mask]
            no2_f = no2_flat[mask]

            if len(no2_f) < 10:
                print(f"{file.name}: trop peu de points valides, ignoré.")
                continue

            interp = griddata(
                (lat_f, lon_f),
                no2_f,
                (grid_lat, grid_lon)
                #method="linear"
            )

            # Ajout à la somme et au compteur
            valid_mask = ~np.isnan(interp)
            accumulated_no2[valid_mask] += interp[valid_mask]
            count_valid[valid_mask] += 1

        except Exception as e:
            print(f"Erreur avec {file.name} : {e}")

    # Moyenne finale
    mean_no2 = np.divide(accumulated_no2, count_valid, out=np.full_like(accumulated_no2, np.nan), where=count_valid > 0)

    # Affichage
    fig, ax = plt.subplots(figsize=(10, 8), subplot_kw={'projection': ccrs.PlateCarree()})
    #ax.set_extent([-5, 10, 41, 51])
    ax.coastlines()
    ax.add_feature(cfeature.STATES.with_scale('10m'), linestyle=":")
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    c = ax.pcolormesh(grid_lon, grid_lat, mean_no2, cmap="viridis_r", shading="auto", vmin=0, vmax=1e-4)
    fig.colorbar(c, ax=ax, label="NO₂ [mol/m²]")
    ax.set_title("Carte concentration de NO₂ sur la France")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
   compute_average_no2_map()


# ===========================================
# affichage données centré sur la Canada  CO
# ===========================================

def interpolate_and_plot_canada_CO():
    filename = "C:/Users/PC/Desktop/CO_16_05_2023.nc"
    cwd = Path(__file__).resolve().parents[1]
    file_nc = cwd / filename

    ds = xr.open_dataset(file_nc, group="PRODUCT")

    co = ds["carbonmonoxide_total_column"]
    qa = ds["qa_value"]

    # Filtrage qualité
    co_filtered = co.where(qa > 0.0001).values.squeeze()
    lat = ds["latitude"].values.squeeze()
    lon = ds["longitude"].values.squeeze()

    # Filtrage France (approx : lat 41-51, lon -5 à 10)
    mask = (lat >= 41) & (lat <= 84) & (lon >= -141) & (lon <= -52)
    lat_canada = lat[mask]
    lon_canada = lon[mask]
    co_c = co_filtered[mask]

    # Interpolation sur une grille régulière
    
    grid_lat, grid_lon = np.mgrid[41:80:1000j, -141:-52:1000j]
    grid_no2 = griddata(
        (lat_canada, lon_canada),
        co_c,
        (grid_lat, grid_lon)
        #method="linear"
    )
        
    # Affichage
    fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
    #ax.set_extent([-5, 10, 41, 51])
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    c = ax.pcolormesh(grid_lon,grid_lat, grid_no2, cmap="plasma", shading="auto", vmin=0, vmax=0.1)
    fig.colorbar(c, ax=ax, label="CO tropospheric column [mol/m²]")
    ax.set_title(" CO - Zone Canada")
    plt.show()

#interpolate_and_plot_canada_CO()


# ===========================================
# Moyennage des jeux de données et crétaion d'une nouvelle carte co
# ===========================================

def compute_average_co_map():
    data_dir = Path(__file__).resolve().parents[1] / "C:/Users/PC/Desktop/CO_données"
    nc_files = list(data_dir.glob("*.nc"))

    # Grille régulière pour interpolation (canada)
    grid_lat, grid_lon = np.mgrid[41:80:800j, -141:-52:1000j]
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
    #ax.set_extent([-5, 10, 41, 51])
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    c = ax.pcolormesh(grid_lon, grid_lat, mean_co, cmap="plasma", shading="auto", vmin=0, vmax=0.1)
    fig.colorbar(c, ax=ax, label="CO [mol/m²]")
    ax.set_title("Carte concentration de CO sur le Canada")
    plt.tight_layout()
    plt.show()

#if __name__ == "__main__":
   #compute_average_co_map()
