Python Install
==============

There are two packages that can be used to install OpenSees from Python:

1. `openseespy <https://pypi.org/project/openseespy>`_ is a Python package developed by Dr. Zhu and Prof. Scott at Oregon State University which provides Python bindings that are designed to feel like Tcl.
2. `sees <https://pypi.org/project/sees>`_ is a Python package developed by a team of researchers at UC Berkeley which exposes the new OpenSeesRT interpreter architecture to provide both a Tcl interpreter and natural Python interpreter simultaneously.

Both packages are actively developed through the central `OpenSees GitHub repository <https://github.com/OpenSees/OpenSees>`_.

Once `Python <https://python.org>`_ is installed, both packages can be installed using ``pip`` on Windows, Mac, or a Linux operating system.



OpenSeesPy
----------

* To install

   ::

      python -m pip install openseespy

      python -m pip install --user openseespy

* To upgrade

   ::

      python -m pip install --upgrade openseespy

      python -m pip install --user --upgrade openseespy
 
* To import

  ::

     import openseespy.opensees as ops


OpenSeesRT
----------

* To install

   ::

      python -m pip install sees


* To upgrade

   ::

      python -m pip install --upgrade sees


* To import

  ::

     import sees.openseespy as ops

