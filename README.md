## OpenSeesDocumentation

# Structure

+ Makefile   - unix Makefile to build the documentation using sphinx
+ make.bat   - windows make.bat to do same thing
+ source     - a directory containing all the restructured text files and images used to create the html file
+ doc        - the folder that is used by github pages. this folder contains final .html files created by sphinx
   

This repo is where the documentation for OpenSees is kept

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

```
xdg-open ./build/html/index.html
````

5. to update the code for github pages, type make gitgub
