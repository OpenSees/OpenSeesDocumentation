**************
Command Manual
**************


To understand how to run a finite element simulation using OpenSees, it is helpful to have a small understanding of the following abstractions. In OpenSees there exists:

1. The **Model Generator**, code that allows the user to build a finite element model.

2. The **Domain**, code that holds the current state and the last committed state of the finite element model.

3. The **Analysis**, code that moves the state of the model from one converged state to another via a number of trial steps.

4. The **Recorders**, code that allows the user to obtain output from a finite element analysis, e.g. to record the node displacement history.

.. figure:: manual/figures/OpenSeesMainAbstractions.png
	:align: center
	:width: 800px
	:figclass: align-center

	OpenSees Abstractions

The OpenSees interpreters add `commands <http://en.wikipedia.org/wiki/Command_(computing)>`_ to interpreters, e.g. Python and Tcl, to allow the user to specify the model builder, the domain, the analysis and the output. Each of these added commands is associated (bound) with a C++ procedure that is provided in the OpenSees Framework. It is this procedure that is called upon by the interpreter to parse the command when it is encountered. In this document we focus primarily on those commands which have been added to these languages. All existing commands that exist in the Tcl and Python languages are available to these interpreters. We provide a brief [[Introduction To Tcl]], more detailed documentation on these existing commands can be found in books and on-line.

.. _command-manual:

.. toctree::
   :maxdepth: 1   

   manual/modelCommands
   manual/analysisCommands
   manual/outputCommands
   manual/materialCommands
   manual/miscCommands



