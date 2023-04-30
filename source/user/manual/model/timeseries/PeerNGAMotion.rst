.. _PeerNGAMotion:

PeerNGAMotion TimeSeries
^^^^^^^^^^^^^^^^^^^^^^^^

This command is used to construct a TimeSeries object which, similar to a Path TimeSeries, the load factor obtained is dependent on a series of points obtained from a file. The difference is that the file is obtained from the `Peer NGA strong motion database <https://peer.berkeley.edu/research/databases>`_ using an internet connection.

.. function:: timeSeries PeerNGAMotion $tag $eqMotion $factor <-dT $dT> <-NPTS $nPts>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

      $tag, |integer|,	"unique tag among TimeSeries objects"
      $eqMotion, |string|, "the PEER NGA name of the motion (a string containing the earthquake name, station & dirn)"
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

	   timeSeries PeerNGAMotion 1 /BORREGO/A-ELC180 $G -dT dt -NPTS nPts
	   timeSeries PeerNGAMotion 2 /BORREGO/A-ELC270 $G


   2. **Python Code**

   .. code-block:: python



Code Developed by: **fmk**

