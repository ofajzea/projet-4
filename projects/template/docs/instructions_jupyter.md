# Accessing the Jupyter scripting environment
- You can either access your Jupyter notebook locally or remotely
- Remotely (if you have a Gricad account):
  - Connect yourself to Jupyterhub at `https://jupyterhub.u-ga.fr/` with your Agalan information
  - For all the extra material (typically images or metadata), you will need to upload files through the interface
  - The material is automatically saved online on your account, but the space is limited
  - The Jupyter Gricad internal servers are often down, so try to save a local copy too if possible 
- Locally:
  - Install python on your machine
  - Type `pip install jupyter` in your installation folder
  - Type `jupyter notebook` and browse to your local project folder
  - The notebook is not compatible with older versions of Internet Explorer (before Edge)
  - For this setup, your material is all automatically saved locally on your machine
  - Remember to save your data at the end of the session
- Workaround for Internet Explorer: 
  - On some computers Internet Explorer runs by default when jupyter notebooks are launched
  - Copy your URL from your IE browser to another one of your choice (e.g., Firefox, Chrome, Edge)
    - The URL is typically `http://localhost:8888/` 
  - It will ask you for an authorization token
  - Open a terminal from your taskbar (e.g. through a `conda terminal` on windows)
  - Type `jupyter server list` within it
  - Copy the token that you see as `token_here` below :
    - ```http://localhost:8888/?token=token_here@...```
  - Paste it to your authorization field
- It is also suggested to install `Jupyter Lab`:
  - In your terminal, type:
    - `pip install jupyterlab` to install the package
    - `jupyter lab` to launch your installed notebook
    - Locally your URL will look like `http://localhost:8888/lab/`
    - Jupyter lab allows for more fine control over your notebooks

# The first time to create your working environment
- Open a new notebook Jupyter: `New (up right) -> Python 3`
- In the cell paste `! git clone https://gricad-gitlab.univ-grenoble-alpes.fr/dallamum/remote-sensing-projects`
This command will do a copy/paste of the git repository of the project on your own Jupyterhub environment
- Add different packages you will need (copy/paste this command in a cell of the notebook you created at point 2)): 
  - `! pip install scikit-image`
  - `! pip install opencv-python `
- Create your working branch in your Terminal (`New` -> `Terminal` (last in the bottom)). In the terminal: 
  - Go the right folder using `cd notebooks/remote-sensing-projects/`

- Create the branch `development` where you will develop your project (NEVER work in the branch master) using
`git checkout development`

  - You can check with `git branch` which branches are in your project (will be listed) and in which one you are (the one in green with the `*`)
-When you are in the `development` branch, you will create your data, codes and results folders: `mkdir Data`, `mkdir src` and `mkdir ImportantResults`

  - Your `data` folder will probably be quite large, to avoid putting too much storage in the git, you should explain to git that this folder will **NEVER** be pushed on the git repository (every persons of the group should have it locally). 
    - `git config --global core.excludesFile ~/.gitignore`
    - `cat .gitignore **/.ipynb_checkpoints/`
- In your Home Jupyter (at the beginning of your tree folders), you will create a new folder for your results. 
  - use `cd ..` and then `mkdir results`
  - In your future code, you will need to think about directing your output to this folder (`outpath:"..."`)

- This folder will be only locally to save your results (because you will probably try a lot of stuffs and have then lot of partial results). When you will want to share your important results with your group, just choose which result you want to share and put it in the folder "ImportantResults" of your git repository. 

# Every time you begin to work on your Jupyterhub environment  

Check in which branch you are `git branch` (the one in green with the `*`)
- If you are not in the `development` one, use `git checkout development` to go in it
- You can check again if you are now in the good one

# When changes have been made and you want to upload them to the git on your working branch

In JupyterHub (at the beginning of your folder tree), open a Terminal (`New` -> `Terminal` (last in the bottom)). In the terminal: 

- Go the right folder using `cd notebooks/remote-sensing-projects/`
- Be sure to be in the `development` branch using `git checkout development`
- You now need to make the folder you are in understand that the new files/folders you have created are files you want to put in the git. There are two ways to do this: 
  - You want to add to git **ALL** your documents: `git add .`
  - You want to add to git only certain files or folders: `git add filename.extension` (do this for all files) or `git add <FOLDER>/*` (to add a folder and all the files in it, do this for all the folders you want)
- You will now make a "version" with all these documents that you want to put under git: `git commit -m "Put a comment explaining what you put in git"`
- You can now upload it to your branch in the git: `git push`

### Be careful to use `git pull` sometime to also have your colleagues works locally and be up-to-date with your project (see the tutorials about using git we gave you at the beginning of the project)