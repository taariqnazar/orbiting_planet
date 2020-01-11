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


#Constants -----------------------------------------------------#
AU = 1            #1.496*10**11 #Astronomical unit
GM = 4*AU**3*(np.pi)**2  #6.67**(-11) #Gravitational Constant
M = 1.99*10**30
mearth = 5.972*10**24


class Planet():
    
    def __init__(self,mass, x, y):
        self.mass = mass
        self.x = x
        self.y = y
        #Always starts at x,y = (*, 0)
        self.vx = 0
        self.vy = (GM/(x**2+y**2)**0.5)**0.5
        

    #Returns distance between this planet and given planet
    def distance(self,planet):
        dx = self.x - planet.x
        dy = self.y - planet.y

        return (dx**2 + dy**2)**0.5

    def setData(self,x,y):
        self.x = x
        self.y = y




#Parameters to Study -------------------------------------------#
Energy = []
t = []


#Plot setup ----------------------------------------------------#
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))

#initailitze celestial bodies
sun, = ax.plot([0], [0], "yo", ms=20)

planet1, = ax.plot([], [], "go", ms = 10)
earth = Planet(5.972*10**24,1,0)

planet2, = ax.plot([], [], "bo", ms = 10)
mars = Planet(6.39*10**23,1.523, 0)

comet, = ax.plot([], [], "ro", ms = 10)
cx = 0
cy = 0
vx = 0
vy = 0

dt = 0.001

def init():
    global planet1, planet2, comet
    comet.set_data([],[])
    planet1.set_data([], [])
    planet2.set_data([], [])
  
    return planet1,planet2,

def integrate():
    global t, earth, mars

    
    r12 = earth.distance(mars)

    x_acc_earth = -(GM*earth.x)/((earth.x**2 + earth.y**2)**(1.5)) + GM*(mars.mass/M)*(1/r12**1.5)*(mars.x - earth.x)
    
    y_acc_earth = -(GM*earth.y)/((earth.x**2 + earth.y**2)**(1.5)) + GM*(mars.mass/M)*(1/r12**1.5)*(mars.y - earth.y)

    x_acc_mars = -(GM*mars.x)/((mars.x**2 + mars.y**2)**(1.5)) - GM*(earth.mass/M)*(1/r12**1.5)*(mars.x - earth.x)
    
    y_acc_mars = -(GM*mars.y)/((mars.x**2 + mars.y**2)**(1.5)) - GM*(earth.mass/M)*(1/r12**1.5)*(mars.y - earth.y)
    

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
    earth.vx += x_acc_earth*dt
    earth.vy += y_acc_earth*dt

    earth.x += earth.vx*dt
    earth.y += earth.vy*dt

    mars.vx += x_acc_mars*dt
    mars.vy += y_acc_mars*dt

    mars.x += mars.vx*dt
    mars.y += mars.vy*dt

    
    #Energy.append(0.5*mearth*(vx**2 + vy**2) - (GM*mearth)/((x**2 + y**2)**0.5))
    

def animate(i):
    global earth, mars

    integrate()

    t.append(i*dt)

    #print(earth.x, earth.y)

    planet1.set_data([earth.x], [earth.y])
    planet2.set_data([mars.x], [mars.y]) 
    return planet1, planet2,

ani = animation.FuncAnimation(fig, animate,
                           frames = 60, interval=1, init_func = init )


plt.show()


#plt.plot(t, Energy)
#plt.show()
