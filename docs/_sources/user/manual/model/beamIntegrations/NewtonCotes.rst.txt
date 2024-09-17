.. _NewtonCotes-BeamIntegration:
   

NewtonCotes
^^^^^^^^^^^

This command creates a Newton-Cotes beamIntegration object. Newton-Cotes places integration points uniformly along the element, including a point at each end of the element.  The weights for the uniformly  spaced integration points are tabulated in references on numerical analysis. The force deformation
   response at each integration point is defined by the section.
   The order of accuracy for Gauss-Radau integration is N-1.

.. function:: beamIntegration 'NewtonCotes' tag secTag N

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$tag",       "|integer|",    "Unique object tag"
   "$sectTag",   "|integer|",    "A previous-defined section"
   "$N",         "|integer|",    "Number of Integration Points along the elementa"
   

.. admonition:: Example:

   The following examples demonstrate the command in Tcl and Python script to add a NewtonCotes beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

   1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration 'NewtonCotes' 2 1 6


   2. **Python Code**

   .. code-block:: python

      beamIntegration('NewtonCotes',2,1,6)


