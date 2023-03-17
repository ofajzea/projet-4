"""
Script to automatically download Earth Explorer imagery.
2022 Tristan Montagnon
(tristan.montagnon@univ-grenoble-alpes.fr || montagnon.tr@gmail.com)

Questions, comments, and bug reports can be sent to:
[Tristan Montagnon](tristan.montagnon@univ-grenoble-alpes.fr)

Additional code:
[Picone Daniele](daniele.picone@grenoble-inp.fr)
"""

import os
import pathlib
import shutil
from unittest import mock
import re
import time
from getpass import getpass

from tqdm import tqdm
from landsatxplore.earthexplorer import EarthExplorer, EarthExplorerError
from landsatxplore.api import API


def _get_tokens_patched(body):
    """Get `csrf_token` and `__ncforminfo`."""
    csrf = re.findall(r'name="csrf" value="(.+?)"', body)[0]
    if not csrf:
        raise EarthExplorerError("EE: login failed (csrf token not found).")
    return csrf, None


def earth_explorer_patched(username, password):
    with mock.patch(
        "landsatxplore.earthexplorer._get_tokens",
        side_effect=_get_tokens_patched,
    ):
        return EarthExplorer(username, password)


def satellite_images_downloader_function(
    path: str,
    latitude: float,
    longitude: float,
    api: API,
    ee: EarthExplorer,
    dataset: str = 'landsat_8_c1',
    start_date: str = '2017-01-01',
    end_date: str = '2022-01-01',
    max_cloud_cover: float = 1.,
    max_results_search: int = 100,
    max_results_download: int = 10,
) -> None:
    """
    Download Landsat Collections scenes through a Python API.

    Args:
        path: directory to save the data
        latitude: latitude of the target dataset
        longitude: longitude of the target dataset
        api: api of EarthExplorer to search the dataset
        ee: api of EarthExplorer download service
        dataset: name of the dataset collection
        start_date: start date of the dataset to explore
        end_date: end date of the dataset to explore
        max_cloud_cover: maximum cloud coverage of the dataset to explore
        max_results_search: maximum number of scenes to search for,
        max_results_download: maximum number of scenes to download,

    Returns:
        None.
    """

    print(
        '\n\nSearching for scenes for the location:',
        f'\nlatitude: {latitude}',
        f'\nlongitude: {longitude}',
    )

    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

    scenes = api.search(
        dataset=dataset,
        latitude=latitude,
        longitude=longitude,
        start_date=start_date,
        end_date=end_date,
        max_cloud_cover=max_cloud_cover,
        max_results=max_results_search
    )

    print(f"\n{len(scenes)} scenes found.")
    for scene in scenes:
        print(scene)

    if len(scenes) == 0:
        print("No scene to download!")
        return

    if dataset.startswith('landsat'):
        number_scenes = 0
        while number_scenes < max_results_download:
            print('\nDownloading scene', number_scenes, '...')
            ee.download(
                scenes[number_scenes]['landsat_scene_id'],
                output_dir=path,
                dataset=dataset,
            )
            print('Scene', number_scenes, 'downloaded!')
            number_scenes += 1

    if dataset.startswith('sentinel'):
        number_scenes = 0
        while number_scenes < max_results_download:
            print('\nDownloading scene', number_scenes, '...')
            ee.download(
                scenes[number_scenes]['sentinel_entity_id'],
                output_dir=path,
                dataset=dataset,
            )
            print('Scene', number_scenes, 'downloaded!')
            number_scenes += 1

    if len(os.listdir(path)) == 0:
        print(f'Directory {path} is empty!')
    else:
        scenes = [f for f in os.listdir(path)]
        print('\n')
        print(len(scenes), 'scenes to unzip:')
        for scene in scenes:
            print(scene)
        for scene in tqdm(scenes, desc='Scenes'):
            print('\nUnzipping the scene...')
            print(scene)
            shutil.unpack_archive(path + scene, path)
            print('Scene unzipped!')
            os.remove(path + scene)


def download_earth_explorer(**kwargs):
    username = input("Username: ")
    password = getpass("Password: ", stream=None)

    api = API(username, password)
    ee = earth_explorer_patched(username, password)

    start = time.time()
    satellite_images_downloader_function(api=api, ee=ee, **kwargs)
    end = time.time()
    print(f"{(end - start):.3f} seconds")

    api.logout()
    ee.logout()


def main():
    """
    To have access to the data provided by Earth Explorer (EE):
    - Create an account EE (https://ers.cr.usgs.gov/login)
    - Request Machine2Machine API: https://ers.cr.usgs.gov/profile/access
         There is a small form to fill to complete this step.
         Warning: The requests takes a few days to be accepted by the EE staff

    - As `dataset`, you can choose amongst:
        - Landsat 5 TM Collection 1 Level 1 	landsat_tm_c1       AVAILABLE
        - Landsat 5 TM Collection 2 Level 1 	landsat_tm_c2_l1    AVAILABLE
        - Landsat 5 TM Collection 2 Level 2 	landsat_tm_c2_l2    AVAILABLE
        - Landsat 7 ETM+ Collection 1 Level 1 	landsat_etm_c1      AVAILABLE
        - Landsat 7 ETM+ Collection 2 Level 1 	landsat_etm_c2_l1   UNAVAILABLE
        - Landsat 7 ETM+ Collection 2 Level 2 	landsat_etm_c2_l2   UNAVAILABLE
        - Landsat 8 Collection 1 Level 1 	    landsat_8_c1        AVAILABLE
        - Landsat 8 Collection 2 Level 1 	    landsat_ot_c2_l1    UNAVAILABLE
        - Landsat 8 Collection 2 Level 2 	    landsat_ot_c2_l2    UNAVAILABLE
        - Sentinel 2A 	                        sentinel_2a         AVAILABLE
    - The `longitude` and `latitude` chosen here point to Grenoble.
    - The `max_results_search` should not be changed
    - The `max_results_download` is the number of images you want to download
    - `start_date` and `end_date` must be adapted to your will.
        - Note that the dates must be in `YYYY-MM-DD` format
    - `username` and `password` are linked to the M2M API.
        - To request access, go to: https://ers.cr.usgs.gov/profile/access
    """
    options = {
        'path': './../../data/satellite_images/Grenoble',
        'latitude': 45.2,
        'longitude': 5.7,
        'dataset': 'landsat_tm_c2_l2',
        'start_date': '2017-01-01',
        'end_date': '2022-01-01',
        'max_cloud_cover': 100.,
        'max_results_search': 100,
        'max_results_download': 2,
    }
    download_earth_explorer(**options)


if __name__ == "__main__":
    main()
