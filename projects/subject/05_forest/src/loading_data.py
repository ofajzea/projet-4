from pathlib import Path
import os
import shutil

import numpy as np
import pandas as pd
import huggingface_hub
import matplotlib.pyplot as plt
import tifffile

def download_data():
    # The repository of this data is private
    #    - Make a new account
    #    - Ask to be added to the repo by the supervisor
    #    - Go to https://huggingface.co/settings/tokens
    #    - Generate a token
    #    - In your terminal write:
    #      ```
    #      export HUGGINGFACE_TOKEN=your_token_here
    #      ```
    #    - Then run the script as normal
    #      ```
    #      python loading_data.py
    #      ```


    # Download target folder relative to current path
    out_folder = "data/raw/forest-plot-analysis"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/forest-plot-analysis"

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


def visualize_data():
    filename_hsi = "data/raw/forest-plot-analysis/data/hi/1.tif"
    filename_label = "data/raw/forest-plot-analysis/data/gt/df_pixel.csv"
    rgb_channels = [64, 28, 15]
    plot_id = "1"

    cwd = Path(__file__).resolve().parents[1]
    file_hsi = cwd / filename_hsi
    file_label = cwd / filename_label

    rgb_array = tifffile.TiffFile(file_hsi)
    rgb_array = rgb_array.asarray()
    rgb_array = rgb_array[:, :, rgb_channels]
    rgb_array = rgb_array / rgb_array.max()

    df = pd.read_csv(file_label)
    df = df[df["plotid"] == plot_id]
    img_label = np.zeros((rgb_array.shape[0], rgb_array.shape[1], 3))

    tree_ids = df["specie"].unique()
    color_map = {tree_id: color for tree_id, color in zip(tree_ids, plt.cm.tab20.colors)}
    for _, row in df.iterrows():
        color = color_map[row["specie"]]
        img_label[int(row["row"]), int(row["col"])] = color

    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(rgb_array)
    ax[0].set_title("Hyperspectral image")
    ax[1].imshow(img_label)
    ax[1].set_title("Labels map")
    plt.show()


def main():
    download_data()
    visualize_data()

if __name__ == "__main__":
    main()