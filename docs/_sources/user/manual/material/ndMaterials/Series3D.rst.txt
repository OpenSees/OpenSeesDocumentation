.. _Series3D:

Series3D Material Wrapper
^^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a Series3D material object. It is a wrapper that imposes an iso-stress condition to an arbitrary number of previously-defined 3D nDMaterial objects

Theory
""""""

This model imposes a minimal kinematic constraint on the sub-materials such that the macro-scopic strain tensor :math:`\varepsilon_{m}` (i.e. the strain tensor of the wrapper Series3D material) is equal to the volumetric average of the micro-scopic strain tensors :math:`\varepsilon_{i}` (i.e. the strain tensors of each sub-material)

.. math::
   \varepsilon_{m} = \frac{1}{V} \int_{V} \varepsilon_{i} \,dV
   :label: eq_1

The above equation can be rewritten as a weighted sum

.. math::
   \varepsilon_{m} = \sum_{i=1}^{n} \varepsilon_{i}w_{i}
   :label: eq_2

where the weight :math:`w_{i}` is the volume fraction of the i\ :sup:`th`\  sub-material.
Imposing the constraint in :eq:`eq_2` is equivalent to impose forces on each sub-material proportional to each material's volume fraction:

.. math::
   F = C\begin{bmatrix} w_1 & w_2 & ... & w_n \end{bmatrix}
   :label: eq_3

But the force acting on each volume fraction (with its own sub-material) is

.. math::
   F_i = V\sigma_iw_i
   :label: eq_4

therefore, the following equality can be written

.. math::
   F = C\begin{bmatrix} w_1 & w_2 & ... & w_n \end{bmatrix} = V\begin{bmatrix} \sigma_1w_1 & \sigma_2w_2 & ... & \sigma_nw_n \end{bmatrix}
   :label: eq_5

which shows that :eq:`eq_2` actually imposes an iso-stress condition on each sum-material

.. math::
   \frac{C}{V} = \sigma_m = \sigma_1 = \sigma_2 = ... = \sigma_n
   :label: eq_6


.. function:: nDMaterial Series3D $matTag    $tag1 $tag2 ... $tagN   <-weights $w1 $w2 ... $wN> <-maxIter $maxIter> <-relTol $relTol> <-absTol $absTol> <-verbose>



.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $matTag, |integer|, "unique tag identifying this series material wrapper"
   $tag1 $tag2 ... $tagN, N |integer|, "unique tags identifying previously defined nD materials"
   $w1 $w2 ... $wN, N |float|, "weight factors, optional. If not defined, they will be assumed all equal to 1"
   -maxIter, |string|, "string keyword to specify a user-defined maximum number of iterations"
   $maxIter, |integer|, "maximum number of iterations to impose the iso-stress condition, optional, default = 10"
   -relTol, |string|, "string keyword to specify a user-defined relative stress tolerance for the iso-stress condition"
   $relTol, |float|, "relative stress tolerance for the iso-stress condition, optional, default = 1.0e-4"
   -absTol, |string|, "string keyword to specify a user-defined absolute stress tolerance for the iso-stress condition"
   $absTol, |float|, "absolute stress tolerance for the iso-stress condition, optional, default = 1.0e-8"
   -verbose, |string|, "string keyword to activate print of debug information"

Usage Notes
"""""""""""

.. admonition:: Limitations

   * The only material formulation for the Series3D material object is "ThreeDimensional".
   * The only material formulation allowed for the sub-material objects is "ThreeDimensional".

.. admonition:: Responses

   * All responses available for the nDMaterial object: **stress** (or **stresses**), **strain** (or **strains**), **tangent** (or **Tangent**), **TempAndElong**.
   * **material** **$matId** ... : use the **material** keyword followed by the 1-based index of the sub-material (and followed by the desired response) to forward the request to the matId sub-material.
   * **homogenized** ... : use the **homogenized** keyword followed by the desired response to forward the request to all sub-materials, and to compute its weighted average.

.. admonition:: Example 1 - Simple Linear Validation

   | A simple example to validate the Series3D material. First material is twice as stiff as the second one. All weights are assumed equal to 1.
   | The expected results are:
   * equal stress 
   * additive strain
   * strain in the soft material twice as large as the strain in the stiff material

   1. **Tcl Code**

   .. code-block:: tcl

      # the 2D model
      wipe
      model basic -ndm 2 -ndf 2
      
      # 2 young's moduli
      set E1 30000.0
      set E2 [expr $E1*0.5]
      
      # 2 elastic materials
      nDMaterial ElasticIsotropic 1 $E1 0.2
      nDMaterial ElasticIsotropic 2 $E2 0.2
      
      # the Series3D wrapper using all weights = 1
      nDMaterial Series3D 3   1 2
      
      # a triangle
      node 1 0 0
      node 2 1 0
      node 3 0 1
      nDMaterial PlaneStress 100 3
      element tri31 1   1 2 3   1.0 "PlaneStress" 100
      
      # fixity
      fix 1   1 1
      fix 2   0 1
      fix 3   1 0
      
      # a simple ramp
      timeSeries Linear 1
      
      # imposed macroscopic strain in XX component
      set em 0.01
      pattern Plain 1 1 {
      	sp 2 1   $em
      }
      
      # solve
      constraints Transformation
      numberer Plain
      system FullGeneral
      test NormDispIncr 1.0e-6 10 0
      algorithm Newton
      integrator LoadControl 1.0
      analysis Static
      analyze 1
      
      # check responses
      puts "Checking responses"
      set Sm [expr [lindex [eleResponse 1 material 1 stress] 0]]
      set S1 [expr [lindex [eleResponse 1 material 1 material 1 stress] 0]]
      set S2 [expr [lindex [eleResponse 1 material 1 material 2 stress] 0]]
      set SmHom [expr [lindex [eleResponse 1 material 1 homogenized stress] 0]]
      puts "Sm = S1 = S2 = SmHom -> [format {%6.3f = %6.3f = %6.3f = %6.3f} $Sm $S1 $S2 $SmHom] (stresses are equal)"
      set Em [expr [lindex [eleResponse 1 material 1 strain] 0]]
      set E1 [expr [lindex [eleResponse 1 material 1 material 1 strain] 0]]
      set E2 [expr [lindex [eleResponse 1 material 1 material 2 strain] 0]]
      puts "Em = E1 + E2 -> [format {%6.5f = %6.5f + %6.5f} $Em $E1 $E2] (strains are additive since w1=w2=1)"

Code Developed by: **Massimo Petracca** at ASDEA Software, Italy.
