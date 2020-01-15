Modelling Commands
------------------

 These are the commands added to the interpreter to create the finite element model. A finite element model consists of nodes, elements, constraints, and loads. In OpenSees the constraints are divided into two types: single-point constraints for specifying the boundary condition for a specific degree-of-freedom at a node and multiple-point constraints for specifying the relationship between the responses between the degrees-of-freedom at two seperate nodes. Loads and single-point constraints are considered to be part of a LoadPatten.

.. toctree::
   :maxdepth: 3

   model/model
   model/node
   model/element
   model/spConstraint

#   model/mpConstraint
#   model/timeSeries
#   model/pattern
#   model/uniaxialMaterial
#   model/ndMaterial
#   model/section
#   model/mass
#   model/region
#   model/rayleigh
#   model/block
#   model/geomTransf   
