.. _eleRespone:

eleResponse Command
*******************

This command is used to obtain state information from the element. The quantities that can be obtained from the element are the same as that whcih can be obtained using the :ref:`elementRecorder`.

.. function:: eleResponse $eleTag $arg1 $arg2 ....

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, integer tag identifying element
   $args,  |list|, list of the arguments

.. note::
   
   #. The values obtained are for the current state of the element. 
   #. The arguments are specific to the type of element being used and are the same as those that are used in :ref:`elementRecorder`.
   
.. admonition:: Example:

   Then following code can be used to obtain the current state related to the **forces** and the **material stress** in element **1**, a Truss element.

   1. **Tcl Code**

   .. code-block:: none

      set eleForces [eleResponse 1 forces]
      set eleMatStress [eleResponse 1 material stress]

   1. **Python Code**

   .. code-block:: python

      eleForces = eleResponse(1,'forces')
      eleMatStress = eleResponse(1, 'material','stress')

Code developed by: |fmk|

