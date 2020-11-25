.. _analyze:

analyze Command
***************

This command is used to perform the analysis. It returns a value indicating success or failure of the analysis. 

.. function:: analyze $numIncr <$dt> <$dtMin $dtMax $Jd>

   $numIncr, |integer|,	number of analysis steps to perform.
   $dt, |float|, time-step increment. Required if transient or variable transient analysis
   $dtMin $dtMax, |float|, minimum and maximum time steps. Required if a variable time step transient analysis was specified.
   $Jd, |integer|, number of iterations user would like performed at each step. The variable transient analysis will change current time step if last analysis step took more or less iterations than this to converge. Required if a variable time step transient analysis was specified.

RETURNS:

0 if successful

<0 if NOT successful


.. admonition:: Static Analysis Example 

   The following example shows how to construct a Static analysis.

   1. **Tcl Code**
   
   .. code:: tcl

      system SuperLU
      constraints Transformation
      numberer RCM
      test NormDispIncr 1.0e-12  10 3
      algorithm Newton
      integrator LoadControl 0.1
      analysis Static
      set ok [analyze 10]

   2. **Python Code**

   .. code:: python

      system('SuperLU');
      constraints('Transformation')
      numberer('RCM')
      test('NormDispIncr',1.0e-12, 10, 3)
      algorithm('Newton')
      integrator('LoadControl', 0.1)
      analysis Static
      ok = analyse(10)


.. admonition:: Transient Analysis Example 

   The following example shows how to construct a Transient analysis.

   1. **Tcl Code**
   
   .. code:: tcl

      system SuperLU
      constraints Transformation
      numberer RCM
      test NormDispIncr 1.0e-12  10 3
      algorithm Newton
      integrator Newmark 0.5 0.25
      analysis Transient -numSubLevels 3  -numSubSteps 10
      set ok [analyze 2000 0.02]


   2. **Python Code**

   .. code:: python

      system('SuperLU');
      constraints('Transformation')
      numberer('RCM')
      test('NormDispIncr',1.0e-12, 10, 3)
      algorithm('Newton')
      integrator('Newmark', 0.5, 0.25)
      analysis('Transient')
      ok = analyze(2000, 0.02)

Code Developed by: |fmk|
