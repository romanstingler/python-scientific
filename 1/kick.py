g = 9.81 #ms-1
rho = 1.2 #kgm-3
a = 0.11 #m
m = 0.43 #kg
Cd = 0.2 
V = 12/3.6 #ms-1
A = pi*a**2
Fg = m*g
Fd = 1./2*Cd*rho*A*V**2
print ('Gravity force {}, drag force {}, ratio {}'.format(Fg,Fd,Fg/Fd))
