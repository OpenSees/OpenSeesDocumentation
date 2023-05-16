.. _contribute:

*********************************
Contributing Code & Documentation
*********************************

Code Contribution
==================
To submit your code contribution (e.g. Material Model, Element) please submit pull request to the `OpenSees Github Page <https://github.com/OpenSees/OpenSees>`_. Please ensure that there is no merge conflict to the OpenSees Repo. Please include documentation!

Documentation
==============

To contribute documentation, submit a pull request to the `OpenSeesDocumentation GitHub page <https://github.com/OpenSees/OpenSeesDocumentation>`_. OpenSees Documentation use sphinx and reStructured Text format. A dummy example is provided below with .. NOTE: as a comment/simple description. More detailed explanation can be found in `reStructured Text Basic <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_

reStructured Text Quickstart
--------------------------------

.. admonition:: Example 

   .. code-block:: rst

        .. _PageUUID: .. NOTE: This is the GLOBAL Identified for your page. Other page could dynamically link your page by calling :ref:`_PageUUID` 

        DummyMaterial Material    .. NOTE: Page Title
        ^^^^^^^^^^^^^^^^   .. NOTE: This mark the above text (DummyMaterial) as an subsections. "===" is for section, "---" is for subsection, "^^^" is for subsubsection and '""""""' is for paragraph.

        .. function:: integrator GimmeMCK $m $c $k $ki  .. The Function input for your model/element

        .. list-table::     .. NOTE: Preferred Table Setup. If you need more columns, add an integer value to the widths. Note that this will add columns to every row!
            :widths: 10 10 40
            :header-rows: 1

        * - Argument         .. * marks a new row and - fill a column in the row (left-right order)
            - Type
            - Description
        * - $m
            - |float|
            - If the value is not zero, add mass matrix to tangent matrix with factored value as large as the input.
        * - $c
            - |float|
            - If the value is not zero, add damping matrix to tangent matrix  with factored value as large as the input.
        * - $ki
            - |float| 
            - If the value is not zero, add the tangent stiffness matrix to tangent matrix  with factored value as large as the input.
        * - $kt 
            - |float| 
            - If the value is not zero, add the initial stiffness matrix to tangent matrix  with factored value as large as the input.

        .. math:

            \textrm{reStructured Text support Latex Math} \leq \frac{a} {b}

        :math:`\frac{a}{b}` In Line Maths
        .. note::   .
            * This is a note
    
          .. admonition:: Example:


          1. **Tcl Code**

          .. code-block:: tcl

              Code Example for TcL Interpreter

          1. **Python Code**

          .. code-block:: python

              Code Example for Python Interpreter            