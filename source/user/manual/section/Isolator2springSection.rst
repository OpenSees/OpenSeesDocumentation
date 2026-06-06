.. _Isolator2springSection:

Isolator2springSection
^^^^^^^^^^^^^^^^^^^^^^

This command constructs a two-spring isolator section based on the Koh and Kelly model for elastomeric bearing buckling, with optional material nonlinearity and strength degradation. In Tcl the command is ``Iso2spring``; in Python it is ``Isolator2spring``.

.. function:: section Iso2spring $secTag $tol $k1 $Fy $k2 $kv $hb $Pe <$Po>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $tol, |float|, convergence tolerance for the internal solution
   $k1, |float|, pre-buckling stiffness
   $Fy, |float|, yield force
   $k2, |float|, post-buckling stiffness
   $kv, |float|, vertical stiffness
   $hb, |float|, bearing height
   $Pe, |float|, Euler buckling load
   $Po, |float|, axial load (optional, default 0)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      section Iso2spring 1 1.0e-6 100.0 50.0 10.0 500.0 6.0 200.0 0.0

   2. **Python Code**

   .. code-block:: python

      ops.section('Isolator2spring', 1, 1.0e-6, 100.0, 50.0, 10.0, 500.0, 6.0, 200.0, 0.0)

Code Developed by: |fmk|
