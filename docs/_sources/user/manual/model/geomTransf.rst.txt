.. _geomTransf:

Geometric Transformation Command
********************************

The geometric-transformation command is used to construct a coordinate-transformation (CrdTransf) object, which transforms beam element stiffness and resisting force from the basic system to the global-coordinate system. The command has at least one argument, the transformation type. Each type is outlined below.

.. function:: geomTransf transfType? arg1? ...


The type of transformation created and the additional arguments required depends on the transfType? provided in the command.

The following contain information about transfType? and the args required for each of the available geometric transformation types:

.. toctree::
   :maxdepth: 1
   
   geomTransf/Linear
   geomTransf/PDelta
   geomTransf/Corotational


Code Developed by: |fmk|
