.. _gimmeMCK:

GimmeMCK Command
-------------------

This command is used to construct a GimmeMCK integrator object. The GimmeMCK Integrator alow the user to return the mass, damping, and stiffness matrix. Depending on the user input, it enable the user to retrieve the desired by using the printA command.

.. function:: integrator GimmeMCK $m $c $k $ki

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $m
     - |float|
     - If the value is not zero, add mass matrix to tangent matrix with factored value as large as the input.
   * - $c
     - |float|
     - If the value is not zero, add damping matrix to tangent matrix  with factored value as large as the input.
   * - $ki
     - |float| 
     - If the value is not zero, add the tangent stiffness matrix to tangent matrix  with factored value as large as the input.
   * - $kt 
     - |float| 
     - If the value is not zero, add the initial stiffness matrix to tangent matrix  with factored value as large as the input.

Theory
^^^^^^
Assembles A = m*M + c*C + kt*KT + ki*KI

.. note::
  * The system used for the model must be FullGeneral
  * To get the desired output (Mass, Stiffness or Damping matrix), you need to print the result using printA command.
  
.. admonition:: Example:


   1. **Tcl Code**

   .. code-block:: tcl

      wipeAnalysis
      system FullGeneral
      integrator GimmeMCK 0. 0. 1.
      analysis Transient

      analyze 1 1
      printA -file "K.txt"

      wipeAnalysis
      system FullGeneral
      integrator GimmeMCK 1. 0. 0.
      analysis Transient

      analyze 1 1
      printA -file "M.txt"


      wipeAnalysis
      system FullGeneral
      integrator GimmeMCK 0. 1. 0.
      analysis Transient

      analyze 1 1
      printA -file "C.txt"


   2. **Python Code**

   .. code-block:: python

      ops.system('FullGeneral')
      ops.analysis('Transient')
      
      # Mass
      ops.integrator('GimmeMCK',1.0,0.0,0.0)
      ops.analyze(1,0.0)
      
      # Number of equations in the model
      N = ops.systemSize() # Has to be done after analyze
      
      M = ops.printA('-ret') # Or use ops.printA('-file','M.out')
      M = np.array(M) # Convert the list to an array
      M.shape = (N,N) # Make the array an NxN matrix
      
      # Stiffness
      ops.integrator('GimmeMCK',0.0,0.0,1.0)
      ops.analyze(1,0.0)
      K = ops.printA('-ret')
      K = np.array(K)
      K.shape = (N,N)
      
      # Damping
      ops.integrator('GimmeMCK',0.0,1.0,0.0)
      ops.analyze(1,0.0)
      C = ops.printA('-ret')
      C = np.array(C)
      C.shape = (N,N)


Code Developed by: |MHS|


.. [MHS2020] Scott, M. H., Gimme All Your Damping, All Your Mass and Stiffness Too (https://portwooddigital.com/2020/05/17/gimme-all-your-damping-all-your-mass-and-stiffness-too/)
