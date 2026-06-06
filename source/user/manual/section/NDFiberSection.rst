.. _NDFiberSection:

NDFiberSection
^^^^^^^^^^^^^^

This command constructs a fiber section in which each fiber uses an nD material in a **beam-fiber** stress state. Unlike a standard ``Fiber`` section (Bernoulli theory with uniaxial materials), an ``NDFiber`` section captures **axial-shear** interaction in 2D and **axial-shear-torsion** interaction in 3D. Section geometry is defined with ``patch``, ``layer``, and ``fiber`` subcommands inside a braced block, the same way as for a ``Fiber`` section.

.. function:: section NDFiber $secTag { $subcommands }

.. csv-table::
   :header: "Argument", "Type", "Description"
   :widths: 10, 10, 40

   $secTag, |integer|, unique section tag
   $subcommands, |list|, braced block of ``patch`` ``layer`` and ``fiber`` commands referencing nD materials

.. note::

   1. **Direct beam-fiber materials.** ``J2BeamFiber`` and ``ElasticIsotropicBeamFiber`` are nD materials formulated directly for the beam-fiber stress condition and are the usual choice for steel or other J2 beam fibers.

   2. **Wrapping general nD materials.** A three-dimensional nD material can also be placed in an ``NDFiber`` section. OpenSees obtains a ``BeamFiber2d`` (2D) or ``BeamFiber`` (3D) copy by wrapping the material with ``BeamFiberMaterial2d`` or ``BeamFiberMaterial``, which performs static condensation to the beam-fiber stress state. This approach can be expensive for complicated constitutive models.

   3. Use ``section NDFiberWarping`` instead of ``section NDFiber`` when warping behavior is required in 2D models.

   4. Further discussion and verification examples are available in `Fibers of Higher Dimensions <https://openseesdigital.com/2020/11/18/fibers-of-higher-dimensions/>`_ on OpenSees Digital.

.. admonition:: Example

   The following example defines a 3D ``NDFiber`` section for a hollow steel tube using ``J2BeamFiber`` and a circular ``patch``.

   1. **Tcl Code**

   .. code-block:: tcl

      nDMaterial J2BeamFiber 1 29000.0 0.3 60.0 0.0 145.73
      section NDFiber 1 {
          patch circ 1 8 4 0.0 0.0 2.25 2.50 0.0 360.0
      }

   2. **Python Code**

   .. code-block:: python

      nDMaterial('J2BeamFiber', 1, 29000.0, 0.3, 60.0, 0.0, 145.73)
      section('NDFiber', 1)
      patch('circ', 1, 8, 4, 0.0, 0.0, 2.25, 2.50, 0.0, 360.0)

Code Developed by: |mhs|
