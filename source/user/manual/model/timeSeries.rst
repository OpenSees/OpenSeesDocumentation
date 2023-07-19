.. _timeSeries:

Time Series Command
*******************

This command is used to construct a TimeSeries object which represents the relationship between the time in the domain, :math:`t`, and the load factor applied to the loads, :math:`\lambda`, in the load pattern with which the TimeSeries object is associated, i.e. :math:`\lambda = F(t)`.

.. function:: timeSeries $type $tag $arg1 ...

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $type, |string|,      type of time series
   $tag,  |integer|,     unique time series tag.
   $args, |list|,        a list of arguments with args depending on type


The following subsections contain information about **$type** and the number of nodes and args required for each of the available element types:

.. toctree::
   :maxdepth: 4

   timeseries/constantTimeSeries
   timeseries/linearTimeSeries
   timeseries/trigTimeSeries
   timeseries/RampTimeSeries
   timeseries/triangleTimeSeries
   timeseries/rectangularTimeSeries
   timeseries/pulseTimeSeries
   timeseries/pathTimeSeries
   timeseries/peerMotion
   timeseries/PeerNGAMotion
