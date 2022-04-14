## Instructions for the git repository

*git* is a platform form code control, which allows to:
- Track your code modifications
- Share your code online
- Syncronize your work across different people

## Preparation

- Login to your Gricad account
- Go to `https://gricad-gitlab.univ-grenoble-alpes.fr/imspoc_gipsa/remote-sensing-projects`
- Fork your project on your private account (click on the button on top right)

## Initialize the git repository

- If under Windows, download `Git for Windows`, and open `git bash`
- If under Linux, `git` is already installed by default on your kernel

- On your forked project webpage, click on clone and take note of your project uri
- Go on your command line (git bash under Windows, shell under Linux)
- Browse to your work folder and copy the content of your forked repository locally:
  - `git clone project_uri` where project uri is the `ssh` or `http` page of your forked project

## Update the repository

- Identify a single person on your group to take care of collecting and 
  updating the code to the repository. This will avoid conflicts between 
  different versions of the code
- Whenever the person in charge want to update your code from your local machine online:
  - `git pull origin master` to download the current version online
  - `git status` to show what files you have changed locally with respect to online
  - `git add .` to inform git that you want to track the new files you added
  - `git commit -m "Commentary"` to save your updates, where `"Commentary"` is a speific explaination on the changes
  - `git push origin master` to upload your changes to the forked repository

## At the end of your project
- 

