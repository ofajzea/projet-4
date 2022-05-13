import rasterio as rio

def rio_img_info(path):
    """ Print information on a raster image file with rasterio. """
    img = rio.open(path)
    x_res = (img.bounds.right - img.bounds.left) / img.width
    y_res = (img.bounds.top - img.bounds.bottom) / img.height
    print("name: {}".format(path))
    print("projection: {}".format(img.crs))
    print('dtype: {}'.format(img.meta['dtype']))
    print("height: {}, width: {}, bands: {}".format(img.height, img.width, img.count))
    print("x_res: {}, y_res: {}".format(x_res, y_res))
    print("bounds: {} \n \n".format(img.bounds))
    img.close()