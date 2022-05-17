## Project description

Use this space to give a very high level description of your project including:
- Problem statement
- Available resources
- Employed methods
- Validation protocols

## Starting up

- Setting up your project folder
  - Indicating your project folders depends on your IDE
      - For PyCharm, it is defined through `File -> Open project`
      - For Spyder, go through `Projects -> Open Project...`
  - For thr template project the folder would be: ```.\0-template```. 
  - If your project has not already an assigned folder:
    - Copy the template folder and rename it to your project name.
    - E.g., for the snow project:
      - Copy ```.\0-template``` 
      - Paste it and rename it to: ```.\1-snow_hr```
      - Set ```.\1-snow_hr``` as your project folder. 
    - You are allowed to call local imports such as:
         ```import src.utilities.utils_rasterio```
      - The imports are relative folders to the project folder.

- Creating your environment:
    - The projects require to build a virtual environment through `conda`
    - The `miniconda` (a minimal install) installer is available here:
      - ```https://docs.conda.io/en/latest/miniconda.html```
    - Follow the instructions relative to your OS (Windows, Linux, MacOS) 

- Locate your terminal:
  - For Pycharm, the terminal is in the tab below, called `terminal`
  - For Spyder, the terminal is directly your command window

- Importing your project requirements:
  - From your terminal, run:
  ```conda install requirements.txt```
  - This will install the packages you need for your project. 
  - Any additional package needed for your project has to be added to 
    the `requirements.txt` file of your project


## Deliverables

In this project you are required to provide the following material.
Note: All the materials should include the names of all the members of the group.

- For the mid-course:
  - A pdf for the mid-course presentation slides, which has to include:
    - A *problem statement*, that is:
          - The available resources to process;
          - The prospected geographical area and the timeslot under study 
          - The desired products;
          - The methodology to achieve said products (at least in general terms);
          - The ground truth and the measures to compare to it, if applicable.
    - A description of the characteristics of the available sensors, specifically:
          - The *ground sample distance* of each band;
          - The bandwidth coverage of each band;
          - Information on the orbit (revisit time, swath, etc.);
          - Possible applications linked to the sensors.
    - A tutorial on how to download, geolocalize and transform the data into an array:
          - The portal used to download the data;
          - The image and metadata format;
          - Description of the scripts used.

- At the end of the course:
  - A notebook describing how to access the code in your project, which has to include:
    - How download the data from an online platform;
    - A data visualization, highlighting its peculiarities;
    - A script to showcase all the tested methods;
    - Tests, experiments and results comparisons 
    - *NOTE:* The actual code in the notebook has to be minimal, as it has to
      just call the functions contained in your `src` folder
  - A pdf for the final presentation slides, extending the mid-course one with:
    - A description of the methods
    - A visual comparison of the results
  - A final report, which details all the work done during the project
      - Sources used in your work (literature, online repositories)
      - Problem statement, with detailed formulation of the input and outputs
      - Mathematical description of the methods
      - Description of the validation framework
      - Discussion on the results:
        - Objective, through quality indices (presented through tables)
        - Qualitative, by visually comparing the results

## Handing out your deliverables
The deliverables have to be added to your project main folder according to the
project organization described in the following section.
Henceforth, in your project folder:
- `notebooks\YYYY_YYYY`: has to include the Jupyter notebook of your work
- `reports\YYYY_YYYY`: has to contain the presentations and the final report
  -  `YYYY_YYYY` is your academic year (e.g. `2021_2022`)

The deliverables are to be provided through a merge request to the central repository.

The instructions for interfacing through `git` are located in `docs\instructions_git.md`.

## Project Organization

The following folder structure serves as a guideline to standardize the project
structure across different groups and across different academic years.

------------
    project            <- Root folder of your project. Do not add or change any 
    │                     file outside this folder.  
    ├── data           <- Contains a subset of the data, with relatively small  
    │                     size (<10 MB), to run a demo of your script.  
    ├── docs           <- Contains the official documentation related to the  
    │                     dataset, methods, etc.  
    ├── notebooks      <- Contains the Jupyter notebooks to present how to use  
    │   │                 the code from src
    │   └─  2021_2022  <- These are the notebooks that are strictly related to
    │                     to your specific group. The notebooks should import
    │                     the code from the src directory.
    ├── reports        <- Contains reports and presentation
    │   ├── 2021_2022  <- Contains the reports and presentation relative to the
    │   │   │             specific academic year, and exclusively produced by
    │   │   │             your workgroup. 
    │   │   └─ LOG.md                 <- To track the progress at each session
    │   │      presentation_mid.pdf   <- Mid-project presentation slides
    │   │      presentation.pdf       <- Final presentation slides
    │   │      report.pdf             <- Final report
    │   └── figures    <- Raw figures that you generated for your reports
    └── src            <- Contains the source code in Python for the specific  
                          project. Ideally to be expanded upon each year.
    README.md          <- This file, which has to include a generic description
                          of your project.
    requirements.txt   <- Add here a list of all the libraries you included
------------
 