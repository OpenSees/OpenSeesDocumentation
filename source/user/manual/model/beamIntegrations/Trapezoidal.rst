

Trapezoidal
^^^^^^^^^^^

Create a Trapezoidal beamIntegration object.

Two input forms: **prismatic** (one section) or **non-prismatic** (*N* section tags).

.. function:: beamIntegration Trapezoidal tag secTag N

.. function:: beamIntegration Trapezoidal tag N secTag1 secTag2 ... secTagN

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

      beamIntegration Trapezoidal 2 1 6
      beamIntegration Trapezoidal 3 4 1 2 2 1

   2. **Python Code**

   .. code-block:: python

      ops.beamIntegration('Trapezoidal', 2, 1, 6)
      ops.beamIntegration('Trapezoidal', 3, 4, 1, 2, 2, 1)



