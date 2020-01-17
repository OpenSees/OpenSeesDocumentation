**************
Command Manual
**************

The OpenSees interpreters add `commands <http://en.wikipedia.org/wiki/Command_(computing)>`_ to interpreters, e.g. Python and Tcl, for finite element analysis. Each of these added commands is associated (bound) with a C++ procedure that is provided in the OpenSees Framework. It is this procedure that is called upon by the interpreter to parse the command when it is encountered. In this document we focus primarily on those commands which have been added to these languages. All existing commands that exist in the Tcl and Python languages are available to these interpreters. We provide a brief [[Introduction To Tcl]], more detailed documentation on these existing commands can be found in books and on-line.

For the OpenSees interpreters the commands we have added for finite element analysis can be grouped into four sections:

.. _command-manual:

.. toctree::
   :maxdepth: 1   

   manual/modelCommands
   manual/analysisCommands
   manual/outputCommands
   manual/miscCommands


