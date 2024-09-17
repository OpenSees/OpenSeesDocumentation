Python Install
==============

There are two different Python packages that can be used to use OpenSees from Python:

1. `OpenSeesPy <https://pypi.org/project/openseespy>`_ is a Python package developed at Oregon State University which provides Python bindings that are designed to feel like Tcl.
2. `OpenSeesRT <https://pypi.org/project/opensees>`_ is a Python package developed at UC Berkeley which leverages a novel interpreter architecture to provide both a Tcl interpreter and natural Python interpreter simultaneously.

Once `Python <https://python.org>`_ is installed, both packages can be installed using ``pip`` on Windows, Mac, or a Linux operating system.



Install OpenSeesPy
------------------

* To install

   ::

      python -m pip install openseespy

      python -m pip install --user openseespy

* To upgrade

   ::

      python -m pip install --upgrade openseespy

      python -m pip install --user --upgrade openseespy

   
Import OpenSeesPy
-----------------

::

   import openseespy.opensees as ops


Install OpenSeesRT
------------------

* To install

   ::

      python -m pip install opensees


* To upgrade

   ::

      python -m pip install --upgrade opensees


   
Import OpenSeesRT
-----------------

::

   import opensees.openseesrt as ops

