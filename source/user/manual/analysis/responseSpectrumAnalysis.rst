.. _responseSpectrumAnalysis:

responseSpectrumAnalysis Command
********************************

|  This command is used to perform a response spectrum analysis.
|  The response spectrum analysis performs N linear analysis steps, where N is the number of eigenvalues requested in a previous call to :ref:`eigen`.
|  For each analysis step, it computes the modal displacements. When the i-th analysis step is complete, all previously defined recorders will be called, so they will record all the results requested by the user, pertaining to the current modal displacements.
|  The modal combination of these modal displacements (and derived results such as beam forces) is up to the user, and can be easily done via TCL or Python scripting.

|  The command can be called in two different ways, depending on how you store the Tn/Sa (response spectrum function) values.
|  They can be either stored in a timeSeries ...

.. function:: responseSpectrumAnalysis $tsTag $direction <-scale $scale> <-mode $mode>

|  ... or in two lists

.. function:: responseSpectrumAnalysis $direction -Tn $Tn -Sa $Sa <-scale $scale> <-mode $mode>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40
   
   $tsTag, |integer|, "The tag of a previously defined :ref:`timeSeries`. This list stores the Tn and Sa values. If you want to use the timeSeries, you cannot specify the -Tn and -Sa options"
   -Tn, |string|, "Tells the command to use the $Tn list, instead of the timeSeries, to get the periods of the response spectrum function"
   $Tn, |floatList|, "The list of periods of the response spectrum function"
   -Sa, |string|, "Tells the command to use the $Sa list, instead of the timeSeries, to get the accelerations of the response spectrum function"
   $Sa, |floatList|, "The list of accelerations of the response spectrum function"
   $direction, |integer|, "The 1-based index of the excited DOF (1 to 3 for 2D problems, or 1 to 6 for 3D problems)."
   -scale, |string|, "Tells the command to use a user-defined scale factor for the computed modal displacements. Not used, placeholder for future implementation."
   $scale, |float|, "User-defined scale factor for the computed modal displacements. Not used, placeholder for future implementation."
    -mode, |string|, "Tells the command to compute the modal displacements for just 1 specified mode (by default all modes are processed)."
   $mode, |integer|, "The 1-based index of the unique mode to process."

.. note::
   *  This command can be used only if a previous call to :ref:`eigen` and :ref:`modalProperties` has been performed.
   *  It computes only the modal displacements, any modal combination is up to the user.
   *  The scale factor (-scale $scale) for the output modal displacements is not used now, and it's there for future implementations. When your model is linear elastic there is no need to use this option. It will be useful in future when we will allow using this command on a nonlinear model as a **linear perturbation** about a certain nonlinear state. In that case, the scale factor can be set to a very small number, so that the computed modal displacements will be very small (linear perturbation) and will not alter the nonlinear state of your model. Then the inverse of the scale factor can be used to post-multiply any result for post-processing.

Theory
^^^^^^
|  Once the eigenvalue problem (:ref:`eigen`) has been solved, and once the modal properties (:ref:`modalProperties`) have been computed, the modal displacements :math:`U` for mode :math:`i` at node :math:`n` and DOF :math:`j` is given by

.. math::
   U_{ij}^n = \frac{\Phi_{ij}^n \cdot MPF_{ij} \cdot RSf\left(T_i\right)}{\lambda_i}

|  where:
   
   *  :math:`\lambda_i` is the eigenvalue
   *  :math:`\Phi_{ij}^n` is the eigenvector
   *  :math:`MPF_{ij}` is the modal participation factor
   *  :math:`RSf\left(T_i\right)` is the response spectrum function value at period :math:`T_i`
   *  and :math:`T_i` is the period :math:`\frac{2\pi}{\sqrt{\lambda_i}}`

.. admonition:: Example 1: Simple call
   
   The following example shows how to call the responseSpectrumAnalysis command for all modes, using the time series 1 (or lists Tn and Sa) along the DOF 1 (Ux)

   1. **Tcl Code using timeSeries**
   
   .. code:: tcl

      set tsTag 1; # use the timeSeries 1 as response spectrum function
      set direction 1; # excited DOF = Ux
      responseSpectrumAnalysis $tsTag $direction

   2. **Tcl Code using lists**
   
   .. code:: tcl

      set Tn {0.0 0.1 0.4 .... }; # the periods
      set Sa {1.9 3.7 4.9 .... }; # the accelerations
      set direction 1; # excited DOF = Ux
      responseSpectrumAnalysis $direction -Tn $Tn -Sa $Sa

   3. **Tcl Code using expanded lists**
   
   .. code:: tcl

      set Tn {0.0 0.1 0.4 .... }; # the periods
      set Sa {1.9 3.7 4.9 .... }; # the accelerations
      set direction 1; # excited DOF = Ux
      responseSpectrumAnalysis $direction -Tn {*}$Tn -Sa {*}$Sa

   4. **Python Code using timeSeries**

   .. code:: python

      tsTag = 1 # use the timeSeries 1 as response spectrum function
      direction = 1 # excited DOF = Ux
      responseSpectrumAnalysis(tsTag, direction)

   5. **Python Code using lists**

   .. code:: python

      Tn = [0.0 0.1 0.4 .... ] # the periods
      Sa = [1.9 3.7 4.9 .... ] # the accelerations
      responseSpectrumAnalysis(direction, '-Tn', *Tn, '-Sa', *Sa)

.. admonition:: Example 2: Iterative call
   
   The following example shows how to call the responseSpectrumAnalysis command for 1 mode at a time, using the time series 1 along the DOF 1 (Ux)

   1. **Tcl Code**
   
   .. code:: tcl

      set tsTag 1; # use the timeSeries 1 as response spectrum function
      set direction 1; # excited DOF = Ux
      for {set i 0} {$i < $num_modes} {incr i} {
         responseSpectrumAnalysis $tsTag $direction -mode [expr $i+1]
         # grab your results here for the i-th modal displacements
      }

   2. **Python Code**

   .. code:: python

      tsTag = 1 # use the timeSeries 1 as response spectrum function
      direction = 1 # excited DOF = Ux
      for i in range(num_modes):
         responseSpectrumAnalysis(tsTag, direction, '-mode', i+1)
         # grab your results here for the i-th modal displacements

.. admonition:: Example 3: Complete Structural Example
   
   .. figure:: figures/responseSpectrumAnalysis.png
       :align: center
       :figclass: align-center
   
   |  The following example show a simple 1-bay 2-story building with rigid diaphragms. Units are **Newton** and **meters**.
   |  It shows how to:
   
      *  call the :ref:`eigen` to extract 7 modes of vibration
      *  call the :ref:`modalProperties` to generate the report with modal properties
      *  call the :ref:`responseSpectrumAnalysis` to compute the modal displacements and section forces
         *  in a first example the :ref:`responseSpectrumAnalysis` is called for all modes. Results are obtained from a recorder after the analysis.
         *  in a second example the :ref:`responseSpectrumAnalysis` is called in a for-loop mode-by-mode. Results are obtained within the for-loop usin the :ref:`eleResponse`
      *  do a CQC modal combination
   
   |  :download:`responseSpectrumAnalysisExample.tcl <codeExample/responseSpectrumAnalysisExample.tcl>`   **(TCL)**.
   |  :download:`responseSpectrumAnalysisExample.py <codeExample/responseSpectrumAnalysisExample.py>`   **(Python)**.


Code Developed by: **Massimo Petracca** at ASDEA Software, Italy
