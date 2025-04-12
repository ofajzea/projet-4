# Solar irradiance estimation at GreEn-Er

## Introduction
A weather station is present on the GreEn-Er building (Ense3,
Grenoble-INP) rooftop.
The station is composed by several instruments that can, for example,
measure the wind, the energy produced by photovoltaic panels and the
illumination (or irradiance) hitting at the surface.

The **solar irradiance** is a very interesting physical variable to
monitor as it can be a proxy to estmate the energy produced by
photovoltaic panels.
The measure of the solar irradiance is done by some dedicated sensors
which are present in the station.
In addition, the station is equipped with a **hemispheric camera**
pointing the sky.
This camera acquires an image every hour, which is archived.
An example of an image acquired by the camera is reported below.

![irradiance](../docs/figs/cam2_UTC_19-01-02_10-59-59-84.jpg)*Example of
image acquired in January 2019*

By analysing these images, it is possible to get an estimate of the
solar irradiance at the moment of the acquisition.
However, this requires some processing as the image can present clouds,
the sun and rain droplets.

Solar irradiance values can be also obtained from remote sensing
acquisitions with a relatively coarse spatial resolution (1+ km) but
wide spatial coverage.
Different satellite data may be used for this purpose.
The study [Modica et al., 2010] uses, for example, data from GEOS
satellite but it will be up to you to look at this kind of study and
choose the data that you think are adequate for this project. For example, Meteosat data (Fig. 1)
can also be considered.

## Objective
This project aims at developing a processing chain for estimating the
solar irradiance from images acquired by the hemispheric camera.

The results of the estimation will be compared with the measurements
done by the irradiance sensors.

In addition, this project aims at integrating measurements from
satellite images in order to have an estimate at a larger scale (for example, on the agglomeration
Grenobloise).

## Resources
  * Ense3 GreEn-Er Weather Station
    * <https://ense3.grenoble-inp.fr/fr/l-ecole/station-meteo-green-er>
    * <ftp://meteo-greener-data.g2elab.grenoble-inp.fr/>

  * [Modica et al., 2010] George D. Modica, R. d’Entremont, E. Mlawer, and G.
Gustafson. Short-range solar radiation forecasts in support of smart grid technology,
in Proc. 1st Conf. on Weather, Climate, and the New Energy Economy, Atlanta, GA,
December. 2010.
