NDTest Examples
===============

This document provides comprehensive examples of using the NDTest command for testing nDMaterial objects in OpenSees.

Basic Material Testing Example
===============================

TCL:

.. code-block:: tcl

   # =============================================
   # Example 1: Basic Elastic Material Test
   # =============================================
   
   # Create an elastic isotropic material
   # E = 200 GPa, ν = 0.3
   nDMaterial ElasticIsotropic 1 200000 0.3
   
   puts "=== Elastic Material Test ==="
   puts "Material Properties:"
   puts "  E = 200 GPa"
   puts "  ν = 0.3"
   puts ""
   
   # Test 1: Uniaxial tension
   puts "Test 1: Uniaxial Tension"
   set strain 0.001
   NDTest SetStrain 1 $strain 0.0 0.0 0.0 0.0 0.0
   set stresses [NDTest GetStress 1]
   set stress11 [lindex $stresses 0]
   puts "  Applied strain: $strain"
   puts "  Resulting stress σ₁₁: $stress11 MPa"
   puts "  Expected stress: [expr {200000 * $strain}] MPa"
   puts ""
   
   # Test 2: Get tangent stiffness
   puts "Test 2: Tangent Stiffness"
   set tangent [NDTest GetTangentStiffness 1]
   set C11 [lindex $tangent 0]
   set C12 [lindex $tangent 1]
   puts "  C₁₁: $C11 MPa"
   puts "  C₁₂: $C12 MPa"
   puts "  Expected C₁₁: [expr {200000}] MPa"
   puts "  Expected C₁₂: [expr {200000 * 0.3 / (1 - 0.3)}] MPa"
   puts ""
   
   # Commit the state
   NDTest CommitState 1

Python:

.. code-block:: python

   # =============================================
   # Example 1: Basic Elastic Material Test
   # =============================================
   
   import openseespy.opensees as op
   
   # Create an elastic isotropic material
   # E = 200 GPa, ν = 0.3
   op.nDMaterial("ElasticIsotropic", 1, 200000, 0.3)
   
   print("=== Elastic Material Test ===")
   print("Material Properties:")
   print("  E = 200 GPa")
   print("  ν = 0.3")
   print("")
   
   # Test 1: Uniaxial tension
   print("Test 1: Uniaxial Tension")
   strain = 0.001
   op.NDTest("SetStrain", 1, strain, 0.0, 0.0, 0.0, 0.0, 0.0)
   stresses = op.NDTest("GetStress", 1)
   stress11 = stresses[0]
   print(f"  Applied strain: {strain}")
   print(f"  Resulting stress σ₁₁: {stress11} MPa")
   print(f"  Expected stress: {200000 * strain} MPa")
   print("")
   
   # Test 2: Get tangent stiffness
   print("Test 2: Tangent Stiffness")
   tangent = op.NDTest("GetTangentStiffness", 1)
   C11 = tangent[0]
   C12 = tangent[1]
   print(f"  C₁₁: {C11} MPa")
   print(f"  C₁₂: {C12} MPa")
   print(f"  Expected C₁₁: {200000} MPa")
   print(f"  Expected C₁₂: {200000 * 0.3 / (1 - 0.3)} MPa")
   print("")
   
   # Commit the state
   op.NDTest("CommitState", 1)

Plasticity Material Testing
============================

TCL:

