.. _eleLoad:

eleLoad Command
"""""""""""""""

The eleLoad command is used to construct an ElementalLoad object and add it to the enclosing LoadPattern.

.. function:: eleLoad $eleLoad $arg1 $arg2 $arg3 ....

The beam column elements all accept eleLoad commands of the following form.

**Uniform (full span)** – NDM=2:

.. code::

   eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy <$Wx>

**Trapezoidal (partial span, 2D)** – Load varies linearly between *a/L* and *b/L* (normalized, 0 to 1). Transverse and axial intensity at start (*Wy*, *Wx*) and at end (*Wyb*, *Wxb*). Supported by 2D ``elasticBeamColumn`` and ``forceBeamColumn``:

.. code::

   eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wya $Wxa $aOverL $bOverL $Wyb $Wxb

**Point load** – NDM=2:

.. code::

   eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $xL <$Px>

When NDM=3, the beam column elements accept:

.. code::

   eleLoad -ele $eleTag1 <$eleTag2 ....> -type -beamUniform $Wy $Wz <$Wx>

For trapezoidal loads in 3D, use *Wy* *Wz* *Wx* *aOverL* *bOverL* *Wyb* *Wzb* *Wxb*. The 3D ``elasticBeamColumn`` implementation may be triangular rather than trapezoidal; you can combine two element loads (e.g. one uniform, one triangular) to obtain a trapezoid.

.. code::

   eleLoad -range $eleTag1 $eleTag2 -type -beamPoint $Py $Pz $xL <$Px>

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $eleTags, |intList|,  tags of previously defined elements
   $Wy $Wx, |float|,    (uniform) distributed load in local y and x (force/length)
   $Wya $Wxa, |float|,  (trapezoidal) load intensity at start (a) in local y and x
   $aOverL $bOverL, |float|,  (trapezoidal) start and end of segment, fraction of length (0–1)
   $Wyb $Wxb, |float|,  (trapezoidal) load intensity at end (b) in local y and x
   $Wz, |float|,        (3D) distributed load in local z
   $Py $Pz $Px, |float|,  (point) ref load in local y, z, x
   $xL, |float|,        location of point load as fraction of element length from node I

.. note::

   The load values are reference loads values, it is the time sereries that provides the load factor. The load factor times the reference values is the load that is actually applied to the node.


.. warning::

   At the moment, eleLoads do not work with 3D beam-column elements if Corotational geometric transformation is used.

.. seealso::

   Trapezoidal beam loads

.. admonition:: Example

   Uniform distributed load; trapezoidal load on segment from 0.2*L* to 0.8*L* (2D).

   1. **Tcl Code**

   .. code-block:: tcl

      set width 20.0
      set W 4000.0
      set wya -0.5
      set wxa 0.0
      set aOverL 0.2
      set bOverL 0.8
      set wyb -1.0
      set wxb 0.0
      timeSeries Linear 1
      pattern Plain 1 1 {
          eleLoad -ele 3 -type -beamUniform [expr -$W/$width]
          eleLoad -ele 4 -type -beamUniform $wya $wxa $aOverL $bOverL $wyb $wxb
      }

   2. **Python Code**

   .. code-block:: python

      width = 20.0
      W = 4000.0
      wya, wxa = -0.5, 0.0
      aOverL, bOverL = 0.2, 0.8
      wyb, wxb = -1.0, 0.0
      ops.timeSeries('Linear', 1)
      ops.pattern('Plain', 1, 1)
      ops.eleLoad('-ele', 3, '-type', 'beamUniform', -W/width)
      ops.eleLoad('-ele', 4, '-type', 'beamUniform', wya, wxa, aOverL, bOverL, wyb, wxb)

Code Developed by: |fmk|