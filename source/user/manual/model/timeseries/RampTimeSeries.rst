.. _RampSeries:

Ramp TimeSeries
^^^^^^^^^^^^^^^^^^

This command is used to construct a TimeSeries object in which the load factor is a linear Ramp function. An optional **-smooth** flag provides an adjustable smoothness, allowing for a smooth transition at the start and end of the ramp. 
The default behavior provides a linear ramp from 0 to 1.0. By providing a smoothness > 0, the time series has a continuous derivative. The smoothing interval is equal to the smoothness factor times half the ramp time.  

The load factor is determined as: 

.. math::
         
   \lambda = f(t) = offset + cFactor * \begin{cases} 0.0 & t < T_{Start}\\
   \left( \frac{\left(t -T_{Start} \right )}{T_{Ramp}}\right)^2\left( \frac{2}{S(2-S))}\right) &t <= T_{Start}+S\left(\frac{T_{Ramp}}{2}\right)\\
   \frac{1}{2}+\left(\frac{t-T_{Start}-\frac{T_{Ramp}}{2}}{T_{Ramp}} \right)\left (\frac{2}{2-S} \right ) &t <= T_{Start}+T_{Ramp}-S\left(\frac{T_{Ramp}}{2}\right )\\
   1-\left(\frac{t-T_{Start}-T_{Ramp}}{T_{Ramp}} \right)^2\left (\frac{2}{S(2-S)} \right ) &t<= T_{Start}+T_{Ramp} \\ 
   1.0 & \text{otherwise} \end{cases} \\

With: :math:`S = smoothness \rightarrow 0<=S<=1.0`


.. figure:: figures/RampTimeSeries.png
   :align: center
   :figclass: align-center

| 

.. function:: timeSeries Ramp $tag? $tStart? $tRamp? <-smooth $smoothness?> <-offset $offset?> <-factor $cFactor?> 


.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

      $tag, |integer|,    unique tag among TimeSeries objects.
      $tStart, |float|,   starting time of non-zero load factor
      $tRamp, |float|,    length of time to perform the ramp
      '-smooth', |string|, optional flag to enable smooth ramp
      $smoothness, |float|, smoothness parameter (optional: 0 ≤ $smoothness ≤ 1   default = 0.0)
     '-offset', |string|, optional flag to provide vertical offset
      $offset, |float|,        vertical offset amount (optional: default = 0.0
     '-factor', |string|, optional flag to provide scale factor
      $cFactor, |float|,  the load factor scale factor (optional: default = 1.0)

| 

.. admonition:: Example 1:


   .. figure:: figures/RampTimeSeries_2.png
	:align: right
	:figclass: align-right

   The following code demonstrates how a user would create a ramp time series with a tag of **1**, has a start time of $tStart = **5.0**, a ramp time of $tRamp = **30.0**, a $smoothness value of **0.25**, an $offset of **-1.0**, and a scale factor of $cFactor = **2.0**. 
   
   1. **Tcl Code**

   .. code-block:: none

      timeSeries Ramp 1 5.0 30.0 -smooth 0.25 -offset -1.0 -factor 2.0 


   1. **Python Code**

   .. code-block:: python

      timeSeries('Ramp', 1, 5.0, 30.0, '-smooth', 0.25, '-offset', -1.0, '-factor', 2.0)
   
   |

   
.. admonition:: Example 2:
   

   .. figure:: figures/RampTimeSeries_3.png
	:align: right
	:figclass: align-right

   The following code demonstrates how a user would create a ramp time series with a tag of **2**, has a start time of $tStart = **10.0**, a ramp time of $tRamp = **30.0**, a $smoothness value of **0.1**, an $offset of **2.0**, and a scale factor of $cFactor = **-2.0**. 
   
   1. **Tcl Code**

   .. code-block:: none

      timeSeries Ramp 2 10.0 30.0 -smooth 0.1 -offset 2.0 -factor -2.0 


   2. **Python Code**

   .. code-block:: python

      timeSeries('Ramp', 2, 10.0, 30.0, '-smooth', 0.1, '-offset', 2.0, '-factor', -2.0)
    
   |

Code Developed by: `Codi McKee <mailto:cmckee@tamu.edu/>`_ (Texas A&M University)