.. code-block:: tcl

   # =============================================
   # Example 2: J2 Plasticity Material Test
   # =============================================
   
   # Create J2 plasticity material
   # E = 200 GPa, ν = 0.3, yield stress = 300 MPa
   nDMaterial J2Plasticity 2 200000 0.3 0.001 300 20.0 0.0
   
   puts "=== J2 Plasticity Test ==="
   puts "Material Properties:"
   puts "  E = 200 GPa, ν = 0.3"
   puts "  Yield stress = 300 MPa"
   puts "  Isotropic hardening = 20.0 MPa"
   puts ""
   
   # Monotonic loading beyond yield
   puts "Monotonic Loading Test:"
   set maxStrain 0.005
   set numSteps 50
   set file [open "j2_test_output.txt" w]
   puts $file "strain stress11"
   
   for {set i 0} {$i <= $numSteps} {incr i} {
       set strain [expr {$maxStrain * $i / $numSteps}]
       NDTest SetStrain 2 $strain 0.0 0.0 0.0 0.0 0.0
       set stresses [NDTest GetStress 2]
       set stress11 [lindex $stresses 0]
       puts $file "$strain $stress11"
       
       if {$i % 10 == 0} {
           puts "  Step $i: ε = $strain, σ₁₁ = $stress11 MPa"
       }
   }
   
   close $file
   puts "Results saved to j2_test_output.txt"
   puts ""
   
   # Cyclic loading test
   puts "Cyclic Loading Test:"
   set cycles 3
   set amplitude 0.003
   
   for {set cycle 1} {$cycle <= $cycles} {incr cycle} {
       puts "  Cycle $cycle:"
       
       # Loading
       for {set i 0} {$i <= 20} {incr i} {
           set strain [expr {$amplitude * $i / 20}]
           NDTest SetStrain 2 $strain 0.0 0.0 0.0 0.0 0.0
           NDTest CommitState 2
       }
       
       # Unloading
       for {set i 20} {$i >= 0} {incr i -1} {
           set strain [expr {$amplitude * $i / 20}]
           NDTest SetStrain 2 $strain 0.0 0.0 0.0 0.0 0.0
           NDTest CommitState 2
       }
       
       set stresses [NDTest GetStress 2]
       puts "    Final stress: [lindex $stresses 0] MPa"
   }

Python:

.. code-block:: python

   # =============================================
   # Example 2: J2 Plasticity Material Test
   # =============================================
   
   import openseespy.opensees as op
   
   # Create J2 plasticity material
   # E = 200 GPa, ν = 0.3, yield stress = 300 MPa
   op.nDMaterial("J2Plasticity", 2, 200000, 0.3, 0.001, 300, 20.0, 0.0)
   
   print("=== J2 Plasticity Test ===")
   print("Material Properties:")
   print("  E = 200 GPa, ν = 0.3")
   print("  Yield stress = 300 MPa")
   print("  Isotropic hardening = 20.0 MPa")
   print("")
   
   # Monotonic loading beyond yield
   print("Monotonic Loading Test:")
   max_strain = 0.005
   num_steps = 50
   
   with open("j2_test_output.txt", "w") as f:
       f.write("strain stress11\n")
       
       for i in range(num_steps + 1):
           strain = max_strain * i / num_steps
           op.NDTest("SetStrain", 2, strain, 0.0, 0.0, 0.0, 0.0, 0.0)
           stresses = op.NDTest("GetStress", 2)
           stress11 = stresses[0]
           f.write(f"{strain} {stress11}\n")
           
           if i % 10 == 0:
               print(f"  Step {i}: ε = {strain}, σ₁₁ = {stress11} MPa")
   
   print("Results saved to j2_test_output.txt")
   print("")
   
   # Cyclic loading test
   print("Cyclic Loading Test:")
   cycles = 3
   amplitude = 0.003
   
   for cycle in range(1, cycles + 1):
       print(f"  Cycle {cycle}:")
       
       # Loading
       for i in range(21):
           strain = amplitude * i / 20
           op.NDTest("SetStrain", 2, strain, 0.0, 0.0, 0.0, 0.0, 0.0)
           op.NDTest("CommitState", 2)
       
       # Unloading
       for i in range(20, -1, -1):
           strain = amplitude * i / 20
           op.NDTest("SetStrain", 2, strain, 0.0, 0.0, 0.0, 0.0, 0.0)
           op.NDTest("CommitState", 2)
       
       stresses = op.NDTest("GetStress", 2)
       print(f"    Final stress: {stresses[0]} MPa")

Advanced Parameter Study
=========================

TCL:

