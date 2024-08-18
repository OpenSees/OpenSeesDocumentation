from openseespy import opensees as ops

ops.model('basic', '-ndm', 3, '-ndf', 3)
ops.node(1, 0,0,0)
ops.node(2, 1,0,0)
ops.node(3, 0,1,0)
ops.node(4, 0,0,1)
ops.nDMaterial('ElasticIsotropic', 100, 1000.0, 0.0)
ops.nDMaterial('InitStrain', 300,  100, 0.0,0.0,0.1,0.0,0.0,0.0)
ops.element('FourNodeTetrahedron', 1,  1,2,3,4,  300)
ops.fixZ(0.0,  1,1,1)
ops.timeSeries('Constant', 1)
ops.pattern('Plain', 1, 1)
ops.constraints('Transformation')
ops.numberer('RCM')
ops.system('FullGeneral')
ops.test('NormDispIncr', 1.0e-5, 100, 0)
ops.algorithm('Newton')
ops.integrator('LoadControl', 1.0)
ops.analysis('Static')
ops.analyze(1)
# should be equal to -0.1, i.e. the opposite of the imposed strain in the Z direction since the tetrahedron has h=1
UZ = ops.nodeDisp(4)[2]
print(UZ)