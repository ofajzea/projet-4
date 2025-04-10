# Snow cover estimation based on remote sensing high spatial resolution images

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

This project focuses on producing spatially accurate snow cover maps, by
considering optical satellite remote sensing images with high spatial resolution
(~1-30 m). We will consider acquisitions by satellites such as
Sentinel-2, Landsat, SPOT and Pléiades.
Acquisitions done by high spatial resolution remote sensing satellites
usually comprise images with different characteristics in terms of
spatial and spectral resolutionus. A common step in the processing is to
produce synthetic images of both high spatial and spectral resolution by
**image fusion** (e.g., sharpening the lower spatial resolution bands).

An example of an image acquired by Sentinel-2 over the sourroundings of
Grenoble is given below.

![Sentinel-2](../docs/figs/S2_snow.png)*Sentinel-2 image*

## Objectives
This project aims at automatically estimating the snow cover extent with
a high spatial resolution (~1-10m).
Snow cover products derived from Sentinel-2 and Landsat images already exists
(e.g., see the Let it snow! processing chain). However, these products are not
usually at the highest possible spatial resolution available from the
acquisitions.

This project aims at producing snow cover maps taking advantage of
image fusion techniques for obtaining maps at the highest resolution.
In addition, images acquired by different remote sensing satellites can
also be joinlty taken into account in order to generate a more robust
estimation of the snow cover extent..

## References

*  Let it snow! Operational snow cover product from Sentinel-2 and
   Landsat-8 data: Snow cover estimation developed by CESBIO and CNES.
   <https://labo.obs-mip.fr/multitemp/let-it-snow-development-of-an-operational-snow-cover-product-from-sentinel-2-and-landsat-8-data/>

   * The Let it snow! algorithm is described in:
     * [https://zenodo.org/record/1414452#.YIf-ZRJ8KV4](https://zenodo.org/record/1414452#.YIf-ZRJ8KV4)
     * Gascoin, S., Grizonnet, M., Bouchet, M., Salgues, G., and Hagolle,
  O.: Theia Snow collection: high-resolution operational snow cover maps
  from Sentinel-2 and Landsat-8 data, Earth Syst. Sci. Data, 11,
  493–514, <https://doi.org/10.5194/essd-11-493-2019>, 2019. [Available at
  <https://essd.copernicus.org/articles/11/493/2019/>]

    * Product description:
      <https://labo.obs-mip.fr/multitemp/sentinel-2/snow/>
    * Code:
      <https://gitlab.orfeo-toolbox.org/remote_modules/let-it-snow>

* Resources for downloading images
  - <https://github.com/CS-SI/eodag> (docs: <https://eodag.readthedocs.io/en/latest/intro.html>)
  - <https://github.com/olivierhagolle/theia_download>
  - <https://github.com/sentinelsat/sentinelsat>

* Sentinel-2:
  * <https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2>
  * Data products: <https://sentinels.copernicus.eu/web/sentinel/missions/sentinel-2/data-products>
* Landsat
  * <https://www.usgs.gov/core-science-systems/nli/landsat/landsat-8?qt-science_support_page_related_con=0#qt-science_support_page_related_con>
  * Snow cover products:  <https://www.usgs.gov/core-science-systems/nli/landsat/landsat-fractional-snow-covered-area?qt-science_support_page_related_con=0#qt-science_support_page_related_con>
