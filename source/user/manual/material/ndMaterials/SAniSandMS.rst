.. _SAniSandMS:

SANISAND-MS Material
^^^^^^^^^^^^^^^^^^^^

**Code Developed by**: `Haoyuan Liu <https://www.linkedin.com/in/haoyuan-liu-059500171/?originalSubdomain=nl>`_ (Norwegian Geotechnical Institute (NGI), formerly TUDelft), `José A. Abell <http://www.joseabell.com>`_ (UANDES, Chile), `Andrea Diambra <https://research-information.bris.ac.uk/en/persons/andrea-diambra>`_ (University of Bristol), and `Federico Pisanò <https://www.tudelft.nl/citg/over-faculteit/afdelingen/geoscience-engineering/sections/geo-engineering/staff/academic-staff/dr-f-federico-pisano>`_ (TU Delft).

This command is used to construct a multi-dimensional SANISAND-MS (``SAniSandMS``) material, which is an extension of the Manzari-Dafalias (SAniSand) model with cyclic ratcheting control using the memory-surface (MS) concept. This allows capturing the ratcheting effects in sands that occur in high-cyclic loading in the presence of a static stress field or in the case of assymetric loading. 

.. figure:: SAniSandMS-fig0a.png
   :align: center
   :width: 400px
   :figclass: align-center

.. admonition:: TCL command:

   nDMaterial SAniSandMS  $matTag $G0 $nu $e_init $Mc $c $lambda_c $e0 $ksi $P_atm $m $h0 $ch $nb $A0 $nd $zeta $mu0 $beta $Den $fabric_flag $flow_flag $intScheme $TanType $JacoType $TolF $TolR

   Please report bugs as an issue on the main OpenSees repositoy and tag ``@jaabell`` 

Where,

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|,	   unique tag identifying material
   $G0, |float|, 	   dimensionless shear modulus constant
   $nu, |float|, 	   Poisson ratio
   $e_init, |float|, 	   initial void ratio
   $Mc, |float|, 	   critical state stress ratio
   $c, |float|, 	   ratio of critical state stress ratio in extension and compression
   $lambda_c, |float|, critical state line constant
   $e0, |float|, reference critical void ratio at p = 0
   $ksi, |float|, critical state line constant
   $P_atm, |float|, atmospheric pressure
   $m, |float|, yield locus opening parameter (radius of yield surface in stress ratio space)
   $h0, |float|, hardening parameter
   $ch, |float|, hardening parameter
   $nb, |float|, bounding surface void ratio dependence parameter  $nb ≥ 0
   $A0, |float|, intrinsic dilatancy parameter
   $nd, |float|, dilatancy surface parameter $nd ≥ 0
   $zeta , |float|, memory surface shrinkage parameter
   $mu0 , |float|, ratcheting parameter
   $beta , |float|, dilatancy memory parameter
   $Den, |float|, mass density of the material
   $fabric_flag , |integer|, (deprecated)
   $flow_flag , |integer|, (deprecated)
   $intScheme , |integer|, constitutive integration method (3: Runge-Kutta 4th order with error control (the only one currently implemented))
   $TanType , |integer|, type of tangent stiffness to report (0: elastic stiffness | 1: continuum elastoplastic stiffness )
   $JacoType , |integer|, placeholder (not used in explicit methods)
   $TolF , |float|, tolerance for yield surface intersection calculation (stress units)
   $TolE, |float|, (adimensional) relative error for explicit integrator


The current implementation on SANISAND-MS uses fourth-order Runge-Kutta with error control for constitutive integration. The strain coming from a finite-element containing SANISAND-MS is applied incrementally by subdividing automatically to keep the constitutive integration error below the parameter ``$TolE``. The integration error :math:`e` is defined as:

.. math::

   e = \max\left\lbrace e_{\sigma},\, e_{\alpha} \right\rbrace \\
   e_{\sigma} = \dfrac{\Vert \sigma^5 - \sigma^4 \Vert}{\Vert \sigma^4 \Vert} \\
   e_{\alpha} = \dfrac{\Vert \alpha^5 - \alpha^4 \Vert}{\Vert \alpha^4 \Vert}

And :math:`\sigma^p` is the stress prediction using a :math:`p`-th order integration formula, and likewise for the backstress :math:`\alpha^p`. Thus, in the code a 5-th order formula to approximate and bound the integration error, while integration advances using the fourth-order equation (RK45).

