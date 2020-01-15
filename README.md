## OpenSeesDocumentation

This repo is where the documentation for OpenSees is kept

# Building

1. Building requires sphinx and some packages for sphinx

```
pip install -U sphinx
pip install sphinx_rtd_theme
pip install sphinxcontrib-bibtex
```

2. Download the repo using git from a terminal window

```
git clone https://github.com/OpenSees/OpenSeesDocumentation.git
```

3. Once sphinx is installed and the repo downloaded, cd to docs folder and build it

```
cd OpenSeesDocumentation/docs
make html
```

4. If it works the html files are in the build/html folder

```
xdg-open ./build/html/index.html
````
