.. _model:

Model Command
*************

This command is used to create the Basic |OPS| model builder. This model builder adds commands to the interpreter which allow the user to build the model. The command is also used to define the spatial dimension of the subsequent nodes to be added and the number of degrees-of-freedom at each node. 

.. function:: model Basic -ndm $ndm <-ndf $ndf>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $ndm, |integer|,  the spatial dimension of problem (1 2 or 3)
   $ndf, |integer|,  number of degrees of freedom at node (optional). 

.. note:: 

   The default value depends on value of ndm: ndm=1 implies ndf=1, ndm=2 implies ndf=3 and ndm=3 implies ndf=6

   The script may contain more than one model command. The script may change the values for ``ndm`` and ``ndf`` in each invocation. This allows elements with different numbers of degrees-of-freedom to be added in the same model.

The additional commands added to the interpreter allow for the construction of Nodes, Masses, Materials (nDMaterial Command, uniaxialMaterial Command), Sections, Elements, LoadPatterns, TimeSeries, Transformations, Blocks and Constraints. These additional commands are described in the subsequent sections.

.. admonition:: Example:

   The following examples demonstrate the command to create a Basic model builder that will create nodes with an **ndm** of 2 and with **3** degrees-of-freedom at each node.

   1. **Tcl Code**

   .. code-block:: tcl

      model Basic -ndm 2 -ndf 3

   2. **Python Code**

   .. code-block:: python

      model('basic', -ndm', 2, '-ndf', 3)


Code Developed by: |fmk|
