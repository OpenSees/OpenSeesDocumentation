sp Command
^^^^^^^^^^

This command is used to construct a single-point constraint object and add it to the enclosing LoadPattern.


.. function:: sp $nodeTag $dofTag $dofValue

   $nodeTag, |integer|, tag of node to which constraint is applied.
   $dofTag, |integer|, the degree-of-freedom at the node to which constraint is applied (1 through ndf)
   $dofValue, |integer|, reference constraint value.


.. note:: 
   The $dofValue is a reference value, it is the time series that provides the load factor. The load factor times the reference value is the constraint that is actually applied to the node.
