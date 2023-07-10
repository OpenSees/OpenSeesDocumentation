Sigmoid TimeSeries
^^^^^^^^^^^^^^^^^^

This command is used to construct a TimeSeries object in which the load factor is a Sigmoid-shaped Ramp function of the time in the domain :math:`\lambda = f(t) = \begin{cases} \text{0.0}, & \text{t} < \text{tStart}\\
\text{cFactor} * [1.0 - exp(-\text{a}*(\text{t}-\text{tStart})^b)], &\text{tStart} <= t <= \text{tEnd}\\
\text{cFactor} *\text{1.0}, &\text{otherwise}\\
\end{cases}`

.. figure:: figures/SigTimeSeries.png
	:align: center
	:figclass: align-center

	Sigmoid Time Series

.. function:: timeSeries Sigmoid $tag $tStart $tEnd $a $b <-factor $cFactor> 

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 62

      $tag, |integer|, unique tag among TimeSeries objects.
      $tStart, |float|, starting time of non-zero load factor
      $tEnd, |float|, ending time of non-zero load factor
      $a, |float|, rate parameter ($a > 0)
      $b, |float|, shape parameter ($b > 0, ideally $b > 1.0)
      $cFactor, |float|, the load factor amplification factor (optional: default=1.0)

.. admonition:: Example:

   The following code demonstrates how user would create a sigmoid time series with a tag of **1**, has a start time of $tStart = **0.0**, an end time of $tEnd = **10.0**, a value of $a = **0.01**, and a value of $b = **2.5**.

   1. **Tcl Code**

   .. code-block:: none

      timeSeries Sigmoid 1 0.0 10.0 0.01 2.5 


   2. **Python Code**

   .. code-block:: python

      timSeries('Sigmoid', 1, 0.0, 10.0, 0.01, 2.5)


Code Developed by: |cdm|



