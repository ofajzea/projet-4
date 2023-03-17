import os
from tqdm import tqdm
import shutil


def satellite_images_downloader_function(location, api, ee, dataset='landsat_8_c1', start_date='2017-01-01', end_date='2022-01-01',
                                         max_cloud_cover=1., max_results_search=100, max_results_download=10):

    """Download Landsat Collections scenes through a Python API.

    Args:
        location: location where you want to download:                      as dictionary
        api: api of EarthExplorer to search the dataset:                    as API object
        ee: api of EarthExplorer to download the dataset:                   as API object
        dataset: name of the dataset collection:                            as string
        start_date: start date of the dataset to explore:                   as string
        end_date: end date of the dataset to explore:                       as string
        max_cloud_cover: maximum cloud coverage of the dataset to explore:  as string
        max_results_search: maximum number of scenes to search for,         as int
        max_results_download: maximum number of scenes to download,         as int

    Returns:
        None.
    """

    lat = location['lat']
    lon = location['lon']
    print('\n\nSearching for scenes for the location:', '\nlatitude:', lat, '\nlongitude:', lon)
    PATH_DATA = './'
    PATH_SATELLITE_IMAGES = PATH_DATA + 'satellite_images/'
    PATH_LOCATION = PATH_SATELLITE_IMAGES + location['country'] + '/'

    scenes = api.search(
        dataset=dataset,
        latitude=lat,
        longitude=lon,
        start_date=start_date,
        end_date=end_date,
        max_cloud_cover=max_cloud_cover,
        max_results=max_results_search
    )

    print(f"\n{len(scenes)} scenes found.")
    for scene in scenes:
        print(scene)

    if len(scenes) == 0:
        print("No scene to download !")
        return()

    if dataset.startswith('landsat'):
        number_scenes = 0
        while number_scenes < max_results_download:
            print('\nDownloading scene', number_scenes, '...')
            ee.download(scenes[number_scenes]['landsat_scene_id'], output_dir=PATH_LOCATION, dataset=dataset)
            print('Scene', number_scenes, 'downloaded!')
            number_scenes += 1

    if dataset.startswith('sentinel'):
        number_scenes = 0
        while number_scenes < max_results_download:
            print('\nDownloading scene', number_scenes, '...')
            ee.download(scenes[number_scenes]['sentinel_entity_id'], output_dir=PATH_LOCATION, dataset=dataset)
            print('Scene', number_scenes, 'downloaded!')
            number_scenes += 1

    if len(os.listdir(PATH_LOCATION)) == 0:
        print('Directory', location['country'], 'is empty!')
    else:
        scenes = [f for f in os.listdir(PATH_LOCATION)]
        print('\n')
        print(len(scenes), 'scenes to unzip:')
        for scene in scenes:
            print(scene)
        for scene in tqdm(scenes, desc='Scenes'):
            print('\nUnzipping the scene...')
            print(scene)
            shutil.unpack_archive(PATH_LOCATION + scene, PATH_LOCATION)
            print('Scene unzipped!')
            os.remove(PATH_LOCATION + scene)