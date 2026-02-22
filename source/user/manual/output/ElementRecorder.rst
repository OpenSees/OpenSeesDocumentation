.. _elementRecorder:

Element Recorder
^^^^^^^^^^^^^^^^

The element recorder is used to record element-level response during an analysis. Output may go to a file, XML, or other targets depending on the arguments. Common responses include ``force``, ``deformation``, and (for elements with sections) section and fiber response.

.. function:: recorder Element <-file $fileName> <-xml $fileName> ... <-time> <-ele $ele1 $ele2 ...> $responseArgs

The exact arguments depend on the element type and what you want to record. The following sections describe how to record **fiber** and **section** response for fiber-section and beam-column elements.

Recording fiber response
""""""""""""""""""""""""

For elements that use fiber sections (e.g. **zeroLengthSection**, **forceBeamColumn**, **dispBeamColumn**, **mixedBeamColumn**), you can record the response of a single fiber. What can be recorded in each fiber is defined by the UniaxialMaterial's ``setResponse()`` method. A common option is ``stressStrain``, which gives the fiber stress-strain history. Other options (e.g. ``stress``, ``strain``, ``tangent``, ``damage`` for the Fatigue material) are available when supported by the material.

You specify *which* fiber to record using one of three options:

1. **Fiber index** – The index in the section's internal array of fibers (0 to *N*\ :sub:`f` − 1). Use ``fiber`` followed by the index and the response type.

2. **Fiber closest to section coordinates** – Give the section *y* and *z* coordinates; the recorder uses the fiber closest to that point. Use ``fiber`` followed by *y*, *z*, and the response type. For 2D problems, bending is about the *z*-axis so only *y* matters, but you must still provide a *z* value (e.g. 0).

3. **Fiber with a given material tag closest to coordinates** – Same as (2), but only among fibers with the specified material tag. Use ``fiber`` followed by *y*, *z*, *matTag*, and the response type. This is useful for sections with overlapping fibers (e.g. steel and concrete) when you want a specific material at a location.

What comes *before* ``fiber`` depends on the element:

- **zeroLengthSection** – Use ``section`` then ``fiber`` (there is only one section).

- **Beam-column elements** (displacement-based, force-based, mixed) – Use ``section`` *secNum* then ``fiber``, where *secNum* is the integration point number (1 to *N*\ :sub:`p` from node *I* to node *J*). Alternatively, use ``sectionX`` *x* then ``fiber`` to select the section closest to coordinate *x* along the element (see :ref:`elementRecorderSectionX`).

1. **Tcl Code**

.. code-block:: tcl

   # zeroLengthSection: fiber closest to (y,z), stress-strain
   recorder Element -ele 1 -file fiber.out section fiber 0.1 0.0 stressStrain

   # Beam-column: section 1, fiber at (y,z) with material tag 2 (e.g. steel)
   recorder Element -ele 1 -file steelFiber.out section 1 fiber -h/2 0 2 stressStrain

2. **Python Code**

.. code-block:: python

   # zeroLengthSection: fiber closest to (y,z)
   ops.recorder('Element', '-ele', 1, '-file', 'fiber.out', 'section', 'fiber', 0.1, 0.0, 'stressStrain')

   # Beam-column: section 1, steel fiber at tension face
   ops.recorder('Element', '-ele', 1, '-file', 'steelFiber.out', 'section', 1, 'fiber', -h/2, 0, 2, 'stressStrain')

.. _elementRecorderSectionX:

Recording section response by location (sectionX)
"""""""""""""""""""""""""""""""""""""""""""""""""

For beam-column elements you can record section response (e.g. ``force``, ``deformation``) by **section number** (1 to *N*\ :sub:`p`). The mapping from section number to position depends on the integration rule (e.g. Lobatto, Legendre, or plastic-hinge schemes), so it is not always obvious which number corresponds to a given location along the element.

You can avoid relying on section numbers by using **sectionX**: give a location *x* in the range [0, *L*] along the element (0 at node *I*, *L* at node *J*). The recorder will use the section **closest** to that *x* coordinate. The remaining arguments after ``sectionX`` *x* are the same as for the usual ``section`` *secNum* recorder (e.g. ``deformation``, ``force``, or ``fiber`` ...).

1. **Tcl Code**

.. code-block:: tcl

   # Section closest to x = 25 along the element
   recorder Element -ele 1 -file sec25.out sectionX 25 deformation

2. **Python Code**

.. code-block:: python

   ops.recorder('Element', '-ele', 1, '-file', 'sec25.out', 'sectionX', 25, 'deformation')

.. note::

   ``sectionX`` accepts a **single** *x* value per recorder. To record at multiple locations, define multiple recorders.

.. seealso::

   For recording **fatigue damage** in fiber sections or truss elements, see the damage recorder notes in :ref:`Fatigue`. For a detailed walkthrough of fiber recorders and moment-curvature analysis, see `How to Record Fiber Response (Portwood Digital) <https://portwooddigital.com/2021/07/25/how-to-record-fiber-response/>`_ and `Section X (Portwood Digital) <https://portwooddigital.com/2021/11/07/section-x/>`_.
