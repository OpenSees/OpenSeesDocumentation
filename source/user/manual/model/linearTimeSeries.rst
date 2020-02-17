.. _linearTimeSeries:

Linear TimeSeries
^^^^^^^^^^^^^^^^^

This command is used to construct a TimeSeries object in which the load factor applied is linearly proportional to the time in the domain, i.e. :math:`\lambda = f(t) = cFactor*t`.

.. figure:: figures/LinearTimeSeries.gif
	:align: center
	:figclass: align-center

	Linear Time Series

.. function:: timeSeries Linear $tag <-factor $cFactor>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

      $tag, |integer|,	unique tag among TimeSeries objects
      $cFactor, |float|, the linear factor (optional: default=1.0)

.. admonition:: Example:

   The following code demonstrates how user would create two linear time series, the first with tag **1** has a **1.0** factor, the second **2** has a constant load factor of **20.0**.

   1. **Tcl Code**

   .. code-block:: none

      timeSeries Linear 1
      timeSeries Linear 2 -factor 20.0


   2. **Python Code**

   .. code-block:: python

      timSeries('Linear',  1)
      timSeries('Linear',  2, '-factor', 20.0)


Code Developed by: **fmk**

