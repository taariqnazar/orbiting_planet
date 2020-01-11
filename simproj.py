import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


#Semi Major axis For planets#
#Mercury 0.387 AU
#Venus   0.723 AU
#Earth   1.000 AU
#Mars    1.523 AU 
#Jupiter 5.202 AU
#Saturn  9.539 AU
#Uranus  19.18 AU
#Neptune 30.06 AU
#Pluto   39.44 AU

class Planet():
    
    def __init__(self,plot, x, y, vx, vy):
        self.plot = plot
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    #Returns distance between this planet and given planet
    def distance(self,planet):
        dx = self.x - planet.x
        dy = self.y - planet.y

        return (dx**2 + dy**2)**0.5


#Constants -----------------------------------------------------#
AU = 1            #1.496*10**11 #Astronomical unit
GM = 4*AU**3*(np.pi)**2  #6.67**(-11) #Gravitational Constant
mearth = 5.972*10**24

#Parameters to Study -------------------------------------------#
Energy = []
t = []


#Plot setup ----------------------------------------------------#
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

#initailitze celestial bodies
sun, = ax.plot([0], [0], "yo", ms=20)


planet1, = ax.plot([], [], "go", ms = 10)
x1 = 1
vx1 = 0
y1 = 0
vy1 = (GM/(x1**2+y1**2))**0.5

planet2, = ax.plot([], [], "bo", ms = 10)
x2 = 1.523
vx2 = 0
y2 = 0
vy2 = (GM/(x2**2+y2**2))**0.5

earth = Planet(planet1, x1,y1,vx1,vy1)
mars = Planet(planet2, x2,y2,vx2,vy2)

dt = 0.001

def integrate():
    global t, x1,y1, vx1, vy1, x2,y2, vx2, vy2
    
    xacc1 = -(GM*x1)/((x1**2 + y1**2)**(1.5))
    yacc1 = -(GM*y1)/((x1**2 + y1**2)**(1.5))

    xacc2 = -(GM*x2)/((x2**2 + y2**2)**(1.5))
    yacc2 = -(GM*y2)/((x2**2 + y2**2)**(1.5))

##    ##VERLET
##    xnew = x + vx*dt + 0.5*xacc*(dt**2)
##    ynew = y + vy*dt + 0.5*yacc*(dt**2)
##
##    xaccnew = -(GM*xnew)/((xnew**2 + ynew**2)**(1.5))
##    yaccnew = -(GM*ynew)/((xnew**2 + ynew**2)**(1.5))
##
##    vx += 0.5*(xaccnew + xacc)*dt
##    vy += 0.5*(yaccnew + yacc)*dt
##
##
##    x = xnew
##    y = ynew
    
    ##EULER CROMER
    vx1 += xacc1*dt
    vy1 += yacc1*dt

    x1 += vx1*dt
    y1 += vy1*dt

    vx2 += xacc2*dt
    vy2 += yacc2*dt

    x2 += vx2*dt
    y2 += vy2*dt

    
    #Energy.append(0.5*mearth*(vx**2 + vy**2) - (GM*mearth)/((x**2 + y**2)**0.5))
    

def init():
    global planet1, planet2
    planet1.set_data([], [])
    planet2.set_data([], [])
  
    return planet1,planet2,

def animate(i):
    global planet1, planet2, x1, y1, x2, y2, t

    integrate()

    t.append(i*dt)

    
    
    planet1.set_data([x1], [y1])
    planet2.set_data([x2], [y2]) 
    return planet1, planet2,

ani = animation.FuncAnimation(fig, animate,
                            frames = 60, interval=1, init_func = init )
plt.show()

print(earth.distance(mars))

#plt.plot(t, Energy)
#plt.show()
