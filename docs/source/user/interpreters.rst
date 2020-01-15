
*********************
OpenSees Interpreters
*********************

In computer science, an interpreter is a computer program that directly executes instructions written in a programming or scripting language, without requiring them previously to have been compiled into a machine language program. Matlab is a great example of an interpreter. The scripts that the user provides, e.g. a .m file if the user is using Matlab, contains a sequence of instructions written in some high level scriping language.
For OpenSees two popular interpreters have been extended:

1. Tcl
2. Python


The extensions introduce **IDENTICAL** new commands with the same arguments into the interpreter languages read by the interpreters. How the command is expressed in the language is the only difference. The languages to add a node number 3 at location (168.0, 0.0):

1. Tcl
   
.. code-block:: none 
   
   node 3 168.0 0.0

2. Python

.. code-block:: python

   node(3, 168.0,  0.0)








