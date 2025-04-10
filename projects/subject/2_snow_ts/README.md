# Snow cover estimation based on remote sensing time series

## Introduction

Monitoring the state of the snow cover
on mountains is of interest for forecasting avalanche
risks in winter, and for estimating the expected flow of
rivers during the snowmelt period for a better management of potential
floods and prediction of hydroelectric power production.

Snow cover maps on large geographical areas are mainly obtained from the
analysis of satellite remote sensing imagery.
The quality of the snow cover estimates depends on the technique used
for estimating it but also on the type of data used.
In particular:
1. the resolution of the remote sensing images
2. the temporal frequency of acquisitions.

This project focuses on monitoring of the snow cover maps temporal
evolution.
This analysis will be done considering satellite remote sensing image
time series acquired by medium spatial resolution
(~200-1000 m) optical satellites such as MODIS, Sentinel-3 and VIIRS.
Medium resolution satellites allow to acquire images with a wide spatial
coverage and have typically a high revisit temporal frequency (e.g., in general
one image per day at our latitudes).

An example of images acquired by MODIS over the sourroundings of
Grenoble is given below. Note the evolution of the snow cover between
the two dates and the presence of missing values (black regions
associated to cloud covered areas).

![MODIS_area](../docs/figs/MODIS_area.png)*Area of study*
![MODIS_feb](../docs/figs/MODIS_feb.png)*Example of MODIS image acquired
in february*
![MODIS_may](../docs/figs/MODIS_may.png)*Example of MODIS image acquired
in may*

## Objectives
This project aims at automatically estimating the snow cover extent
using remote sensing image time series acquired by moderate resolution
satellites.
The project will address first the estimation of snow cover maps from a
single image and then will take advantage on the availability of a time
series in order to monitor the temporal evolution of the snow cover
extent (and possibly in terms of type of snow), to have more robust
estimations coping with the presence of missing acquisitions (e.g.,
areas covered by clouds).

## Hints
1. Automatically retrieve images from sensors based on a geographical
   area and date
   - Modis (retrieve snow product at 500m)
   - Sentinel-3
   - VIIRS
2. Pre-process images (e.g., take into account cloud cover maps, sharpen bands at the highest spatial resolution...)
3. Compute NDSI
4. Estimate snow cover map per date
5. Take advantage of the time series for interpolating cloud covered
   areas, get more robust estimates...

Ideas
   - fuse Modis terra and aqua acquisitions
   - fuse MODIS and Sentinel-3
   - test different sharpening techniques

## References
* MODIS:
  * <https://lpdaac.usgs.gov/data/get-started-data/collection-overview/missions/modis-overview/>
  * Snow products <https://nsidc.org/data/modis/index.html>
* Sentinel-3 Mission:
  <https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-3>
* VIIRS: <https://nsidc.org/data/viirs>
* Copernicus DEM data: <https://spacedata.copernicus.eu/web/cscda/dataset-details?articleId=394198>
