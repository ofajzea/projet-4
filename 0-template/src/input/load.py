# Importing from built-in repositories
import sys

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


# This is required to set your project path
sys.path.append("./../../")


def main():
    # Reading a standard image. Here we use the imageio package.
    # imageio can also read images that are not coded in 8 bits.
    # Other options exist, for example: open-cv
    img = io.imread('./data/cam2_UTC_19-01-02_10-59-59-84.jpg')
    plt.imshow(img)

    # Reading a remote sensing image.
    # imageio can also read images that are not coded in 8 bits.

    gdal_img_info("./data/example_geotiff_1band.tif")
    rio_img_info("./data/example_geotiff_1band.tif")

    # Example of reading an image not coded on 8 bits (here float32)

    filename1 = "./data/example_geotiff_1band.tif"
    img1 = io.imread(filename1)

    print(img1.shape)
    print(img1.dtype)

    # This is a scalar image with floating point values coded on 32 bits
    plt.imshow(img1)
    plt.colorbar()
    plt.show()

    # Example of reading a multispectral image with 7 bands
    filename2 = "./data/example_geotiff_ms.tif"

    img2 = io.imread(filename2)

    print(img2.shape)
    print(img2.dtype)
    print((img2.min(), img2.max()))

    # Visualize an arbitrary combination of 3 bands as a color image
    plt.imshow(img2[:, :, (2, 1, 0)])
    plt.show()

    # Clipping input data to the valid range
    # for imshow with RGB data ([0..1] for floats or[0..255] for integers).

    # Do the same using rasterio (note that the pixel coordinates are
    # expressed in a coordinate reference system (lat, lon))
    img = rasterio.open(filename2)
    # For visualizing an image, use `show` from rasterio
    show(img)

    rio_img_info(filename2)

    # Use gdal for loading an image and matplotlib for visualize it
    dataset = gdal.Open(filename2, gdal.GA_ReadOnly)
    # Note GetRasterBand() takes band no. starting from 1 not 0
    band = dataset.GetRasterBand(1)
    # Get an numpy array
    arr = band.ReadAsArray()

    # Being a numpy array, it is possible to visualize it with matplotlib
    plt.imshow(arr)
    plt.show()

    # Reading a Matlab workspace
    data = loadmat('./data/example_matlab_workspace.mat')
    print(data)

    # Have a look at the content of a dictionary
    print(data.keys())

    # Extract the data of interest, by accessing the dictionary by its key.
    eem = data['Eem']
    # Plot the data
    plt.plot(eem)
    plt.show()


if __name__ == "__main__":
    main()
