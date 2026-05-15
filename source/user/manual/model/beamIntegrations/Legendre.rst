Legendre
^^^^^^^^

This command is used to create a Gauss-Legendre beamIntegration object. Gauss-Legendre integration is more accurate than Gauss-Lobatto; however, it is not common in force-based elements because there are no integration points at the element ends. The command places *N* Gauss-Legendre integration points along the element. The location and weight of each integration point are tabulated in references on numerical analysis. The order of accuracy is 2*N*−1.

Two input forms are supported: **prismatic** (one section for all points) and **non-prismatic** (one section tag per integration point).

.. function:: beamIntegration Legendre tag secTag N

.. function:: beamIntegration Legendre tag N secTag1 secTag2 ... secTagN

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   tag,       |integer|,  unique beam integration tag
   secTag,    |integer|,  (prismatic) one previously-defined section
   N,         |integer|,  number of integration points
   secTag1 …, |integer|,  (non-prismatic) *N* section tags, one per point

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration Legendre 2 1 6
      beamIntegration Legendre 3 4 1 2 2 1

   2. **Python Code**

   .. code-block:: python

      ops.beamIntegration('Legendre', 2, 1, 6)
      ops.beamIntegration('Legendre', 3, 4, 1, 2, 2, 1)

