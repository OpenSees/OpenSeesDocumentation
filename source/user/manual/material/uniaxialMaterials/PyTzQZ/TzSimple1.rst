.. _TzSimple1:

TzSimple1 Material
^^^^^^^^^^^^^^^^^^

This command is used to construct a TzSimple1 uniaxial material object:

.. function:: uniaxialMaterial TzSimple1 $matTag $tzType $tult $z50 <$c>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, integer tag identifying material
   $soilType, |integer|, 1 or 2. see note.
   $tult, |float|, Ultimate capacity of the t-z material. see notes
   $Z50, |float|, Displacement at which 50% of tult is mobilized in monotonic loading.
   $c, |float|,	 The viscous damping term (optional: default = 0.0). see note.

.. note::

   soilType = 1 Backbone of t-z curve approximates Reese and O'Neill (1987) 

   soilType = 2 Backbone of t-z curve approximates Mosher (1984) relation.

   The argument tult is the ultimate capacity of the t-z material. Note that “t” or “tult” are shear stresses [force per unit area of pile surface] in common design equations, but are both loads for this uniaxialMaterial [i.e., shear stress times the tributary area of the pile].

   The viscous damping term (dashpot) on the far-field (elastic) component of the displacement rate (velocity). Nonzero c values are used to represent radiation damping effects

EQUATIONS and EXAMPLERESPONSES:

The equations describing PySimple1 behavior are described in [BoulangerEtAl1990]_. Only minor changes have been made in its implementation for OpenSees.


The nonlinear t-z behavior is conceptualized as consisting of elastic (:math:`t-z^e`) and plastic (:math:`t-z^p`) components in series. Radiation damping is modeled by a dashpot on the “far-field” elastic component (:math:`t-z^e`) of the displacement rate. Note that :math:`z = z^e + z^p`, and that :math:`t = t^e = t^p`.


The plastic component is described by:

.. math::

   t^p = t_{ult} - (t_{ult} - t^p_0) \left [\frac{c z_{50}}{c z_{50} + | z_p - z^p_0|} \right ]

where :math:`t_{ult} = ` the ultimate resistance of the t-z material in the current loading direction, :math:`t^p_o = t^p` at the start of the current plastic loading cycle, :math:`z^p_0 = z^P` at the start of the current plastic loading cycle, and c = a constant and n = an exponent that define the shape of the :math:`t-z^p` curve.

The elastic component can be conveniently expressed as:

.. math::

   t^e = C_e \frac{t_{ult}}{z_{50}} z^e

where :math:`C_e` = a constant that defines the normalized elastic stiffness. The value of :math:`C_e` is not an independent parameter, but rather depends on the constants c & n (along with the fact that :math:`t = 0.5 t_{ult}` at :math:`z = z_{50}`).

The flexibility of the above equations can be used to approximate different t-z backbone relations. Reese and O’Neill’s (1987) recommended backbone for drilled shafts is closely approximated using c = 0.5, n = 1.5, and Ce = 0.708. Mosher’s (1984) recommended backbone for axially loaded piles in sand is closely approximated using c = 0.6, n = 0.85, and Ce = 2.05. TzSimple1 is currently implemented to allow use of these two default sets of values. Values of tult and z50 must then be specified to define the t-z material behavior.

Viscous damping on the far-field (elastic) component of the t-z material is included for approximating radiation damping. For implementation in OpenSees the viscous damper is placed across the entire material, but the viscous force is calculated as proportional to the component of velocity (displacement rate) that developed in the far-field elastic component of the material. In addition, the total force across the t-z material is restricted to tult in magnitude so that the viscous damper cannot cause the total force to exceed the near-field soil capacity. Users should also be familiar with numerical oscillations that can develop in viscous damper forces under transient loading with certain solution algorithms and damping ratios. In general, an HHT algorithm is preferred over a Newmark algorithm for reducing such oscillations in materials like TzSimple1.

Examples of the cyclic loading response of TzSimple1 are given in the following plots. Note that the response for tzType = 2 has greater nonlinearity at smaller displacements (and hence greater hysteretic damping) and that it approaches tult more gradually (such that t/tult is still well below


.. figure:: figures/TzSimple1.gif
	:align: center
	:figclass: align-center


.. admonition:: Example 

   The following constructs a TzSimple material with tag **102**, soil type **2** (Mosher relationship for backbone), :math:`t_{ult}` of **0.734** and a :math:`Z_{50}` of **0.0000254**. C is set to **0.0** for zero damping.

   1. **Tcl Code**

   .. code-block:: tcl

      uniaxialMaterial TzSimple1 102  2  0.734  2.54e-5  0.0

   2. **Python Code**

   .. code-block:: python

      uniaxialMaterial('TzSimple1', 102, 2, 0.734, 2.54e-5, 0.0)

Code Developed by: `Ross Boulanger <https://faculty.engineering.ucdavis.edu/boulanger/>`_, UC Davis 


.. [BoulangerEtAl1999] Boulanger, R. W., Curras, C. J., Kutter, B. L., Wilson, D. W., and Abghari, A. (1999). "Seismic soil-pile-structure interaction experiments and analyses." Journal of Geotechnical and Geoenvironmental Engineering, ASCE, 125(9): 750-759. Only minor changes have been made in its implementation for OpenSees.



