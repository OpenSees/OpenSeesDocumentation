from openseespy import opensees as ops

ops.model('basic', '-ndm', 3, '-ndf', 3)
ops.node(1, 0,0,0)
ops.node(2, 1,0,0)
ops.node(3, 0,1,0)
ops.node(4, 0,0,1)
E1 = 1000.0
E2 = 2000.0
W1 = 0.5
W2 = 0.5
ops.nDMaterial('ElasticIsotropic', 100, E1, 0.0)
ops.nDMaterial('ElasticIsotropic', 200, E2, 0.0)
ops.nDMaterial('Parallel3D', 300,  100,200, '-weights', W1, W2)
ops.element('FourNodeTetrahedron', 1,  1,2,3,4,  300)
ops.fixZ(0.0,  1,1,1)
ops.timeSeries('Constant', 1)
ops.pattern('Plain', 1, 1)
ops.load(4, 0.0, 0.0, 1.0/6.0) # sigma33=1
ops.constraints('Transformation')
ops.numberer('RCM')
ops.system('FullGeneral')
ops.test('NormDispIncr', 1.0e-5, 100, 0)
ops.algorithm('Newton')
ops.integrator('LoadControl', 1.0)
ops.analysis('Static')
ops.analyze(1)
S0_33 = ops.eleResponse(1, 'material', 1, 'stress')[2] # the stress computed by the parallel material
S0_33_homogenized = ops.eleResponse(1, 'material', 1, 'homogenized', 'stress')[2] # manually homogenized from sub-materials, should, be equal to S0_33
S1_33 = ops.eleResponse(1, 'material', 1,    'material', 1, 'stress')[2] # S33 from the first material
S2_33 = ops.eleResponse(1, 'material', 1,    'material', 2, 'stress')[2] # S33 from the first material
print('   Parallel Sigma33 = {:.3g}'.format(S0_33))
print('Homogenized Sigma33 = {:.3g} (must be equal to the previous)'.format(S0_33_homogenized))
print(' Sub-mat (1)Sigma33 = {:.3g}'.format(S1_33))
print(' Sub-mat (2)Sigma33 = {:.3g}'.format(S2_33))
print('Check:')
print('(1)Sigma33*W1 + (2)Sigma33*W2 = Sigma33')
print('{:.3g}*{:.3g} + {:.3g}*{:.3g} = {:.3g}'.format(S1_33,W1, S2_33,W2, S1_33*W1+S2_33*W2))