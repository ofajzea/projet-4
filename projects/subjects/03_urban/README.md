# Mapping the Grenoble urban environment by remote sensing

## Introduction

Mapping of an urban landscape has several practical interests in urban planning: better planning of urban areas, estimation of the density of households in a given area, verification of the state of degradation of a road network, etc. On the other hand, the mapping of rural areas has applications related to the agricultural field: estimation of the used and available agricultural area, estimation of forest areas, planning of a new road, etc.

In both cases, very high resolution aerial images of the area to be mapped prove to be valuable assets for these different tasks. However, as the surface of the area to be mapped can be potentially very large, it is necessary to develop appropriate automatic processing. The diversity of the areas to be mapped remains a major obstacle to the development of generic image processing methods.

## Project development

### Objectives


The objective of the project is the automatic *classification* of different images representing urban and rural landscapes of the Grenoble environment. More specifically, it will divide the image into several *classes*, each associated with a certain semantic object, and assign each pixel to the class to which it belongs, as shown in the figure below. In the case of urban images, for example, buildings, roads, trees, etc. will be detected. For rural images, the different classes may correspond to cultivated fields, fallow fields, vegetation, etc. The different classes (in other words, the different objects present in the images) are not known a priori, so you will have to define them beforehand, bearing in mind that this definition will influence all the object recognition processes that you will use later (you will not, for example, necessarily use the same strategies if you are only trying to detect *buildings*, or if you are trying to separate these buildings into *red buildings* and *grey buildings*).

Furthermore, due to the extreme diversity of different urban and rural scenes, it seems very unlikely that *all* of the objects in these scenes can be classified correctly (in the case of the image shown in the following figure, for example, cars do not have a specific class, so they cannot be classified). Thus, you will have to find a compromise to define classes that are general enough, but still precise enough.

You are going to implement your algorithms in Python, so you might as well start using good programming practices with this language right away. It's up to you to organise yourself to harmonise the different scripts you are going to write!

![urban](../docs/figs/Grenoble_classif.png)*Example of land cover
classification of the urban area in Grenoble*

### Resources

It is up to you to download the data you want. Be careful, before downloading a large number of images, check their format and be sure you know how to open/process them. As a reminder, we want to study an area around Grenoble and for images between the beginning of 2019 and today.

You will find the SENTINEL-2 data to be used at the following link: <https://www.copernicus.eu/en/access-data>

## Here are some ideas...

Here are some ideas you can explore:
- Some of the objects you are trying to recognise have common characteristics from one image to another. For example, the roofs of the city of Grenoble are not necessarily all red, but their shape is always more or less rectangular. Similarly, a tree will always appear dark green and relatively round, a road will always be straight, etc. It is up to you to exploit these properties of *shapes* and *colours*, when they seem characteristic of a certain semantic class.
- Images have relatively large dimensions on the one hand, and the objects you are trying to recognise are not composed of single pixels, but rather of "blocks" of pixels. Thus, it may be useful to *segment* the image (divide it into related regions).
- Some objects seem easier to recognise than others, so it is up to you to identify the order in which to proceed.
- You can compare your results with classifications already made (<https://land.copernicus.eu/pan-european/corine-land-cover> or the classifications made by the IGN on <https://www.geoportail.gouv.fr/donnees/parcelles-cadastrales>)

Keep the following points in mind:
- This is a project, not a tutorial. We do not have the exact solution, so there is no need to expect us to give you that solution.
- Besides, a perfect solution most probably does not exist! Your goal is to find the solution that you think is best.
- This solution should be as robust as possible. If you are only working on one image, make sure that the results are still correct by testing your method on another image.
- This is a (very) ambitious project, don't get discouraged!
- The notions acquired during the elective course of image processing will not be sufficient, it is up to you to deepen your knowledge as much as possible (you will find on the net a great number of websites presenting tutorials on image processing techniques, if you look for them). We are of course also available to answer your questions. Enjoy it, be curious, and most importantly, have fun! 😁
