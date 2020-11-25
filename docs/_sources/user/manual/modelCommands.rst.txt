Modelling Commands
------------------

These are the commands added to the interpreter to create the finite element model. A finite element model consists of **Nodes**, **Elements**, **Constraints**, and **Loads**. In OpenSees the Constraints are divided into two types: single-point constraints (**SP_Constraints)** for specifying the boundary condition for a specific degree-of-freedom at a node and multiple-point constraints (**MP_Constraints**) for specifying the relationship between the responses between the degrees-of-freedom at two separate nodes. The loads in OpenSees are assigned to **LoadPatterns**. Also associated with load patterns are **TimeSeries** objects ans sometime **SP_Constraints** when the user wants to specify time-varying **SP_Constraints**. 

.. figure:: figures/OpenSeesDomain.png
	:align: center
	:width: 800px
	:figclass: align-center

	OpenSees Model

In OpenSees there are commands to add each of these types of objects to a domain:

.. toctree::
   :maxdepth: 1

   model/model
   model/node
   model/element
   model/spConstraints
   model/mpConstraints
   model/timeSeries
   model/pattern

In addition to these commands, other commands needed for modelling include commands to create the materials used by the elements, commands for damping, and commands for creating blocks of continuum elements. These commands are described in the following sections:

.. toctree::
   :maxdepth: 1

   model/mass
   model/region
   model/damping
   model/block
   model/geomTransf   
