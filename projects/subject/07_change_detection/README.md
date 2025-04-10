# Urban Monitoring: Change Detection Bundle

## Introduction

Mapping of an urban landscape has several practical interests in urban planning: better planning of urban areas, estimation of the density of households in a given area, verification of the state of degradation of a road network, etc. On the other hand, the mapping of rural areas has applications related to the agricultural field: estimation of the used and available agricultural area, estimation of forest areas, planning of a new road/route, etc.

In both cases, very high resolution aerial images of the area to be mapped prove to be valuable assets for these different tasks. However, as the surface area of the area to be mapped can be potentially very large, it is necessary to develop appropriate automatic processing. The diversity of the areas to be mapped remains a major obstacle to the development of generic image processing methods.

## Project development

### Objectives

The objective of the project is the automatic *classification* of different images representing urban landscapes of four different cities (Las Vegas, Hong Kong, Shanghai and Toulouse). More specifically, it will divide the image into several *classes*, each associated with a certain semantic object, and assign each pixel to the class to which it belongs, as shown in the figure below. For example, this will detect buildings, roads, trees, etc. The different classes (in other words, the different objects present in the images) are not known a priori, so you will have to define them beforehand, bearing in mind that this definition will influence all the object recognition processes you will use later (you will not, for example, necessarily use the same strategies if you are only trying to detect *buildings*, or if you are trying to separate these buildings into *red buildings* and *grey buildings*).

Moreover, due to the extreme diversity of different urban scenes, it seems very unlikely that *all* objects in these scenes can be classified correctly (in the case of the image shown in the following figure for example, cars do not have a specific class, so they cannot be classified). Thus, you will have to find a compromise to define classes that are general enough, but still precise enough.

You are going to implement your algorithms in Python, so you might as well start using good programming practices with this language right away. It's up to you to organise yourself to harmonise the different scripts you are going to write!

![urban](../docs/figs/Grenoble_classif.png)*Example of land cover
classification of the urban area in Grenoble*

### Resources

You will find the data to be used at the following link: <https://sandbox.intelligence-airbusds.com/web/>

This dataset offers 8 image pairs of four different cities (Las Vegas, Hong Kong, Shanghai and Toulouse) to allow you to compare the changes between the two acquisition dates. Each location is covered by two pairs of images: a pair of Pleiades images (@0.5m.) and a pair of SPOT images (@1.5m.) at approximately one year intervals. The images are available for download and are in DIMAP format.

Las Vegas (USA)

    Pléiades images from 2017-07-27 and 2016-07-22
    SPOT images from 2016-05-12 and 2015-10-24

Hong Kong (China)

    Pléiades images from 2016-01-01 and 2014-12-09
    SPOT images from 2016-11-15 and 2015-10-09

Shanghai (China)

    Pléiades images from 2017-05-27 and 2016-04-19
    SPOT images from 2017-04-23 and 2016-03-16

Toulouse (France)

    Pléiades images from 2017-04-10 and 2016-03-22
    SPOT images from 2017-04-24 and 2016-03-30


## Here are some ideas...

Here are some ideas you can explore:
- Some of the objects you are trying to recognise have common features from one image to another. For example, the roofs of different cities are not all the same colour, but their shape is always more or less rectangular. Similarly, a tree will always appear dark green and relatively round, a road will always be straight, etc. It is up to you to exploit these properties of *shapes* and *colours*, when they seem characteristic of a certain semantic class.
- Images have relatively large dimensions on the one hand, and the objects you are trying to recognise are not composed of single pixels, but rather of "blocks" of pixels. Thus, it may be useful to *segment* the image (divide it into related regions).
- Some objects seem to be easier to recognise than others, so it is up to you to identify the order in which to proceed.

Keep the following points in mind:
- This is a project, not a tutorial. We don't have the exact solution, so don't expect us to give you that solution.
- Besides, a perfect solution most probably does not exist! Your goal is to find the solution that you think is best.
- This solution should be as robust as possible. If you are only working on one image, make sure that the results are still correct by testing your method on another image.
- This is a (very) ambitious project, don't get discouraged!
- The notions acquired during the elective course of image processing will not be sufficient, it is up to you to deepen your knowledge as much as possible (you will find on the net a great number of websites presenting tutorials on image processing techniques, if you look for them). We are of course also available to answer your questions. Enjoy it, be curious, and most importantly, have fun! 😁


---
The dataset used in this project is courtesy of Airbus and can be found
at [https://sandbox.intelligence-airbusds.com/web/](https://sandbox.intelligence-airbusds.com/web/).

The participants working on this project accept the Airbus
[Standard Technical Evaluation
Licence](https://sandbox.intelligence-airbusds.com/web/assets/files/Technical-Evaluation-Licence-December2014.pdf),
[OneAtlas Evaluation Licence](https://sandbox.intelligence-airbusds.com/web/assets/files/Technical-Evaluation-Licence-OneAtlas-20160929.pdf)
and [Catalog API Licence](https://sandbox.intelligence-airbusds.com/web/assets/files/Terms_and_Conditions_for_Airbus_DS_Catalog_API_Service_2015.pdf)
fully and without reserves.
