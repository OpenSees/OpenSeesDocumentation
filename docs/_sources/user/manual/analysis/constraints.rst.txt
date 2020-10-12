
.. _constraints:

constraints Command
*******************

This command is used to construct the ConstraintHandler object. The ConstraintHandler object determines how the constraint equations are enforced in the analysis. Constraint equations define a specified value for a DOF, or a relationship between DOFs.


.. function:: constraints constraintType? arg1? ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
	$constraintType, |string|,  the constraints type
	$args, |list|,   a list of arguments for that type


The following contain information about numbererType? and the args required for each of the available dof numberer types:

The type of ConstraintHandler created and the additional arguments required depends on the constraintType? provided in the command.

The following contain information about numbererType? and the args required for each of the available constraint handler types:

.. toctree::

    PlainConstraints
    PenaltyMethod
    TransformationMethod
    lagrangeMultipliers
