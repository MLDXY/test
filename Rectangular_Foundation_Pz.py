import numpy as np
def zjhtheta(e,zbr):
    x=np.array([3,5,10])
    y1=np.array([6,10,20])
    y2=np.array([23,25,30])
    ya=np.interp(e,x,y1)
    yb=np.interp(e,x,y2)
    y=np.interp(zbr,np.array([0.25,0.5]),np.array([ya,yb]))
    return y
pi=np.pi
#改
l=2
b=5
pk=2
pc=1
z=1
Es1=10
Es2=1.5
#改



theta=zjhtheta(Es1/Es2,z/b)
pz=l*b*(pk-pc)/(b+2*z*np.tan(theta/180*pi))/(l+2*z*np.tan(theta/180*pi))

print('theta=',theta)
print('Pz=',pz)

