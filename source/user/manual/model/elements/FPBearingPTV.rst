.. _FPBearingPTV:

FPBearingPTV Element
^^^^^^^^^^^^^^^^^^^^

This command constructs a single friction pendulum bearing element with friction coefficient that depends on sliding velocity; axial pressure; and temperature at the sliding surface. Use with ``-ndm 3 -ndf 6``. For triple pendulum systems with heating see :ref:`TripleFrictionPendulumX`.

.. function:: element FPBearingPTV $eleTag $iNode $jNode $MuRef $IsPressureDependent $pRef $IsTemperatureDependent $Diffusivity $Conductivity $IsVelocityDependent $rateParameter $ReffectiveFP $Radius_Contact $kInitial $matP $matT $matMy $matMz $x1 $x2 $x3 $y1 $y2 $y3 $shearDist $doRayleigh $mass $iter $tol $unit

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTag, |integer|, unique element tag
   $iNode $jNode, |integer|, end nodes
   $MuRef, |float|, reference coefficient of friction at reference pressure and 20 C
   $IsPressureDependent, |integer|, 1 if friction depends on instantaneous axial pressure
   $pRef, |float|, reference axial pressure
   $IsTemperatureDependent, |integer|, 1 if friction depends on temperature at sliding surface
   $Diffusivity, |float|, thermal diffusivity of steel
   $Conductivity, |float|, thermal conductivity of steel
   $IsVelocityDependent, |integer|, 1 if friction depends on sliding velocity
   $rateParameter, |float|, exponent controlling friction-velocity curve shape
   $ReffectiveFP, |float|, effective radius of curvature of sliding surface
   $Radius_Contact, |float|, radius of contact area at sliding surface
   $kInitial, |float|, lateral stiffness before sliding begins
   $matP $matT $matMy $matMz, |integer|, uniaxial material tags for axial; torsion; and rocking directions
   $shearDist, |float|, shear distance from iNode as fraction of element length
   $doRayleigh, |integer|, 1 to include Rayleigh damping contribution from bearing
   $mass, |float|, element mass
   $iter $tol, |integer| |float|, maximum equilibrium iterations and convergence tolerance
   $unit, |integer|, unit system tag (1: N-m-s-C; 2: kN-m-s-C; 3: N-mm-s-C; 4: kN-mm-s-C; 5-8: imperial variants)

.. note::

   1. Element recorders with ``Temperature``, ``FrictionFactors``, and ``MuAdjusted`` return temperature; friction factor history; and adjusted coefficient of friction.

   2. Valid standard :ref:`elementRecorder` queries include ``force``, ``localForce``, ``basicForce``, ``localDisplacement``, and ``basicDisplacement``.

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      element FPBearingPTV 1 1 2 0.06 1 5.0e7 1 4.44e-6 18.0 1 100.0 2.2352 0.2 500.0 1 2 3 4 0.0 0.0 1.0 1.0 0.0 0.0 0.0 0 0.0 100 1.0e-8 1

   2. **Python Code**

   .. code-block:: python

      element('FPBearingPTV', 1, 1, 2, 0.06, 1, 5.0e7, 1, 4.44e-6, 18.0, 1, 100.0,
              2.2352, 0.2, 500.0, 1, 2, 3, 4, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0, 0.0, 100, 1.0e-8, 1)

Code developed by: Manish Kumar, University at Buffalo, SUNY
