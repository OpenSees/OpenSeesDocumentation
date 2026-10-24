import csv
from pathlib import Path

INCREMENTS_PER_LEG = 120
MATERIAL_ARGS = (
    206000.0, 305.0, 0.02, -342.07, 26.58, -74.87, 3.16,
    4.07, 6.38, 3.12, 2.36, 5.82, 1.0, 1.0, 1.0, 1.0, 1.0,
    116.39, 11.81, 1, 4467.68, 38.39,
)

def peaks():
    result = []
    for amplitude in (0.002, 0.005, 0.01, 0.015, 0.02, 0.03, 0.04, 0.05):
        result.extend((amplitude, -amplitude))
    return result + [0.0]

def strain_history():
    yield 0.0
    previous = 0.0
    for peak in peaks():
        for j in range(1, INCREMENTS_PER_LEG + 1):
            yield previous + (peak - previous) * j / INCREMENTS_PER_LEG
        previous = peak

def run(output='CFSTsteel_symmetric.csv'):
    try:
        import opensees as ops
    except ModuleNotFoundError:
        import openseespy.opensees as ops
    ops.wipe()
    try:
        ops.uniaxialMaterial('CFSTsteel', 1, *MATERIAL_ARGS)
        ops.testUniaxialMaterial(1)
        with Path(output).open('w', newline='', encoding='utf-8') as stream:
            writer = csv.writer(stream)
            writer.writerow(['step', 'strain', 'stress_MPa', 'tangent_MPa'])
            for step, strain in enumerate(strain_history()):
                ops.setStrain(strain)
                writer.writerow([step, strain, ops.getStress(), ops.getTangent()])
    finally:
        ops.wipe()
    return Path(output)

if __name__ == '__main__':
    print(run())
