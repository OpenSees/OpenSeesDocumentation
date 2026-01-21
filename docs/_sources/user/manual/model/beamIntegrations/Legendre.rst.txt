Legendre  
^^^^^^^^

   This command is used to create a Gauss-Legendre beamIntegration object. Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common in force-based elements because there are no integration points at the element ends. The command places ``N`` Gauss-Legendre integration points along the element. The location and weight of each integration point are tabulated in references on numerical analysis.  The force deformation response at each integration point is defined by the section. The order of accuracy for Gauss-Legendre integration is 2N-1.
   
.. function:: beamIntegration 'Legendre' tag secTag N

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   "$tag",       "|integer|",    "Unique object tag"
   "$sectTag",   "|integer|",    "A previous-defined section"
   "$N",         "|integer|",    "Number of Integration Points along the elementa"
   

.. admonition:: Example:

   The following examples demonstrate the command in Tcl and Python script to add a Legendre beam integration with tag 2 and 6 integration points that uses the previously defined section whose tag is 1.

   1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration 'Legendre' 2 1 6


   2. **Python Code**

   .. code-block:: python

      beamIntegration('Legendre',2,1,6)

