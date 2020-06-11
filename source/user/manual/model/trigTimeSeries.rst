Trig TimeSeries
^^^^^^^^^^^^^^^

This command is used to construct a TimeSeries object in which the load factor is some trigonometric function of the time in the domain :math:`\lambda = f(t) = \begin{cases}
\text{cFactor} * sin (\frac{2.0 \Pi (t-tStart)}{\text{period}} + \text{shift}), &\text{tStart} <= t <= \text{tFinish}\\
\text{0.0}, &\text{otherwise}\\
\end{cases}`

.. figure:: figures/TrigTimeSeries.gif
	:align: center
	:figclass: align-center

	Trigonometric Time Series

.. function:: timeSeries Trig $tag $tStart $tEnd $period <-factor $cFactor> <-shift $shift>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

      $tag, |integer|,	   unique tag among TimeSeries objects.
      $tStart, |float|, 	   starting time of non-zero load factor
      $tFinish, |float|,	   ending time of non-zero load factor
      $period, |float|,	   characteristic period of sine wave
      $shift, |float|,	   phase shift in radians (optional: default=0.0)
      $cFactor, |float|,   the load factor amplification factor (optional: default=1.0)

.. admonition:: Example:

   The following code demonstrates how user would create a trigonometric time series with a tag of **1**, has a start time of **0.0**, an end time of **10.0**, a period of **1.0**, and a max load factor of **2.0**.

   1. **Tcl Code**

   .. code-block:: none

      timeSeries Trig 1 0.0 10.0 1.0 -factor 2.0


   2. **Python Code**

   .. code-block:: python

      timSeries('Trig',  1, 0.0, 10.0, 1.0, '-factor', 2.0)


Code Developed by: |fmk|
