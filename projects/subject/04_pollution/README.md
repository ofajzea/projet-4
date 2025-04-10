# Evolution of air pollution related to containment by remote sensing

## Introduction

In the context of the current climate change, air pollution has been increasingly monitored in recent years. One gas of interest that is often monitored is $NO_2$, a pollutant that comes mainly from the use of fossil fuels. With the great decrease in economic activity due to the containment of COVID-19, it is interesting to look at the evolution of $NO_2$ in the atmosphere in recent months. Studies have already been started in different areas in Europe and Asia (https://www.bbc.com/news/science-environment-52065140).

## Project development

### Objectives

This topic is broad enough to observe the evolution of air pollution in relation to containment. A first objective will be to look at what studies have already been started (like the one mentioned in the introduction), what data are used in them, etc. in order to be able to make a similar study of an area near Grenoble.

A second objective will be to exploit the data from the TROPOMI instrument. This instrument is embedded on the SENTINEL-5P satellite and allows the atmosphere to be imaged in order to study its various components (including $NO_2$). In the above-mentioned study, the $NO_2$ maps are looked at directly. It would be interesting to look at this one for the desired geographical study area.

![NO2map](../docs/figs/NO2map.png)*Example of NO2 map*

You are going to implement your algorithms in Python, so you might as well learn the good programming practices with this language right away. It's up to you to organise yourself to harmonise the different scripts you are going to write!

### Resources

It is up to you to download the data you want. Before downloading a large number of images, please check their format and make sure you know how to open/process them. As a reminder, we would like to study the evolution of the last few months.

You can find the TROPOMI data to be used at the following link: <https://s5phub.copernicus.eu/dhus/#/home> (login: s5pguest; password: s5pguest). The $NO_2$ maps can be accessed by filtering the data as shown in the following figure.

![copernicus](../docs/figs/copernicus.png)

To manage your data, you can look at the following links, among others:
- <http://www.acgeospatial.co.uk/sentinel-5p-and-python/>
- <http://www.acgeospatial.co.uk/gee-sentinel-5p-fusion-tables/>
- <https://www.giss.nasa.gov/tools/panoply/download/> (Python Panoply library to visualize TROPOMI data)


## Here are some ideas...

Here are some ideas you can explore:
- This is a very topical subject and you can find a lot of studies already conducted in different parts of the world on the internet. The idea is not to study them exhaustively but to look at what data has been used, how, what the results were and to use this to make your own study on the desired area.
- Information about the TROPOMI instrument and the calculation of gas maps can be found at <http://www.tropomi.eu>

Keep the following points in mind:
- This is a project, not a tutorial. We do not have the exact solution, so there is no need to expect us to give you that solution.
- Besides, a perfect solution most probably does not exist! Your goal is to find the solution that you think is best.
- This solution should be as robust as possible. If you are only working on one image, make sure that the results are still correct by testing your method on another image.
- This is a (very) ambitious project, don't get discouraged!
- The notions acquired during the elective course of image processing will not be sufficient, it is up to you to deepen your knowledge as much as possible (you will find on the net a great number of websites presenting tutorials on image processing techniques, if you look for them). We are of course also available to answer your questions. Enjoy it, be curious, and most importantly, have fun! 😁

