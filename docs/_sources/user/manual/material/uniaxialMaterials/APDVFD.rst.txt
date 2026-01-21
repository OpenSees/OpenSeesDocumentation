.. _APDVFD :

APDVFD Material
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a uniaxialMaterial model that simulates the hysteretic responses (axial load-deformation) of an asynchronous parallel double-stage viscous fluid damper (APDVFD) with specific parameters. An adaptive iterative algorithm with a high-precision accuracy has been implemented and validated to solve numerically the constitutive equations. (Specific parameters are shown in Fig. 1.)

.. function:: uniaxialMaterial APDVFD $matTag $K $G1 $G2 $Alpha $L $LC $DP $DG $N1 $N2 $DO1 $DO2 $DC $S $HP $HC <$LGap> <$NM $RelTol $AbsTol $MaxHalf>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material.
   $K, |float|, Elastic stiffness of linear spring to model the axial flexibility of a viscous damper (e.g. combined stiffness of the supporting brace and internal damper portion. The value is usually 10^5N/mm.).
   $G1, |float|, Primary piston hydrodynamic viscosity.
   $G2, |float|, Secondary piston hydrodynamic viscosity.
   $Alpha, |float|, Velocity exponent.
   $L, |float|, The thickness of the total piston (The primary piston is equal to the secondary piston.).
   $LC, |float|, The thickness of the two ends of the secondary piston head (To ensure the secondary piston could smoothly move from the free segment into the damping segment, it is a smaller diameter than that at the middle.).
   $DP, |float|, The diameters of the piston (The primary piston is equal to the secondary piston.).
   $DG, |float|, The diameters of the piston rod.
   $N1, |float|, Number of primary piston circular orifices.
   $N2, |float|, Number of secondary piston circular orifices.
   $DO1, |float|, The diameters of primary piston circular orifices.
   $DO2, |float|, The diameters of secondary piston circular orifices.
   $DC, |float|, Inside diameter of the cylinder (The primary cylinder is equal to the secondary cylinder.).
   $S, |float|, The second-stage activation deformation (The displacement of the secondary piston begins to participate in the work.).
   $HP, |float|, Height of annular gap between cylinder inner surface and piston middle outer surface (The value cannot be zero.).
   $HC, |float|, Height of annular gap between cylinder inner surface and outer surface of piston two ends (The value cannot be zero.).
   $LGap, |float|, Gap length to simulate the gap length due to the pin tolerance.
   $NM, |float|, Employed adaptive numerical algorithm (default value NM = 1; 1 = Dormand-Prince54, 2=6th order Adams-Bashforth-Moulton, 3=modified Rosenbrock Triple).
   $RelTol, |float|, Tolerance for absolute relative error control of the adaptive iterative algorithm (default value 10^-6).
   $AbsTol, |float|, Tolerance for absolute error control of adaptive iterative algorithm (default value 10^-10).
   $MaxHalf, |float|, Maximum number of sub-step iterations within an integration step (default value 15).


.. figure:: figures/APDVFD/APDVFD1.png
	:align: center
	:figclass: align-center

.. note::
Example:
   In order to verify the reliability of the asynchronous parallel double-stage viscous fluid damper, two sets of test and simulation results are selected for verification. Material parameters are shown in the following table (Units can be arbitrarily converted, but must be unified):

.. figure:: figures/APDVFD/APDVFD2.png
	:align: center
	:figclass: align-center
   The input parameters for the material should be as follows: 
    **Tcl Code**

   .. code-block:: tcl


      uniaxialMaterial  APDVFD   1  300  0.009   0.009  0.2238  170  25  179.8 90  6  6  4.5  5  180 20  0.1 0.5
      uniaxialMaterial  APDVFD   1  300  0.013   0.013  0.1986  170  25  179.8 90  6  6  4.5  5  180 20  0.1 0.5
Using these parameters, comparison between the experimental and simulated load-deformation curves of APDVFD1 for sinusoidal displacement increment of 80mm and a frequency f = 0.02Hz is shown in Fig. 2. The comparison between the experimental and simulated load-deformation curves of APDVFD2 for sinusoidal displacement increment of 120mm and a frequency f = 0.02Hz is shown in Fig. 3.



.. figure:: figures/APDVFD/APDVFD3.png
	:align: center
	:figclass: align-center




Code Developed by: Linlin Xie, Cantian Yang, Haoxiang Wang, Aiqun Li, Beijing University of Civil Engineering and Architecture.

References:

[1] Yang C, Wang H, Xie L, Li A, Wang X. “Experimental and theoretical investigations on an asynchronized parallel double-stage viscous fluid damper.” Structural Control and Health Monitoring,(under review).

[2] Akcelyan, S., Lignos, D. G., Hikino, T. (2018). “Adaptive Numerical Method Algorithms for Nonlinear Viscous and Bilinear Oil Damper Models Subjected to Dynamic Loading.” Soil Dynamics and Earthquake Engineering, 113, 488-502.

[3] Oohara, K., and Kasai, K. (2002), “Time-History Analysis Models for Nonlinear Viscous Dampers”, Proc. Structural Engineers World Congress (SEWC), Yokohama, JAPAN, CD-ROM, T2-2-b-3 (in Japanese).
