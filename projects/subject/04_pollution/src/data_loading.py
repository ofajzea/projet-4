from pathlib import Path
import os

import huggingface_hub
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import xarray as xr
import h5netcdf
import matplotlib.pyplot as plt


def download_data():
    # Download target folder relative to current path
    out_folder = "data/raw/tropomi-pollution"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/tropomi-pollution"

    cwd = Path(__file__).resolve().parents[1]
    target_directory = cwd / out_folder
    if not target_directory.exists():
        try:
            target_directory.mkdir(parents=True, exist_ok=True)
            huggingface_hub.snapshot_download(
                repo_id=repository,
                repo_type="dataset",
                local_dir=target_directory,
            )
        except Exception as e:
            target_directory.rmdir()
            raise ValueError(
                f"Error downloading repository." +
                f"{e}"
            )

def data_info():
    filename = "data/raw/tropomi-pollution/data/27_09_2020.nc"
    cwd = Path(__file__).resolve().parents[1]
    file_nc = cwd / filename

    with h5netcdf.File(file_nc, "r") as f:
        print(list(f.groups.keys()))

    ds = xr.open_dataset(file_nc, group="PRODUCT")
    print(ds)


def visualize_data():
    filename = "data/raw/tropomi-pollution/data/27_09_2020.nc"
    cwd = Path(__file__).resolve().parents[1]
    file_nc = cwd / filename

    ds = xr.open_dataset(file_nc, group="PRODUCT")

    no2 = ds["nitrogendioxide_tropospheric_column"]
    qa = ds["qa_value"]

    no2_filtered = no2.where(qa > 0.75)
    no2_filtered = no2_filtered.values.squeeze()
    lat = ds["latitude"].squeeze()
    lon = ds["longitude"].squeeze()

    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.coastlines()
    ax.add_feature(cfeature.BORDERS, linestyle=':')
    c = ax.pcolormesh(lon, lat, no2_filtered, cmap="plasma", shading="auto", vmin=0, vmax=1e-4)
    fig.colorbar(c, ax=ax, label="NO₂ tropospheric column [mol/m²]")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("TROPOMI Tropospheric NO₂ Column")
    fig.tight_layout()
    plt.show()


def main():
    download_data()
    data_info()
    visualize_data()

if __name__ == "__main__":
    main()