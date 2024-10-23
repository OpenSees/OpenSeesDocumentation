.. _ElasticFrame:

ElasticFrame
^^^^^^^^^^^^^^^^

The **ElasticFrame** section implements a general linear elastic frame section.

.. tabs::

   .. tab:: Tcl

      .. function:: section ElasticFrame $tag $E $A $Iz $Iy $G $J

      The required arguments are:

      .. csv-table:: 
         :header: "Argument", "Type", "Description"
         :widths: 10, 10, 40

         $tag, |integer|,	       unique element object tag
         $iNode  $jNode, |integer|,  end nodes
         $secTag, |integer|,         section tag
         $transf, |integer|,      identifier for previously-defined coordinate-transformation (CrdTransf)


   .. tab:: Python (RT)

      .. function:: section("ElasticFrame", tag, **kwds)


