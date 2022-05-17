import imageio
import rasterio


def load_tiff(path):
    """ Loads a tiff file using the imageio library"""
    return imageio.imread(path)
