from pathlib import Path
import os
import shutil

import numpy as np
import huggingface_hub
import rasterio
import matplotlib.pyplot as plt


def download_data():
    # Download target folder relative to current path
    out_folder = "data/raw/sentinel_3_snow_coverage"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/sentinel_3_snow_coverage"

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
    filename_ndsi = "data/raw/sentinel_3_snow_coverage/data/05_01_20.tiff"

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
    filename_rgb = "data/raw/sentinel_3_snow_coverage/data/TC_05_01_20.tiff"
    cwd = Path(__file__).resolve().parents[1]
    file_rgb = cwd / filename_rgb

    with rasterio.open(file_rgb) as img_rgb:
        rgb_array = img_rgb.read()
        rgb_array = np.moveaxis(rgb_array, [-3, -2, -1], [2, 0, 1])
        rgb_array = rgb_array / rgb_array.max()

    fig, ax = plt.subplots()
    ax.imshow(rgb_array)
    plt.show()


def main():
    download_data()
    data_info()
    visualize_data()

if __name__ == "__main__":
    main()