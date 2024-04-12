.. _modelClass:

Model Class
***********

The ``Model`` class is an alternative to the ``model`` command in Python 
that creates an isolated model that is safe from global state corruption. 
An instance of ``Model`` has all of the standard OpenSees modeling commands 
exposed as methods.

.. The command is also used to define the spatial dimension of the subsequent nodes to be added and the number of degrees-of-freedom at each node. 

.. class:: Model(ndm, ndf=None, echo=None)

   Create an isolated model for given number of dimensions and number of DOFs.

   ========================   ===========================================================================
   ``ndm`` |integer|          number of dimensions (1,2, or 3)
   ``ndf`` |integer|          number of dofs (optional, default ``ndm*(ndm+1)/2``)
   ``echo`` *FileLike*        Optional file handle to write command history to.
   ========================   ===========================================================================


.. note:: 

   The ``Model`` class is currently only available in the experimental 
   `opensees <http://pypi.org/project/opensees>`_ Python package, but may
   eventually be added to ``openseespy``.
   To install ``opensees``, just run:

   .. code-block:: bash

      pip install opensees
   
   This experimental package exposes an identical interface to ``openseespy``, but must
   be imported as ``opensees.openseespy`` as opposed to ``openseespy.opensees``. 
   For more information, visit `GitHub <https://github.com/STAIRLab/opensees>`_.


The ``Model`` class prevents inadvertent corruption of global state that may be caused when using
the ``model`` command of OpenSeesPy.
Each instance of a ``Model`` owns a unique instance of an interpreter which can only be manipulated
through the instance itself. This interpreter can be be used from
Python to invoke either Tcl or Python commands to create Nodes, Masses, Materials, Sections, Elements, LoadPatterns, TimeSeries, Transformations, Blocks and Constraints. 
These additional commands are described in the subsequent sections.


.. admonition:: Example:

   The following examples demonstrate the creation of a ``Basic`` model builder that will 
   create nodes with an ``ndm`` of ``2`` and with ``3`` degrees-of-freedom at each node.


   .. code-block:: python

      import opensees.openseespy as ops
      model = ops.Model(ndm=2, ndf=3)

      model.node(1, 2.0, 3.0)
      ...

   Note that ``opensees`` must come before ``openseespy`` in the ``import`` statement.


Code Developed by: *cmp*
