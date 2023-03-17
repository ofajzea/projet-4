from osgeo import gdal
from osgeo import osr


def get_extent(ds):
    """ Return list of corner coordinates from a gdal Dataset """
    xmin, xpixel, _, ymax, _, ypixel = ds.GetGeoTransform()
    width, height = ds.RasterXSize, ds.RasterYSize
    xmax = xmin + width * xpixel
    ymin = ymax + height * ypixel

    return (xmin, ymax), (xmax, ymax), (xmax, ymin), (xmin, ymin)


def reproject_coords(coords,src_srs,tgt_srs):
    """ Reproject a list of x,y coordinates. """
    trans_coords=[]
    transform = osr.CoordinateTransformation( src_srs, tgt_srs)
    for x,y in coords:
        x,y,z = transform.TransformPoint(x,y)
        trans_coords.append([x,y])
    return trans_coords


def gdal_img_info(filename):
    """ Print information on a raster image file with gdal. """
    raster = gdal.Open(filename, gdal.GA_ReadOnly)

    # Get the extent of the image (geographical coordinates of the bounding box)
    # https://gis.stackexchange.com/a/201320

    geoTransform = raster.GetGeoTransform()
    # ulx, uly is the upper left corner, lrx, lry is the lower right corner
    ulx, xres, xskew, uly, yskew, yres  = raster.GetGeoTransform()
    lrx = ulx + xres * raster.RasterXSize
    lry = uly + yres * raster.RasterYSize

    # Get coordinates in lat-lon
    # Setup the source projection - you can also import from epsg, proj4...
    source = osr.SpatialReference()
    source.ImportFromWkt(raster.GetProjection())

    # The target projection
    target = osr.SpatialReference()
    target.ImportFromEPSG(4326)

    # Create the transform - this can be used repeatedly
    transform = osr.CoordinateTransformation(source, target)
    # Transform the point. You can also create an ogr geometry and use the
    # more generic `point.Transform()` transform.TransformPoint(ulx, uly)

    # Read the raster band as separate variable
    band = raster.GetRasterBand(1)
    # Check type of the variable 'band'
    type(band)
    # Data type of the values
    gdal.GetDataTypeName(band.DataType)

    print("name: {}".format(filename))
    print("type: {}".format(type(raster)))
    print("projection: {}".format(raster.GetProjection()))
    print('dtype: {}'.format(gdal.GetDataTypeName(band.DataType)))
    print("height: {}, width: {}, bands: {}".format(
        raster.RasterYSize, raster.RasterXSize, raster.RasterCount)
    )
    print("x_res: {}, y_res: {}".format(xres, yres))
    print("bounds: {}".format(
        (transform.TransformPoint(ulx, uly), transform.TransformPoint(lrx, lry)))
    )
    print("metadata: {}\n\n".format(raster.GetMetadata()))

    band = None
    raster = None
