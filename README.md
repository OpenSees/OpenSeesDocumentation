## OpenSeesDocumentation

This repo is where the documentation for OpenSees is kept

# Building

1. Building requires sphink and some packages for sphink

```
pip install -U sphinx
pip install sphinx_rtd_theme
```

2. Download the repo of course, using git from a terminal window

```
git clone https://github.com/OpenSees/OpenSeesDocumentation.git
```

3. Once sphink is installed & the repo downloaded, cd to docs folder and build it

```
cd OpenSeesDocumentation/docs
make
```