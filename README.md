## OpenSeesDocumentation

This repo is where the documentation for OpenSees is kept. The repo contains both source code for building the documentation, and the html pages that github pages serves to the user.

If you are looking for the online documentation, visit the repo through github pages.

https://OpenSees.github.io/OpenSeesDocumentation


# Structure

+ Makefile   - unix Makefile to build the documentation using sphinx
+ make.bat   - windows make.bat to do same thing
+ source     - a directory containing all the restructured text files and images used to create the html file
+ doc        - The folder that is used by github pages. This folder contains final .html files created by sphinx. If you want to make contributions to OpenSsees Documentation, don't bother updating these pages as pull requests with updates here will be rejected. Make the changes to the files in the source directory and make a pull request for these. We will build and update the doc folder.
   

# Building the HTML files

1. Building requires sphinx and some packages for sphinx

```
pip install -U sphinx
pip install sphinx_rtd_theme
```

2. Download the repo using git from a terminal window

```
git clone https://github.com/OpenSees/OpenSeesDocumentation.git
```

3. Once sphinx is installed and the repo downloaded, type make html to build it

```
make html
```

4. If it works the html files are in the build/html folder

on Linux type the following to open a browser with index page

```
xdg-open ./build/html/index.html
````

on a Mac

```
open ./build/html/index.html
```

