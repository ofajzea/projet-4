from pathlib import Path
import os
import shutil

import numpy as np
import huggingface_hub
import rasterio
import matplotlib.pyplot as plt
from scipy.io import loadmat
import tifffile


def download_data():
    # Download target folder relative to current path
    out_folder = "data/raw/modis-snow-coverage"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/modis-snow-coverage"

    cwd = Path(__file__).resolve().parents[1]
    target_directory = cwd / out_folder
    if not target_directory.exists():
        try:
            target_directory.mkdir(parents=True, exist_ok=True)
            huggingface_hub.snapshot_download(
                repo_id=repository,
                repo_type="dataset",
                local_dir=target_directory,
                token=os.getenv("HUGGINGFACE_TOKEN"),
            )
        except Exception as e:
            shutil.rmtree(target_directory)
            raise ValueError(
                f"Error downloading repository." +
                f"{e}"
            )

def data_info():
    filename_ndsi = "data/raw/modis-snow-coverage/data/2013039/Modimlab_2013039_reproj2.tif"

    cwd = Path(__file__).resolve().parents[1]
    file_ndsi = cwd / filename_ndsi

    with rasterio.open(file_ndsi) as img:
        print("File info:")
        print(f"- Dimensions: {img.width} x {img.height} x {img.count}")
        print(f"- CRS: {img.crs}")
        print(f"- Bounds: {img.bounds}")
        print(f"- Dtype: {img.dtypes}")
        print(f"- Driver: {img.driver}")


def visualize_data():
    filename_hsi = "data/raw/modis-snow-coverage/data/2013039/Modimlab_2013039_reproj2.tif"
    filename_mat = "data/raw/modis-snow-coverage/data/2013039/Spot_degrade_2013039.mat"
    cwd = Path(__file__).resolve().parents[1]
    file_hsi = cwd / filename_hsi
    file_mat = cwd / filename_mat

    mat_handler = loadmat(file_mat)
    array_spot = mat_handler["Spot_degrade"]

    rgb_channels = [0, 3, 2]

    array = tifffile.imread(file_hsi)
    array = np.nan_to_num(array, nan=0.0)
    rgb_array = array[:, :, rgb_channels]
    rgb_array = rgb_array / rgb_array.max()

    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(rgb_array)
    ax[0].set_title("MODIS acquisition")
    ax[1].imshow(array_spot, cmap="gray")
    ax[1].set_title("SPOT refererence")
    plt.show()


def main():
    download_data()
    data_info()
    visualize_data()

if __name__ == "__main__":
    main()