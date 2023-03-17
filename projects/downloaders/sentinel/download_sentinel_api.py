from datetime import date
from pathlib import Path

from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt


def main():
    # connect to the API
    print("Please insert your username and password. Retrieve it from https://sentinels.copernicus.eu/web/sentinel/home.")
    user = input("Username?\n")
    password = input("Password")
    api = SentinelAPI(
        user=user,
        password=password,
        api_url='https://scihub.copernicus.eu/dhus',
    )
    current_path = Path(__file__).resolve().parent
    save_path = current_path.joinpath("data/")
    geojson_file = save_path.joinpath("jsonfile.json")

    # from geojson:
    footprint = geojson_to_wkt(read_geojson(f"{geojson_file}"))
    products = api.query(
        footprint,
        date=(date(2022, 4, 1), date(2022, 5, 1)),
        platformname='Sentinel-2',
        processinglevel='Level-2A',
        cloudcoverpercentage=(0, 10),
    )
    api.download_all(products=products, directory_path=f"{save_path}")


if __name__ == "__main__":
    main()
