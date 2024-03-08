.. _eleLoad:

eleLoad Command
"""""""""""""""

The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.

.. function:: eleLoad $eleLoad $arg1 $arg2 $arg3 ....

The beam column elements all accept eleLoad commands of the following form:

.. code::

   eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy <$Wx>

.. code::

   eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $xL <$Px>

When NDM=3, the beam column elements all accept eleLoad commands of the following form:

.. code::

   eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy $Wz <$Wx>

.. code::

   eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $Pz $xL <$Px>

.. csv-table:: 
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTags, |intList|,	tags of PREVIOUSLY DEFINED element
   $Wx, |float|, mag of uniformily distributed ref load acting in direction along member length
   $Wy, |float|, mag of uniformily distributed ref load acting in local y direction of element
   $Wz, |float|, mag of uniformily distributed ref load acting in local z direction of element
   $Py, |float|, mag of ref point load acting in direction along member length
   $Py, |float|, mag of ref point load acting in local y direction of element
   $Pz, |float|, mag of ref point load acting in local z direction of element
   $xL	 location of point load relative to node I, prescribed as fraction of element length

.. note::

   The load values are reference loads values, it is the time sereries that provides the load factor. The load factor times the reference values is the load that is actually applied to the node.


.. warning::

   At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.

.. admonition: Example

.. code:: tcl

   set width 20.0
   set W 4000.0;
   timeSeries Linear 1
   pattern Plain 1 1 {
       eleLoad -ele 3 -type -beamUniform [expr -$W/$width]
   }

.. code:: tcl

   width = 20.0;
   W = 4000.0;
   timeSeries('Linear', 1)
   pattern('Plain',1,1)
   eleLoad('-ele',3, '-type', -beamUniform', W/width)

Code Developed by: |fmk|