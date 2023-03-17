# Importing standard libraries
from pathlib import Path

# Importing from open source public libraries
import imageio as io
import rasterio
from rasterio.plot import show
from scipy.io import loadmat
from osgeo import gdal
import matplotlib.pyplot as plt

# Importing from local code (written by yourself)
from src.utilities.utils_gdal import gdal_img_info
from src.utilities.utils_rasterio import rio_img_info


def main():
    project_path = Path(__file__).resolve().parents[1]
    # Reading a standard image. Here we use the imageio package.
    # imageio can also read images that are not coded in 8 bits.
    # Other options exist, for example: open-cv
    img = io.imread(f"{project_path}/data/cam2_UTC_19-01-02_10-59-59-84.jpg")
    plt.imshow(img)

    # Reading a remote sensing image.
    # imageio can also read images that are not coded in 8 bits.

    gdal_img_info(f"{project_path}/data/example_geotiff_1band.tif")
    rio_img_info(f"{project_path}/data/example_geotiff_1band.tif")

    # Example of reading an image not coded on 8 bits (here float32)

    filename1 = f"{project_path}/data/example_geotiff_1band.tif"
    img1 = io.imread(filename1)

    print(img1.shape)
    print(img1.dtype)

    # This is a scalar image with floating point values coded on 32 bits
    plt.imshow(img1)
    plt.colorbar()

    # Example of reading a multispectral image with 7 bands
    filename2 = f"{project_path}/data/example_geotiff_ms.tif"

    img2 = io.imread(filename2)

    print(img2.shape)
    print(img2.dtype)
    print((img2.min(), img2.max()))

    # Visualize an arbitrary combination of 3 bands as a color image
    _, ax = plt.subplots()
    ax.imshow(img2[:, :, (2, 1, 0)])

    # Clipping loading data to the valid range
    # for imshow with RGB data ([0..1] for floats or[0..255] for integers).

    # Do the same using rasterio (note that the pixel coordinates are
    # expressed in a coordinate reference system (lat, lon))
    img = rasterio.open(filename2)
    # For visualizing an image, use `show` from rasterio
    _, ax = plt.subplots()
    show(img, ax=ax)

    rio_img_info(filename2)

    # Use gdal for loading an image and matplotlib for visualize it
    dataset = gdal.Open(filename2, gdal.GA_ReadOnly)
    # Note GetRasterBand() takes band no. starting from 1 not 0
    band = dataset.GetRasterBand(1)
    # Get an numpy array
    arr = band.ReadAsArray()

    # Being a numpy array, it is possible to visualize it with matplotlib
    _, ax = plt.subplots()
    ax.imshow(arr)

    # Reading a Matlab workspace
    data = loadmat(f"{project_path}/data/example_matlab_workspace.mat")
    print(data)

    # Have a look at the content of a dictionary
    print(data.keys())

    # Extract the data of interest, by accessing the dictionary by its key.
    eem = data['Eem']
    # Plot the data
    _, ax = plt.subplots()
    ax.plot(eem)
    plt.show()


if __name__ == "__main__":
    main()