.. figure:: SAniSandMS-fig0b.png
   :align: center
   :width: 640px
   :figclass: align-center

The above equations differ from those in the main reference by Liu et al. (2019) in that the use of the yield back-stress ratio :math:`\alpha` is resumed here, as in Dafalias and Manzari (2004), to avoid certain numerical inconveniences. 

.. admonition:: Citation information

   If you use SANISAND-MS in your published research work, please cite the main reference ([SANISAND-MS]_) and also inform ``jaabell`` (*at* miuandes *dot* cl), to update the list of published articles and works that use the code.


.. admonition:: Naming convention

   In text documents we use the spelling `SANISAND-MS`, but the OpenSees implementation uses ``SAniSandMS`` to accomodate coding conventions in OpenSees. 



.. admonition:: Available formulations

   The material formulations for the SAniSandMS object are "ThreeDimensional" and "PlaneStrain"

.. admonition:: Recorder queries
   
   Valid Element recorder queries are:
   
   *  ``stress`` returns stress tensor 
   *  ``strain``returns strain tensor 
   *  ``alpha``  for :math:`\mathbf{\alpha}`, the back-stress ratio tensor for the yield surface
   *  ``alphaM``  for :math:`\mathbf{\alpha^M}`, the back-stress ratio tensor for the memory surface
   *  ``alpha_in`` for :math:`\mathbf{\alpha_{in}}`
   *  ``MM`` size of memory surface
   *  ``estrain`` elastic strain tensor


   .. code:: tcl

    recorder Element -eleRange 1 $numElem -time -file stress.out  stress

    #. Elastic or Elastoplastic response could be enforced by
       Elastic:   updateMaterialStage -material $matTag -stage 0
       Elastoplastic:	updateMaterialStage -material $matTag -stage 1





.. admonition:: Example

   This example, provides an asymetric drained triaxial test of the constitutive model to show the effect of ratcheting. First the sample is compressed isotropically to 200KPa, then a cyclic deviator stress is applied. 

   .. literalinclude:: SAniSandMS.tcl
      :language: tcl


   The script produces an output that can be visualized as follows. 

   .. figure:: SAniSandMS-fig1.png
      :align: center
      :width: 600px
      :figclass: align-center

   .. figure:: SAniSandMS-fig2.png
      :align: center
      :width: 600px
      :figclass: align-center

   .. figure:: SAniSandMS-fig3.png
      :align: center
      :width: 600px
      :figclass: align-center

**Main references**

.. [SANISAND-MS] Liu, H. Y., Abell, J. A., Diambra, A., & Pisanò, F. (2019). `Modelling the cyclic ratcheting of sands through <https://www.researchgate.net/publication/328211282_Modelling_the_cyclic_ratcheting_of_sands_through_memory-enhanced_bounding_surface_plasticity>`_. Géotechnique, 69(9), 783-800.

.. [PhDThesis] Liu, H.Y.  (2020). `Constitutive modelling of cyclic sand behaviour for offshore foundations <https://repository.tudelft.nl/islandora/object/uuid%3A6e3ae33c-e95d-474f-8d6b-d8c0f8aa4788?collection=research>`_ (Doctoral dissertation, Delft University of Technology).

**List of works using SANISAND-MS**

.. [1] Liu, H. Y., & Pisano, F. (2019). `Prediction of oedometer terminal densities through a memory-enhanced cyclic model for sand <https://www.icevirtuallibrary.com/doi/pdf/10.1680/jgele.18.00187>`_. Géotechnique Letters, 9(2), 81-88.
 
.. [2] Liu, H. Y., Kementzetzidis, E., Abell, J. A., & Pisanò, F. (2021). `From cyclic sand ratcheting to tilt accumulation of offshore monopiles: 3D FE modelling using SANISAND-MS <https://www.icevirtuallibrary.com/doi/pdf/10.1680/jgeot.20.P.029>`_. Géotechnique, 1-16.

.. [3] Liu, H.Y., & Kaynia, A. M. (2021). `Characteristics of cyclic undrained model SANISAND-MSu and their effects on response of monopiles for offshore wind structures <https://www.icevirtuallibrary.com/doi/pdf/10.1680/jgeot.21.00068>`_. Géotechnique, 1-39.