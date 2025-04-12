from pathlib import Path
import shutil
import os

import imageio
import huggingface_hub
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

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
    out_folder = "data/raw/meteo-greener"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/meteo-greener"

    cwd = Path(__file__).resolve().parents[1]
    target_directory = cwd / out_folder
    if not target_directory.exists():
        try:
            target_directory.mkdir(parents=True, exist_ok=True)
            huggingface_hub.snapshot_download(
                repo_id=repository,
                repo_type="dataset",
                local_dir=target_directory,
                token=os.getenv("HUGGINGFACE_TOKEN")
            )
        except Exception as e:
            shutil.rmtree(target_directory)
            raise ValueError(
                f"Error downloading repository." +
                f"{e}"
            )


def visualize_data():
    filename_rgb = "data/raw/meteo-greener/data/examples/19-07-01/cam2 UTC 19-07-01_10-59-59-40.jpg"
    filename_csv = "data/raw/meteo-greener/data/Meteo_GreEnER_01_Hour_2019_annee.csv"

    cwd = Path(__file__).resolve().parents[1]
    file_rgb = cwd / filename_rgb
    file_csv = cwd / filename_csv

    img = imageio.v3.imread(file_rgb)
    df = pd.read_csv(file_csv, skiprows=[0, 2, 3])
    measure_unit = pd.read_csv(file_csv, skiprows=[0], nrows=2)

    # Filtering to relevant week
    timestamps = pd.to_datetime(df["TIMESTAMP"])
    start_date = "2019-06-28"
    end_date = "2019-07-04"
    df_week = df[(timestamps >= start_date) & (timestamps <= end_date)]
    timestamps = timestamps[(timestamps >= start_date) & (timestamps <= end_date)]
    temperatures = pd.to_numeric(df_week["AirTemp_Avg"], errors="coerce")

    fig, ax = plt.subplots(1, 2)
    ax[0].imshow(img)
    plt.setp(ax[1].get_xticklabels(), rotation=45, ha="right")
    ax[1].plot( timestamps, temperatures, label="Temperature", color="blue")
    ax[1].xaxis.set_major_locator(mdates.DayLocator())  # tick every day
    ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))  # e.g., 'Jul 01'
    ax[1].set_ylabel(f"Temperature ({measure_unit['AirTemp_Avg'].iloc[0]})")

    plt.show()




def main():
    download_data()
    visualize_data()

if __name__ == "__main__":
    main()