.. code-block:: tcl

   # =============================================
   # Example 3: Parameter Study with NDTest
   # =============================================
   
   # Base material properties
   set E_base 30000
   set nu_values {0.15 0.20 0.25 0.30 0.35 0.40}
   set test_strain 0.001
   
   puts "=== Poisson's Ratio Effect Study ==="
   puts "Applied strain: $test_strain"
   puts ""
   
   # Results file
   set file [open "poisson_study.txt" w]
   puts $file "poisson_ratio lateral_strain axial_stress"
   
   foreach nu $nu_values {
       # Create material with specific Poisson's ratio
       nDMaterial ElasticIsotropic 10 $E_base $nu
       
       # Apply uniaxial strain
       NDTest SetStrain 10 $test_strain 0.0 0.0 0.0 0.0 0.0
       
       # Get results
       set strains [NDTest GetStrain 10]
       set stresses [NDTest GetStress 10]
       
       set lateral_strain [lindex $strains 1]
       set axial_stress [lindex $stresses 0]
       
       puts $file "$nu $lateral_strain $axial_stress"
       
       puts "ν = $nu:"
       puts "  Lateral strain ε₂₂: $lateral_strain"
       puts "  Expected: [expr {-$nu * $test_strain}]"
       puts "  Axial stress σ₁₁: $axial_stress MPa"
       puts ""
       
       NDTest CommitState 10
   }
   
   close $file
   puts "Parameter study results saved to poisson_study.txt"

Python:

.. code-block:: python

   # =============================================
   # Example 3: Parameter Study with NDTest
   # =============================================
   
   import openseespy.opensees as op
   
   # Base material properties
   E_base = 30000
   nu_values = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
   test_strain = 0.001
   
   print("=== Poisson's Ratio Effect Study ===")
   print(f"Applied strain: {test_strain}")
   print("")
   
   # Results file
   with open("poisson_study.txt", "w") as f:
       f.write("poisson_ratio lateral_strain axial_stress\n")
       
       for nu in nu_values:
           # Create material with specific Poisson's ratio
           op.nDMaterial("ElasticIsotropic", 10, E_base, nu)
           
           # Apply uniaxial strain
           op.NDTest("SetStrain", 10, test_strain, 0.0, 0.0, 0.0, 0.0, 0.0)
           
           # Get results
           strains = op.NDTest("GetStrain", 10)
           stresses = op.NDTest("GetStress", 10)
           
           lateral_strain = strains[1]
           axial_stress = stresses[0]
           
           f.write(f"{nu} {lateral_strain} {axial_stress}\n")
           
           print(f"ν = {nu}:")
           print(f"  Lateral strain ε₂₂: {lateral_strain}")
           print(f"  Expected: {-nu * test_strain}")
           print(f"  Axial stress σ₁₁: {axial_stress} MPa")
           print("")
           
           op.NDTest("CommitState", 10)
   
   print("Parameter study results saved to poisson_study.txt")

Shear Testing Example
=====================

.. code-block:: tcl

   # =============================================
   # Example 4: Pure Shear Test
   # =============================================
   
   # Create material
   nDMaterial ElasticIsotropic 4 70000 0.2
   
   puts "=== Pure Shear Test ==="
   puts "Material: Concrete-like (E = 70 GPa, ν = 0.2)"
   puts ""
   
   # Apply pure shear strain γ₁₂
   set shear_strain 0.002
   NDTest SetStrain 4 0.0 0.0 0.0 $shear_strain 0.0 0.0
   
   # Get results
   set strains [NDTest GetStrain 4]
   set stresses [NDTest GetStress 4]
   
   set shear_stress [lindex $stresses 3]
   set shear_modulus [expr {$shear_stress / $shear_strain}]
   
   puts "Applied shear strain γ₁₂: $shear_strain"
   puts "Resulting shear stress τ₁₂: $shear_stress MPa"
   puts "Calculated shear modulus G: $shear_modulus MPa"
   puts "Expected shear modulus: [expr {70000 / (2 * (1 + 0.2))}] MPa"
   puts ""
   
   # Test with multiple shear components
   puts "Multiple Shear Components Test:"
   NDTest SetStrain 4 0.0 0.0 0.0 0.001 0.0015 0.0008
   set stresses [NDTest GetStress 4]
   puts "  τ₁₂ = [lindex $stresses 3] MPa"
   puts "  τ₂₃ = [lindex $stresses 4] MPa"  
   puts "  τ₃₁ = [lindex $stresses 5] MPa"
   
   NDTest CommitState 4

Custom Response Testing
========================

