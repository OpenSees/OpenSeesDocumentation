.. _Lobatto-BeamIntegration:

Lobatto
^^^^^^^

This command is used to create a Gauss-Lobatto beamIntegration object. Gauss-Lobatto integration is the most common approach for evaluating the response of :doc:`ForceBeamColumn` (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending moments are largest in the absence of interior element loads.

Two input forms are supported:

**Prismatic** – One section for all integration points:

.. function:: beamIntegration Lobatto tag secTag N

**Non-prismatic** – One section tag per integration point (section tags are mapped to Lobatto point locations in order from node *I* to node *J*):

.. function:: beamIntegration Lobatto tag N secTag1 secTag2 ... secTagN

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   tag,       |integer|,  unique beam integration tag
   secTag,    |integer|,  (prismatic) one previously-defined section for all points
   N,         |integer|,  number of integration points
   secTag1 …, |integer|,  (non-prismatic) *N* section tags, one per integration point

.. note::

   The non-prismatic form allows different sections along the element length (e.g. different reinforcement or cross-sections) without using FixedLocation or plastic-hinge integration. Same option exists for Legendre, Radau, NewtonCotes, Trapezoidal, CompositeSimpson, and other distributed plasticity methods.

.. admonition:: Example

   Prismatic: 6 integration points, one section (tag 1). Non-prismatic: 3 sections (tags 1, 2, 1) at the 3 Lobatto points.

   1. **Tcl Code**

   .. code-block:: tcl

      beamIntegration Lobatto 2 1 6
      beamIntegration Lobatto 3 3 1 2 1

   2. **Python Code**

   .. code-block:: python

      ops.beamIntegration('Lobatto', 2, 1, 6)
      secTagList = [1, 2, 1]
      ops.beamIntegration('Lobatto', 3, len(secTagList), *secTagList)
