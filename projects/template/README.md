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
  ```conda install --file requirements.txt```
  - This will install the packages you need for your project. 
  - Any additional package needed for your project has to be added to 
    the `requirements.txt` file of your project


## Project Organization

The following folder structure serves as a guideline to standardize the project
structure across different groups and across different academic years.

------------
    project            <- Root folder of your project. Do not add or change any 
    │                     file outside this folder.  
    ├── data           <- Contains a subset of the data, with relatively small  
    │   │                 size (<10 MB), to run a demo of your script. 
    │   ├── raw        <- Input data
    │   └── outputs    <- Processed data
    ├── docs           <- Contains the official documentation related to the  
    │                     dataset, methods, etc.  
    ├── notebooks      <- Contains the Jupyter notebooks to present how to use
    ├── reports        <- Contains reports and presentation
    │   ├── presentation_mid.pdf   <- Mid-project presentation slides
    │   ├── presentation.pdf       <- Final presentation slides
    │   ├── report.pdf             <- Final report
    │   └── figures    <- Raw figures that you generated for your reports
    └── src            <- Contains the source code in Python for the specific  
                          project. Ideally to be expanded upon each year.
    LOG.md             <- To track the progress at each session
    README.md          <- This file, which has to include a generic description
                          of your project.
    pyproject.toml     <- Add here a list of all the libraries you included
    .gitignore         <- List of folders and files not to upload to git
------------
 