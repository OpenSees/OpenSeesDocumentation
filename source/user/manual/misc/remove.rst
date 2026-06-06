.. _remove:

remove Command
**************

This command is used to remove components from the model.

.. function:: remove element $eleTag

   Remove an element from the domain.

.. function:: remove node $nodeTag

   Remove a node from the domain.

.. function:: remove loadPattern $patternTag

   Remove a load pattern from the domain.

.. function:: remove parameter $paramTag

   Remove a parameter from the model.

.. function:: remove recorders

   Remove all recorders.

.. function:: remove recorder $tag

   Remove a single recorder. The tag is the integer returned when the recorder was created.

.. function:: remove sp $nodeTag $dof

   Remove a single-point constraint.

.. function:: remove mp $constrainedNodeTag

   Remove a multi-point constraint.

Code Developed by: |fmk|
