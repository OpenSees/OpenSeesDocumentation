.. _envelopeElementRecorder:

Envelope Element Recorder
^^^^^^^^^^^^^^^^^^^^^^^^^

The EnvelopeElement recorder tracks the minimum, maximum, and maximum absolute value of element response quantities over the analysis. The response arguments are the same as for the :ref:`elementRecorder`; see that page for fiber and section recording options.

.. function:: recorder EnvelopeElement <-file $fileName> <-xml $fileName> <-binary $fileName> <-tcp $inetAddress $port> <-precision $nSD> <-time> <-dT $deltaT> <-rTolDt $rTol> <-closeOnWrite> <-ele $ele1 $ele2 ...> <-eleRange $startEle $endEle> <-region $regionTag> $responseArgs
   :noindex:

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $fileName, |string|, file to which output is sent
   $inetAddr, |string|, IP address of remote machine (with ``-tcp``)
   $port, |integer|, TCP port on remote machine
   $nSD, |integer|, number of significant digits (optional, default 6)
   -time, |string|, include the time at which each envelope extremum occurred
   $deltaT, |float|, time interval for updating the envelope
   $rTol, |float|, relative tolerance on $deltaT (optional, default 0.00001)
   -closeOnWrite, |string|, open and close the output file on each write
   $ele1 $ele2 ..., |listInt|, element tags to record
   $startEle $endEle, |integer|, inclusive range of element tags
   $regionTag, |integer|, tag of a previously defined :ref:`region`
   $responseArgs, |list|, element response request (e.g. ``globalForce``, ``localForce``, ``section 1 force``)

.. note::

   1. Only one of ``-file``, ``-xml``, ``-binary``, or ``-tcp`` may be used to specify the output destination.

   2. Only one of ``-ele``, ``-eleRange``, or ``-region`` may be used to select elements.

   3. For each recorded quantity, the output contains three values: minimum, maximum, and maximum absolute value. When ``-time`` is used, the time at which each extremum occurred is also recorded.

   4. Common beam-column response requests include ``globalForce``, ``localForce``, ``section $secNum force``, ``section $secNum deformation``, and ``section $secNum fiber $y $z stressStrain``.

   5. | The function returns a value:
      | SUCCESS: **>0** an integer tag that can be used as a handle to remove a recorder with the :ref:`remove` command.
      | FAILURE: **-1** recorder command failed (read the log)

.. admonition:: Example

   1. **Tcl Code**

   .. code-block:: tcl

      recorder EnvelopeElement -file ele1global.out -time -ele 1 globalForce
      recorder EnvelopeElement -file ele1sec1.out -time -ele 1 section 1 force

   2. **Python Code**

   .. code-block:: python

      recorder('EnvelopeElement', '-file', 'ele1global.out', '-time', '-ele', 1, 'globalForce')
      recorder('EnvelopeElement', '-file', 'ele1sec1.out', '-time', '-ele', 1, 'section', 1, 'force')

Code developed by: |fmk|