.. code-block:: tcl

   # =============================================
   # Example 5: Custom Material Responses
   # =============================================
   
   # Create a material with custom responses
   nDMaterial J2Plasticity 5 200000 0.3 0.001 300 20.0 0.0
   
   puts "=== Custom Response Testing ==="
   
   # Apply plastic deformation
   NDTest SetStrain 5 0.002 0.0 0.0 0.0 0.0 0.0
   NDTest CommitState 5
   
   # Get custom responses
   puts "Available custom responses:"
   
   # Try to get plastic strain (if supported)
   if {[catch {set plasticStrain [NDTest GetResponse 5 "plasticStrain"]}]} {
       puts "  plasticStrain response not available"
   } else {
       puts "  Plastic strain: $plasticStrain"
   }
   
   # Try to get backstress (if supported)  
   if {[catch {set backstress [NDTest GetResponse 5 "backstress"]}]} {
       puts "  backstress response not available"
   } else {
       puts "  Backstress: $backstress"
   }
   
   # Try to get yield function value
   if {[catch {set yieldFunc [NDTest GetResponse 5 "yieldFunction"]}]} {
       puts "  yieldFunction response not available"
   } else {
       puts "  Yield function value: $yieldFunc"
   }
   
   puts ""
   puts "Basic responses always available:"
   set stress [NDTest GetResponse 5 "stress"]
   set strain [NDTest GetResponse 5 "strain"] 
   puts "  Stress: $stress"
   puts "  Strain: $strain"

Runtime Parameter Updates
==========================

.. code-block:: tcl

   # =============================================
   # Example 6: Runtime Parameter Updates
   # =============================================
   
   # Create material
   nDMaterial ElasticIsotropic 6 200000 0.3
   
   puts "=== Runtime Parameter Update Test ==="
   
   # Initial test
   NDTest SetStrain 6 0.001 0.0 0.0 0.0 0.0 0.0
   set initial_stress [lindex [NDTest GetStress 6] 0]
   puts "Initial stress: $initial_stress MPa"
   
   # Update Young's modulus (assuming parameter ID 1 for E)
   # Note: Parameter IDs are material-specific - check material documentation
   set new_E 150000
   puts "Updating Young's modulus to: $new_E MPa"
   
   if {[catch {NDTest UpdateDoubleParameter 6 1 $new_E}]} {
       puts "Failed to update parameter (ID may be incorrect for this material)"
   } else {
       # Test with updated parameter
       NDTest SetStrain 6 0.001 0.0 0.0 0.0 0.0 0.0
       set updated_stress [lindex [NDTest GetStress 6] 0]
       puts "Updated stress: $updated_stress MPa"
       puts "Expected stress: [expr {$new_E * 0.001}] MPa"
   }
   
   # Update integer parameter example (if applicable)
   puts "Attempting to update integer parameter..."
   if {[catch {NDTest UpdateIntegerParameter 6 1 0}]} {
       puts "Integer parameter update failed (not supported or incorrect ID)"
   } else {
       puts "Integer parameter updated successfully"
   }
   
   NDTest CommitState 6

Automated Testing Procedure
===========================

