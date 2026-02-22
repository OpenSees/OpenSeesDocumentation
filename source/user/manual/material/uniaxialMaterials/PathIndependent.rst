.. _PathIndependent:

PathIndependent Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a PathIndependent uniaxial material wrapper. The wrapper does not call commitState() on the wrapped material, so the stress-strain response is path-independent: the response depends only on the current strain, not on the loading history.

.. function:: uniaxialMaterial PathIndependent $matTag $otherTag

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag,   |integer|,  unique material tag
   $otherTag, |integer|,  tag of a previously-defined UniaxialMaterial

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial Elastic 1 100.0
      uniaxialMaterial PathIndependent 2 1

   2. **Python Code**

   .. code-block:: python

      ops.uniaxialMaterial('Elastic', 1, 100.0)
      ops.uniaxialMaterial('PathIndependent', 2, 1)

Code developed by: |mhs|
