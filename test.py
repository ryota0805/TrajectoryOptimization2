import numpy as np
import animation

def kari(p1, p2, p3, rho, v, omega):
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    x3, y3 = p3[0], p3[1]
    
    #角度計算
    theta = np.arctan2((y3-y2)-(y2-y1), (x3-x2)-(x2-x1))
    d = v/(np.tan((np.pi-theta)/2)*omega)
    
    d1 = 1/(np.tan((np.pi-theta)/2)*rho)
    return d

p1 = [0, 0]
p2 = [1, 0]
p3 = [2+np.sqrt(3), 1]
rho = 2
v = 0.5
omega = np.pi/6
d = kari(p1, p2, p3, rho, v, omega)
print(d)