.. code-block:: tcl

   # =============================================
   # Example 7: Automated Material Testing Procedure
   # =============================================
   
   proc testMaterial {matTag testName testProcs} {
       puts "=== $testName ==="
       
       foreach procName $testProcs {
           puts "Running $procName..."
           if {[catch {$procName $matTag} result]} {
               puts "  ERROR: $result"
           } else {
               puts "  PASSED"
           }
       }
       puts ""
   }
   
   proc testElasticResponse {matTag} {
       # Test linear elastic response
       set testStrain 0.001
       NDTest SetStrain $matTag $testStrain 0.0 0.0 0.0 0.0 0.0
       set stresses [NDTest GetStress $matTag]
       set stress11 [lindex $stresses 0]
       
       # Get tangent stiffness
       set tangent [NDTest GetTangentStiffness $matTag]
       set C11 [lindex $tangent 0]
       
       # Basic sanity checks
       if {$C11 <= 0} {
           return "Invalid tangent stiffness: $C11"
       }
       
       if {abs($stress11) < 1e-10} {
           return "No stress response to applied strain"
       }
       
       return "OK"
   }
   
   proc testSymmetry {matTag} {
       # Test material symmetry for elastic materials
       # Apply strain in direction 1, check response in direction 2
       NDTest SetStrain $matTag 0.001 0.0 0.0 0.0 0.0 0.0
       set stresses1 [NDTest GetStress $matTag]
       set stress22_1 [lindex $stresses1 1]
       
       # Apply strain in direction 2, check response in direction 1  
       NDTest SetStrain $matTag 0.0 0.001 0.0 0.0 0.0 0.0
       set stresses2 [NDTest GetStress $matTag]
       set stress11_2 [lindex $stresses2 0]
       
       # For isotropic materials, these should be equal
       set tolerance 1e-6
       if {abs($stress22_1 - $stress11_2) > $tolerance} {
           return "Material symmetry violated: $stress22_1 != $stress11_2"
       }
       
       return "OK"
   }
   
   proc testEnergyConservation {matTag} {
       # Simple energy conservation test
       # Apply strain, get work done, remove strain, check work recovery
       
       # Loading
       NDTest SetStrain $matTag 0.001 0.0 0.0 0.0 0.0 0.0
       set stresses [NDTest GetStress $matTag]
       set stress11 [lindex $stresses 0]
       
       # Unloading  
       NDTest SetStrain $matTag 0.0 0.0 0.0 0.0 0.0 0.0
       set stresses_unload [NDTest GetStress $matTag]
       set stress11_unload [lindex $stresses_unload 0]
       
       # For elastic materials, stress should return to zero
       if {abs($stress11_unload) > 1e-10} {
           return "Elastic material not returning to zero stress: $stress11_unload"
       }
       
       return "OK"
   }
   
   # Run automated tests
   nDMaterial ElasticIsotropic 7 200000 0.3
   set testProcs [list testElasticResponse testSymmetry testEnergyConservation]
   testMaterial 7 "Elastic Material Validation" $testProcs

Integration with Analysis Workflow
===================================

.. code-block:: tcl

   # =============================================
   # Example 8: Integration with Structural Analysis
   # =============================================
   
   # This example shows how to use NDTest for material calibration
   # before running a full structural analysis
   
   proc calibrateMaterial {targetModulus targetPoisson} {
       puts "Material Calibration:"
       puts "Target: E = $targetModulus, ν = $targetPoisson"
       
       # Start with initial guess
       set E_guess [expr {$targetModulus * 0.8}]
       set nu_guess [expr {$targetPoisson * 0.9}]
       
       for {set iteration 1} {$iteration <= 10} {incr iteration} {
           puts "Iteration $iteration: E = $E_guess, ν = $nu_guess"
           
           # Create test material
           nDMaterial ElasticIsotropic 99 $E_guess $nu_guess
           
           # Apply test strain
           NDTest SetStrain 99 0.001 0.0 0.0 0.0 0.0 0.0
           
           # Measure response
           set stresses [NDTest GetStress 99]
           set measured_stress [lindex $stresses 0]
           set measured_modulus [expr {$measured_stress / 0.001}]
           
           # Measure Poisson effect
           set strains [NDTest GetStrain 99]
           set lateral_strain [lindex $strains 1]
           set measured_poisson [expr {-$lateral_strain / 0.001}]
           
           puts "  Measured: E = $measured_modulus, ν = $measured_poisson"
           
           # Update guesses (simple proportional correction)
           set E_guess [expr {$E_guess * $targetModulus / $measured_modulus}]
           set nu_guess [expr {$nu_guess * $targetPoisson / $measured_poisson}]
           
           # Check convergence
           if {abs($measured_modulus - $targetModulus) < 100 && \
               abs($measured_poisson - $targetPoisson) < 0.01} {
               puts "Calibration converged!"
               return [list $E_guess $nu_guess]
           }
       }
       
       puts "Calibration did not fully converge"
       return [list $E_guess $nu_guess]
   }
   
   # Run calibration
   set calibratedProps [calibrateMaterial 30000 0.2]
   set finalE [lindex $calibratedProps 0]
   set finalNu [lindex $calibratedProps 1]
   
   puts "Calibrated material properties:"
   puts "E = $finalE MPa"
   puts "ν = $finalNu"
   
   # Now use calibrated material in structural model
   model BasicBuilder -ndm 3 -ndf 3
   nDMaterial ElasticIsotropic 1 $finalE $finalNu
   
   # ... continue with structural analysis ...

These examples demonstrate the versatility of NDTest commands for material testing, calibration, validation, and research applications.