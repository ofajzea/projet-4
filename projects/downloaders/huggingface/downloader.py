from pathlib import Path

import huggingface_hub

def main():
    
    # Download target folder relative to current path
    out_folder = "data"

    # Example data repository name
    # This one links to:
    # https://huggingface.co/datasets/remote-sensing-ense3-grenoble-inp/sentinel_3_snow_coverage
    repository = "remote-sensing-ense3-grenoble-inp/sentinel_3_snow_coverage"

    # If the repository above is private
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
    #      python downloader.py
    #      ```

    cwd = Path(__file__).resolve().parent
    target_directory = cwd / out_folder
    target_directory.mkdir(parents=True, exist_ok=True)
    huggingface_hub.snapshot_download(
        repo_id=repository,
        repo_type="dataset",
        local_dir=target_directory,
    )

if __name__ == "__main__":
    main()