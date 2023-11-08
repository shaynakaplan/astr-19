import numpy as np 

x = 1.0	#define a float
y = 2.0	#define another float

#trigonometry
print(f'np.sin({x}) = {np.sin(x)}')		#sin(x)
print(f'np.cos({x}) = {np.cos(x)}')		#cos(x)
print(f'np.tan({x}) = {np.tan(x)}')		#tan(x)
print(f'np.arcsin({x}) = {np.arcsin(x)}')		#arcsin(x)
print(f'np.arccos({x}) = {np.arccos(x)}')		#arccos(x)
print(f'np.arctan({x}) = {np.arctan(x)}')		#arctan(x)
print(f'np.actan2({x}, {y}) = {np.arctan2(x, y)}')	#arctan(x/y)
print(f'np.rad2deg({x}) = {np.rad2deg(x)}')	#convert rad to deg

#hyperbolic functions
print(f'np.sinh({x}) = {np.sinh(x)}')		#sinh(x)
print(f'np.cosh({x}) = {np.cosh(x)}')		#cosh(x)
print(f'np.tanh({x}) = {np.tanh(x)}')		#tanh(x)
print(f'np.arcsinh({x}) = {np.arcsinh(x)}')		#arcsinh(x)
print(f'np.arccosh({x}) = {np.arccosh(x)}')		#arccosh(x)
print(f'np.arctanh({x}) = {np.arctanh(x)}')		#arctanh(x)

#exponents and logarithms
print(f'np.exp({x}) = {np.exp(x)}')	#exp(x)
print(f'np.log({x}) = {np.log(x)}')	#log(x)
print(f'np.log10({x}) = {np.log10(x)}')	#log10(x)
print(f'np.log2({x}) = {np.log2(x)}')	#log2(x)

#min/max/misc functions
x = -1.0
print(f'np.fabs({x}) = {np.fabs(x)}')	#absolute val as float
print(f'np.fmin({x}, {y}) = {np.fmin(x, y)}')	#min of x and y
print(f'np.fmax({x}, {y}) = {np.fmax(x, y)}')	#max of x and y

#populate arrays
n = 100								#define an integer
z = np.arange(n, dtype = float)		#get an array [0.0, n-1]
z *= 2.0 * np.pi / float(n - 1)		#x = [0,2.*pi]
sin_z = np.sin(z)					#get the array sin(z)

#interpolation
#interpolate
print(f'Our interpolated value of sin(0.75) = {np.interp(0.75, z, sin_z)}')
print(f'Actual value of sin(0.75) = {np.sin(0.75)}')