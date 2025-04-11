from pathlib import Path
import os

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
    out_folder = "data/raw/"

    # Example data repository name
    repository = "remote-sensing-ense3-grenoble-inp/forest-plot-analysis"

    cwd = Path(__file__).resolve().parents[1]
    target_directory = cwd / out_folder
    if target_directory.exists():
        try:
            target_directory.mkdir(parents=True, exist_ok=True)
            huggingface_hub.snapshot_download(
                repo_id=repository,
                repo_type="dataset",
                local_dir=target_directory,
                token=os.getenv("HUGGINGFACE_TOKEN"),
            )
        except Exception as e:
            target_directory.rmdir()
            raise ValueError(
                f"Error downloading repository." +
                f"{e}"
            )