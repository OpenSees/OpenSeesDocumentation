import math

def _bezier3(xi,   x0, x1, x2,   y0, y1, y2):
	'''
	a quadratic bezier curve. gives the yi at xi, from 3 control points
	'''
	A = x0 - 2.0 * x1 + x2
	B = 2.0 * (x1 - x0)
	C = x0 - xi
	if abs(A) < 1.0e-12:
		x1 = x1 + 1.0E-6 * (x2 - x0)
		A = x0 - 2.0 * x1 + x2
		B = 2.0 * (x1 - x0)
		C = x0 - xi
	if A == 0.0:
		return 0.0
	D = B * B - 4.0 * A * C
	t = (math.sqrt(D) - B) / (2.0 * A)
	return (y0 - 2.0 * y1 + y2) * t * t + 2.0 * (y1 - y0) * t + y0

def _get_lch_ref(E,ft,Gt,fc,ec,Gc):
	'''
	automatically computes a dummy reference characteristic length
	when Gt and Gc are computed from equations
	'''
	
	# min lch for tension
	et_el = ft/E # no damage at peak
	Gt_min = ft*et_el/2.0
	hmin_t = Gt/Gt_min/100.0
	
	# min lch for compression
	ec1 = fc/E
	ec_pl = (ec-ec1)*0.4 + ec1
	Gc_min = fc*(ec-ec_pl)/2.0
	hmin_c = Gc/Gc_min/100.0
	
	# return the minimum
	return min(hmin_t, hmin_c)

def _make_tension(E, ft, Gt):
	'''
	a trilinar hardening-softening law for tensile response
	'''
	f0 = ft*0.9
	f1 = ft
	e0 = f0/E
	e1 = f1/E*1.5
	ep = e1-f1/E
	f2 = ft/5.0
	f3 = 1.0e-3*ft
	w2 = Gt/ft
	w3 = 5.0*w2
	e2 = w2 + f2/E + ep
	if e2 <= e1: e2 = e1*1.001
	e3 = w3 + f3/E + ep
	if e3 <= e2: e3 = e2*1.001
	e4 = e3*10.0
	Te = [0.0,  e0,  e1,  e2,  e3,  e4] # total strain points
	Ts = [0.0,  f0,  f1,  f2,  f3,  f3] # nominal stress points
	Td = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0] # initialize damage list
	Tpl = [0.0, 0.0, ep, e2*0.9, e3*0.8, e3*0.8] # desired values of equivalent plastic strains
	for i in range(2, len(Te)):
		xi = Te[i]
		si = Ts[i]
		xipl = Tpl[i]
		xipl_max = xi-si/E
		xipl = min(xipl, xipl_max)
		qi = (xi-xipl)*E
		Td[i] = 1.0-si/qi # compute damage
	return (Te, Ts, Td)

def _make_compression(E, fc, ec, Gc):
	'''
	a quadratic hardening followed by linear softening for compressive response
	'''
	fc0 = fc/2.0
	ec0 = fc0/E
	ec1 = fc/E
	fcr = fc*1.0e-1
	ec_pl = (ec-ec1)*0.4 + ec1
	Gc1 = fc*(ec-ec_pl)/2.0
	Gc2 = max(Gc1*1.0e-2, Gc-Gc1)
	ecr = ec + 2.0*Gc2/(fc+fcr)
	Ce = [0.0, ec0] # total strain points
	Cs = [0.0, fc0] # nominal stress points
	Cpl = [0.0, 0.0] # desired values of equivalent plastic strains
	nc = 10
	dec = (ec-ec0)/(nc-1)
	for i in range(nc-1):
		iec = ec0+(i+1.0)*dec
		Ce.append(iec)
		Cs.append(_bezier3(iec,  ec0, ec1, ec,  fc0, fc, fc))
		Cpl.append(Cpl[-1]+(iec-Cpl[-1])*0.7)
	# end of linear softening - begin residual plateau
	Ce.append(ecr)
	Cs.append(fcr)
	Cpl.append(Cpl[-1] + (ecr-Cpl[-1])*0.7)
	# extend to make a plateau
	Ce.append(ecr+ec0)
	Cs.append(fcr)
	Cpl.append(Cpl[-1])
	# compute damage now
	Cd = [0.0]*len(Ce)
	for i in range(2, len(Ce)):
		xi = Ce[i]
		si = Cs[i]
		xipl = Cpl[i]
		xipl_max = xi-si/E
		xipl = min(xipl, xipl_max)
		qi = (xi-xipl)*E
		Cd[i] = 1.0-si/qi # compute damage
	# Done
	return (Ce, Cs, Cd)

def make(E, ft, fc, ec, Gt, Gc):
	lch_ref = _get_lch_ref(E, ft, Gt, fc, ec, Gc)
	Te, Ts, Td = _make_tension(E, ft, Gt/lch_ref)
	Ce, Cs, Cd = _make_compression(E, fc, ec, Gc/lch_ref)
	return (Te, Ts, Td, Ce, Cs, Cd, lch_ref)