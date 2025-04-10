# Ship detection challenge
Shipping traffic is growing fast. More ships increase the chances of infractions at sea like environmentally devastating ship accidents, piracy, illegal fishing, drug trafficking, and illegal cargo movement. This has compelled many organizations, from environmental protection agencies to insurance companies and national government authorities, to have a closer watch over the open seas.

This project addresses the **Airbus Ship Detection Challenge** which is
a past Kaggle competition focusing on finding ships on satellite images as quickly as possible.
More information at
[https://www.kaggle.com/c/airbus-ship-detection/](https://www.kaggle.com/c/airbus-ship-detection/).

The objective of this project is to **automatically locate ships** in images
by **machine learning**. Many images do not contain
ships, and those that do may contain multiple ships. Ships within and
across images may differ in size (sometimes significantly) and be
located in open sea, at docks, marinas, etc.
Images were acquired under different wheater conditions, so ship
detection might be perfomed also on images with haze and clouds.

The original dataset contains 150,000 JPEG images (768 px by 768 px)
extracted from SPOT satellite imagery at 1.5 meters resolution. The full
dataset is over 29GB. The
images feature tankers, commercial and fishing ships of various shapes
and sizes. Apart from the images, a CSV file provides the oriented bounding boxes around the ships (in run-length encoding format). You will need to define your own split for the training images and the test images.

![Example of image acquired by SPOT for ship detection.](../docs/figs/ships_xs.jpg)

The competition is now over but you can still enrol for late
submissions and see how your automatic ship detection algorithm ranks. Please check the Kaggle website
[https://www.kaggle.com/c/airbus-ship-detection/](https://www.kaggle.com/c/airbus-ship-detection/).

---
The dataset used in this project is courtesy of Airbus and can be found
at [https://sandbox.intelligence-airbusds.com/web/](https://sandbox.intelligence-airbusds.com/web/).

The participants working on this project accept the Airbus
[Standard Technical Evaluation
Licence](https://sandbox.intelligence-airbusds.com/web/assets/files/Technical-Evaluation-Licence-December2014.pdf),
[OneAtlas Evaluation Licence](https://sandbox.intelligence-airbusds.com/web/assets/files/Technical-Evaluation-Licence-OneAtlas-20160929.pdf)
and [Catalog API Licence](https://sandbox.intelligence-airbusds.com/web/assets/files/Terms_and_Conditions_for_Airbus_DS_Catalog_API_Service_2015.pdf)
fully and without reserves.
