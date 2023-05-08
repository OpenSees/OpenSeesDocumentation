#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.append(os.path.abspath('./sphinx_ext/'))


# -- Project information -----------------------------------------------------

numfig = True
numfig_secnum_depth = 3

project = 'OpenSees Documentation'
copyright = '2022, The Regents of the University of California'
author = 'Frank McKenna, Michael Scott, Pedro Arduino, Minjie Zhu'
html_logo = 'OpenSeesLogo.png'

master_doc = 'index'

rst_prolog = """
.. |floatList| replace:: *list float*
.. |integerList| replace:: *list integer*
.. |intList| replace:: *list integer*
.. |listFloat| replace:: *list float*
.. |listInteger| replace:: *list integer*
.. |listInt| replace:: *list integer*
.. |list| replace:: *list*
.. |string| replace:: *string*
.. |float| replace:: *float*
.. |integer| replace:: *integer*
.. |OPS| replace:: OpenSees
.. |OPS link| replace:: `OpenSees app`_
.. _OpenSees app: http://opensees.berkeley.edu/
.. |githubLink| replace:: `OpenSees Github link`_
.. _OpenSees Github link: https://github.com/OpenSees/OpenSees
.. |messageBoard| replace:: `OpenSees Message Board`_
.. _OpenSees Message Board: https://opensees.berkeley.edu/community/index.php
.. |glf| replace:: `Gregory L. Fenves`_
.. _Gregory L. Fenves: http://www.caee.utexas.edu/faculty/directory/fenves
.. |mhs| replace:: `Michael H. Scott`_
.. _Michael H. Scott: https://cce.oregonstate.edu/scott
.. |fmk| replace:: **fmk**
.. |pedro| replace:: `Pedro Arduino`_
.. _Pedro Arduino: https://www.ce.washington.edu/facultyfinder/pedro-arduino
.. |peter| replace:: `Peter Mackenzie-Helnwein`_
.. _Peter Mackenzie-Helnwein: https://www.ce.washington.edu/facultyfinder/peter-mackenzie-helnwein
.. |chris| replace:: `Chris McGann`_
.. _Chris McGann: https://www.canterbury.ac.nz/engineering/contact-us/people/chris-mcgann.html
.. |andreas| replace:: **Andreas Schellenberg**
.. |silvia| replace:: `Silvia Mazzoni`_
.. _`Silvia Mazzoni`: https://www.silviasbrainery.com/
"""	

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'toctree_filter'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
        'analytics_id': 'UA-2431545-1',
	'logo_only': True,
	'prev_next_buttons_location': None,
        "body_max_width": None
}

#  'style_nav_header_background': '#F2F2F2' #64B5F6 #607D8B,

html_css_files = [
	'css/custom.css'
]

html_secnum_suffix = " "

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# For a full list of configuration options see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

