## Instructions for the git repository

*git* is a platform form code control, which allows to:
- Track your code modifications
- Share your code online
- Synchronize your work across different people


## Getting started
- If under Windows, download `Git for Windows`, and launch `git bash`
- If under Linux/Mac, `git` is already installed by default on your kernel


## Managing permissions
- On the Gricad website, login and click on `Edit Profile` on the top right icon
- On the left menu, click on `Access Tokens` and generate a new one:
    - Give a token name (eg: `token_name`)
    - Check `api`
    - Select an expiration date (ending after the end of this project)
    - Finally, click on `Create personal access token`
- Copy the token (a 19-characters key) from the box somewhere safe
- This token will be called `token_key` in the rest of the document


## Forking the original project

- Login to your Gricad account
- Go to `https://gricad-gitlab.univ-grenoble-alpes.fr/dallamum/remote-sensing-projects`
- Fork your project on your private account (click on the button `Fork` on top right)

## Initialize the git repository

- Get your project URL:
    - The git project URL is an identifier of your project, with permission rights
    - On your forked project webpage, click on clone and copy the URL in `clone with HTTPS`
    - The project URL will be something like `https://gricad-gitlab.univ-grenoble-alpes.fr/username/remote-sensing-projects/`
    - Rewrite it as: `https://token_name:token_key@gricad-gitlab.univ-grenoble-alpes.fr/username/remote-sensing-projects/`
    - where:
        - `username` is your specific username in the forked project
        - `token_key` is the token obtained in the `Managing permissions`section
    - The obtained URL will be called from now on `project_uri`
- Go on your command line (git bash under Windows, shell under Linux)
- Go to the folder where you save your projects
- Type `git clone project_uri` to have the version of your forked project on your device


## Setting the original repository as upstream
- Add the original repository as remote source of your repository:
    - ```git remote add upstream https://token_name:token_key@kegricad-gitlab.univ-grenoble-alpes.fr/dallamum/remote-sensing-projects```
    - where `token_key` is the token obtained in the `Managing permissions` section


## Updating your forked repository

- Identify a single person on your group to take care of collecting and 
  updating the code to the repository. This will avoid conflicts between 
  different versions of the code
- Whenever the person in charge want to update your code from your local machine online:
  - `git pull origin master` to download the current version online
  - `git status` to show what files you have changed locally with respect to online
  - `git add .` to inform git that you want to track the new files you added
  - `git commit -m "Commentary"` to save your updates, where `"Commentary"` is a specific explanation on the changes
  - `git push origin master` to upload your changes to the forked repository

## At the end of your project
- In your terminal:
  - `git pull upstream master` to get the most up-to-date version of the central repository
- On the Gricad page of your forked repository:
  - Click on `Merge reauests` on the menu on the left
  - For the source:
    - Select your own project and your currently active
  - For the destination:
    - Select `https://gricad-gitlab.univ-grenoble-alpes.fr/dallamum/remote-sensing-projects` 
    - Select the branch `master`
  - Click on `Send a merge request`
  - Once approved, your code will be uploaded on the central repository


