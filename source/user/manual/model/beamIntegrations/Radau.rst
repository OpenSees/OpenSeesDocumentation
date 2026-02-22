.. include:: sub.txt


Radau
^^^^^

To create a Gauss-Radau beamIntegration object. Gauss-Radau integration is not common in force-based elements because it places an integration point at only one end of the element; however, it forms the basis for optimal plastic
   hinge integration methods.

   Places ``N`` Gauss-Radau integration points along the element with a point constrained to be at ndI. The location and weight of each integration point are tabulated in references on
   numerical analysis. The force-deformation response at each integration point is defined
   by the section. The order of accuracy for Gauss-Radau integration is 2N-2.

Two input forms: prismatic (one section) or non-prismatic (N section tags).

.. function:: beamIntegration Radau tag secTag N

.. function:: beamIntegration Radau tag N secTag1 secTag2 ... secTagN

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   tag,       |integer|,  unique beam integration tag
   secTag,    |integer|,  (prismatic) one previously-defined section
   N,         |integer|,  number of integration points
   secTag1 ..., |integer|,  (non-prismatic) N section tags, one per point

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration Radau 2 1 6
      beamIntegration Radau 3 4 1 2 2 1

   2. **Python Code**

   .. code-block:: python

      ops.beamIntegration('Radau', 2, 1, 6)
      ops.beamIntegration('Radau', 3, 4, 1, 2, 2, 1)


