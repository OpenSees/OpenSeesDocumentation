.. _NewtonCotes-BeamIntegration:
   

NewtonCotes
^^^^^^^^^^^

This command creates a Newton-Cotes beamIntegration object. Newton-Cotes places integration points uniformly along the element, including a point at each end of the element.  The weights for the uniformly  spaced integration points are tabulated in references on numerical analysis. The force deformation
   response at each integration point is defined by the section.
   The order of accuracy for Gauss-Radau integration is N-1.

Two input forms: **prismatic** (one section) or **non-prismatic** (*N* section tags).

.. function:: beamIntegration NewtonCotes tag secTag N

.. function:: beamIntegration NewtonCotes tag N secTag1 secTag2 ... secTagN

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

      beamIntegration NewtonCotes 2 1 6
      beamIntegration NewtonCotes 3 4 1 2 2 1

   2. **Python Code**

   .. code-block:: python

      ops.beamIntegration('NewtonCotes', 2, 1, 6)
      ops.beamIntegration('NewtonCotes', 3, 4, 1, 2, 2, 1)


