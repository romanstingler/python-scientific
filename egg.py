from math import log,e
M = 67.0 #g
rho = 1.038 #gcm-3
c = 3.7 #Jg-1K-1
K = 5.4*10**-3 # Wcm-1K-1
Tw = 100.0 #C
Ty = 70.0 #C
To = 4.0 #C
#To = 20 #C
t = ((M**(2./3)*c*rho**(1./3))/(K*pi**2*((4.*pi)/3)**(2./3)))*log(0.76*((To-Tw)/(Ty-Tw)))
print t
