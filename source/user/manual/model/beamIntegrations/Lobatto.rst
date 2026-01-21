
.. _Lobatto-BeamIntegration:
   

Lobatto
^^^^^^^

This command is used to create a Gauss-Lobatto beamIntegration object. Gauss-Lobatto integration is the most common approach for evaluating the response of :doc:`ForceBeamColumn` (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.

.. function:: beamIntegration 'Lobatto' tag secTag N

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$tag",       "|integer|",    "Unique object tag"
   "$sectTag",   "|integer|",    "A previous-defined section"
   "$N",         "|integer|",    "Number of Integration Points along the elementa"
   

.. admonition:: Example:

   The following examples demonstrate the command in Tcl and Python script to add a Lobatto beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

   1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration 'Lobatto' 2 1 6


   2. **Python Code**

   .. code-block:: python

      beamIntegration('Lobatto',2,1,6)
