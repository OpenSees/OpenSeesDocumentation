Python Install
==============

There are two different Python packages that can be used to use OpenSees from Python:

1. `openseespy <https://pypi.org/project/openseespy>`_ is a Python package developed at Oregon State University which provides Python bindings that are designed to feel like Tcl.
2. `opensees <https://pypi.org/project/opensees>`_ is a Python package developed at UC Berkeley which leverages the new OpenSeesRT interpreter architecture to provide both a Tcl interpreter and natural Python interpreter simultaneously.

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

      python -m pip install opensees


* To upgrade

   ::

      python -m pip install --upgrade opensees


* To import

  ::

     import opensees.openseesrt as ops

