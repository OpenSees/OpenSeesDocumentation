
Python Install
==============

There are two packages that can be used to install OpenSees from Python:

1. `openseespy <https://pypi.org/project/openseespy>`_ is a Python package developed by Dr. Zhu and Prof. Scott at Oregon State University which provides Python bindings that are designed to feel like Tcl.
2. `xara <https://xara.so>`__ is a Python package developed by Claudio Perez and colleagues at UC Berkeley which exposes the new OpenSeesRT interpreter architecture to provide both a Tcl interpreter and Python module simultaneously.

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


xara
----


* To install

  ::

      python -m pip install xara


* To import

  .. code-block:: Python

     import xara


For details on how to run OpenSeesPy and OpenSees Tcl scripts with *xara*, visit the package `documentation <https://xara.so>`__.
