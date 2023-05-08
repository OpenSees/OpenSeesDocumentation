.. _PeerMotion:

PeerMotion TimeSeries
^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a TimeSeries object which, similar to a Path TimeSeries, the load factor obtained is dependent on a series of points obtained from a file. The difference is that the file is obtained from the original Peer strong motion database using an internet connection.

.. function:: timeSeries PeerMotion $tag $eqMotion $station $type $factor <-dT $dT> <-nPTS $nPts>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

      $tag, |integer|,	"unique tag among TimeSeries objects"
      $eqMotion, |string|, "the PEER name for the earthquake"
	  $station, |float|, "a combination of PEER abbreviated station name and direction"
	  $type, |string|, 	"type can be either -ACCEL or -DISP depending on whether you want accelerations or displacements"
	  $factor, |float|, "factor to be applied to the data points, if accel record type you want to specify G"
	  $dT, |float|, "optional, if provided will set the variable nPts equal to number of data points found in record"
	  $nPts, |integer|, "optional, if provided will set the variable dT equal to time interval between points in the record"
	  
.. note::

	* If the time in the domain does not match a data point in record, linear interpolation is performed between nearest points in record.
	* The command can be used with the results obtained from the searchPeerNGA command (hence the craziness of the $eqMotion names).
	* An internet connection is required to run command.

.. admonition:: Example:

   To create 2 time series for two horizontal motions recorded for the Borrego Mtn 1968-04-09 earthquake recorded at the USGS 117 El Centro Array #9 station

   1. **Tcl Code**

   .. code-block:: none

	   timeSeries PeerMotion 1 BORREGO A-ELC180 -ACCEL $G -dT dt -NPTS nPts
	   timeSeries PeerMotion 2 BORREGO A-ELC270 -ACCEL $G


   2. **Python Code**

   .. code-block:: python



Code Developed by: **fmk**

