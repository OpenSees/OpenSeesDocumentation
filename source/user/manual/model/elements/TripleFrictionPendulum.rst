.. _TripleFrictionPendulum:

TripleFrictionPendulum Element
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command constructs a triple friction pendulum bearing element using the series model of Dao et al. (2013). Three friction model objects define sliding behavior at the three active interfaces; four :ref:`uniaxialMaterial` objects define axial and rotational behavior. For the original geometry-based TFP element see :ref:`TripleFrictionPendulumBearing`. For heating effects see :ref:`TripleFrictionPendulumX`.

.. function:: element TripleFrictionPendulum $eleTag $iNode $jNode $frnMdl1 $frnMdl2 $frnMdl3 $matP $matT $matMy $matMz $L1 $L2 $L3 $Ubar1 $Ubar2 $Ubar3 $W $Uy $Kvt $minFv $tol

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $frnMdl1 $frnMdl2 $frnMdl3, |integer|, tags of three friction models
   $matP, |integer|, uniaxial material tag for axial behavior
   $matT, |integer|, uniaxial material tag for torsion
   $matMy $matMz, |integer|, uniaxial material tags for moments about local y and z
   $L1 $L2 $L3, |float|, effective pendulum lengths for the three sliding interfaces
   $Ubar1 $Ubar2 $Ubar3, |float|, displacement capacities at the three interfaces
   $W, |float|, axial load on bearing
   $Uy, |float|, yield displacement for shear behavior
   $Kvt, |float|, vertical stiffness
   $minFv, |float|, minimum vertical force for friction activation
   $tol, |float|, convergence tolerance for internal equilibrium

.. note::

   1. Use with ``-ndm 3 -ndf 6``.

   2. P-Delta moments are transferred entirely to the concave sliding surface (iNode).

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element TripleFrictionPendulum 1 1 2 1 2 3 10 11 12 13 2.0 2.0 4.0 0.5 0.5 1.0 500.0 0.01 1.0e6 10.0 1.0e-8

   2. **Python Code**

   .. code-block:: python

      element('TripleFrictionPendulum', 1, 1, 2, 1, 2, 3, 10, 11, 12, 13,
              2.0, 2.0, 4.0, 0.5, 0.5, 1.0, 500.0, 0.01, 1.0e6, 10.0, 1.0e-8)

Code developed by: Nhan Dao, University of Nevada, Reno
