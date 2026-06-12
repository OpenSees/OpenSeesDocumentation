.. _SSPbrickUP:

SSPbrickUP Element
^^^^^^^^^^^^^^^^^^

This command constructs a stabilized single-point brick element with u-p formulation for analysis of fluid-saturated porous media. Use with ``-ndm 3 -ndf 4``.

.. function:: element SSPbrickUP $eleTag $N1 $N2 $N3 $N4 $N5 $N6 $N7 $N8 $matTag $fBulk $fDen $k1 $k2 $k3 $e $alpha <$b1 $b2 $b3> <-lumped>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $N1 ... $N8, |integer|, eight node tags in standard brick order
   $matTag, |integer|, tag of a previously defined ND material
   $fBulk, |float|, fluid bulk modulus
   $fDen, |float|, fluid mass density
   $k1 $k2 $k3, |float|, permeability in local x; y; and z directions
   $e, |float|, void ratio
   $alpha, |float|, :math:`1 - K_s/K_f` parameter
   $b1 $b2 $b3, |float|, optional body-force components (default 0.0)
   -lumped, |string|, optional flag to use lumped mass matrix

.. note::

   Valid :ref:`elementRecorder` queries include ``force``, ``stress``, and ``material $matNum ...``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element SSPbrickUP 1 1 2 3 4 5 6 7 8 1 2.2e6 1000.0 1.0e-5 1.0e-5 1.0e-5 0.5 1.0

   2. **Python Code**

   .. code-block:: python

      element('SSPbrickUP', 1, 1, 2, 3, 4, 5, 6, 7, 8, 1, 2.2e6, 1000.0, 1.0e-5, 1.0e-5, 1.0e-5, 0.5, 1.0)

Code developed by: Chris McGann, Pedro Arduino, and Peter Mackenzie-Helnwein, University of Washington
