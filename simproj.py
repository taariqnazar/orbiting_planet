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

    def mek_energy():
        return 0




#Parameters to Study -------------------------------------------#
Energy = []
t = []


#Plot setup ----------------------------------------------------#
fig = plt.figure()
ax = plt.axes(xlim=(-13, 13), ylim=(-13, 13))

#initailitze celestial bodies
sun, = ax.plot([0], [0], "y.", ms=10)

planet1, = ax.plot([], [], "r.", ms = 5)
mercury = Planet(3.285*10**23,0.387,0)

planet2, = ax.plot([], [], "b.", ms = 5)
venus = Planet(4.867*10**24,0.723,0)

planet3, = ax.plot([], [], "g.", ms = 5)
earth = Planet(5.972*10**24,1,0)

planet4, = ax.plot([], [], "b.", ms = 3)
mars = Planet(6.39*10**23,1.523, 0)

planet5, = ax.plot([], [], "r.", ms = 8)
jupiter = Planet(1.898*10**27,5.202, 0)

planet6, = ax.plot([], [], "g.", ms = 7)
saturn = Planet(5.683**26,9.539, 0)


comet, = ax.plot([], [], "ro", ms = 10)
cx = 0
cy = 0
vx = 0
vy = 0

dt = 0.001

def init():
    global planet1, planet2, planet3, planet4, planet5, planet6
    comet.set_data([],[])
    planet1.set_data([], [])
    planet2.set_data([], [])
    planet3.set_data([], [])
    planet4.set_data([], [])
    planet5.set_data([], [])'
    planet6.set_data([], [])
  
    return planet1,planet2,planet3,planet4,planet5,planet6,

def integrate():
    global t, mercury, venus, earth, mars, jupiter

    r13 = mercury.distance(earth) # distance between mercury and earth
    r12 = mercury.distance(venus) # merc-venus
    r14 = mercury.distance(mars) #distance between mars and jupiter
    r15 = mercury.distance(jupiter)
    r16 = mercury.distaance(saturn) #merc-saturn

    r23 = venus.distance(earth)
    r24 = venus.distance(mars)
    r25 = venus.distance(jupiter)
    r26 = venus.distance(saturn)
    
    r34 = earth.distance(mars) #distance between earth and mars
    r35 = earth.distance(jupiter) #distance between earth and jupiter
    r36 = earth.distance(saturn)
    
    r45 = mars.distance(jupiter) #distance between mars and jupiter
    r46 = mars.distance(saturn)

    r56 = jupiter.distance(saturn)

    #MERCURY FORCE
    x_acc_mercury = -(GM*mercury.x)/((mercury.x**2 + mercury.y**2)**(1.5))
    - GM*(venus.mass/M)*(1/r12**1.5)*( mercury.x - venus.x )
    - GM*(earth.mass/M)*(1/r13**1.5)*( mercury.x - earth.x )
    - GM*(mars.mass/M)*(1/r14**1.5)*( mercury.x - mars.x)
    - GM*(jupiter.mass/M)*(1/r15**1.5)*( mercury.x - jupiter.x)

    y_acc_mercury = -(GM*mercury.y)/((mercury.x**2 + mercury.y**2)**(1.5))
    - GM*(venus.mass/M)*(1/r12**1.5)*( mercury.y - venus.y )
    - GM*(earth.mass/M)*(1/r13**1.5)*( mercury.y - earth.y )
    - GM*(mars.mass/M)*(1/r14**1.5)*( mercury.y - mars.y)
    - GM*(jupiter.mass/M)*(1/r15**1.5)*( mercury.y - jupiter.y)


    #VENUS FORCE
    x_acc_venus = -(GM*venus.x)/((venus.x**2 + venus.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r12**1.5)*( venus.x - mercury.x )
    - GM*(earth.mass/M)*(1/r23**1.5)*( venus.x - earth.x )
    - GM*(mars.mass/M)*(1/r24**1.5)*( venus.x - mars.x)
    - GM*(jupiter.mass/M)*(1/r25**1.5)*( venus.x - jupiter.x)

    y_acc_venus = -(GM*venus.y)/((venus.x**2 + venus.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r12**1.5)*( venus.y - mercury.y )
    - GM*(earth.mass/M)*(1/r23**1.5)*( venus.y - earth.y )
    - GM*(mars.mass/M)*(1/r24**1.5)*( venus.y - mars.y)
    - GM*(jupiter.mass/M)*(1/r25**1.5)*( venus.y - jupiter.y)
    
    #EARTH FORCE
    x_acc_earth = -(GM*earth.x)/((earth.x**2 + earth.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r13**1.5)*( earth.x - mercury.x )
    - GM*(venus.mass/M)*(1/r23**1.5)*( earth.x - venus.x )
    - GM*(mars.mass/M)*(1/r34**1.5)*( earth.x - mars.x )
    - GM*(jupiter.mass/M)*(1/r35**1.5)*( earth.x - jupiter.x)

    y_acc_earth = -(GM*earth.y)/((earth.x**2 + earth.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r13**1.5)*( earth.y - mercury.y )
    - GM*(venus.mass/M)*(1/r23**1.5)*( earth.y - venus.y )
    - GM*(mars.mass/M)*(1/r34**1.5)*( earth.y - mars.y )
    - GM*(jupiter.mass/M)*(1/r35**1.5)*( earth.y - jupiter.y)

    #MARS FORCE
    x_acc_mars = -(GM*mars.x)/((mars.x**2 + mars.y**2)**(1.5))
    - GM*(venus.mass/M)*(1/r24**1.5)*( mars.x - venus.x )
    - GM*(mercury.mass/M)*(1/r14**1.5)*( mars.x - mercury.x )
    - GM*(earth.mass/M)*(1/r34**1.5)*(mars.x - earth.x)
    - GM*(jupiter.mass/M)*(1/r45**1.5)*( mars.x - jupiter.x)

    y_acc_mars = -(GM*mars.y)/((mars.x**2 + mars.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r14**1.5)*( mars.y - mercury.y )
    - GM*(venus.mass/M)*(1/r24**1.5)*( mars.y - venus.y )
    - GM*(earth.mass/M)*(1/r34**1.5)*(mars.y - earth.y)
    - GM*(jupiter.mass/M)*(1/r45**1.5)*( mars.y - jupiter.y)

    #JUPITER FORCE
    x_acc_jupiter = -(GM*jupiter.x)/((jupiter.x**2 + jupiter.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r15**1.5)*( jupiter.x - mercury.x )
    - GM*(venus.mass/M)*(1/r25**1.5)*( jupiter.x - venus.x )
    - GM*(earth.mass/M)*(1/r35**1.5)*(jupiter.x - earth.x)
    - GM*(mars.mass/M)*(1/r45**1.5)*( jupiter.x - jupiter.x)

    y_acc_jupiter = -(GM*jupiter.y)/((jupiter.x**2 + jupiter.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r15**1.5)*( jupiter.y - mercury.y )
    - GM*(venus.mass/M)*(1/r25**1.5)*( jupiter.y - venus.y )
    - GM*(earth.mass/M)*(1/r35**1.5)*(jupiter.y - earth.y)
    - GM*(mars.mass/M)*(1/r45**1.5)*( jupiter.y - mars.y)
    

    #SATURN FORCE
    
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
    mercury.vx += x_acc_mercury*dt
    mercury.vy += y_acc_mercury*dt

    mercury.x += mercury.vx*dt
    mercury.y += mercury.vy*dt

    venus.vx += x_acc_venus*dt
    venus.vy += y_acc_venus*dt

    venus.x += venus.vx*dt
    venus.y += venus.vy*dt

    earth.vx += x_acc_earth*dt
    earth.vy += y_acc_earth*dt

    earth.x += earth.vx*dt
    earth.y += earth.vy*dt

    mars.vx += x_acc_mars*dt
    mars.vy += y_acc_mars*dt

    mars.x += mars.vx*dt
    mars.y += mars.vy*dt

    jupiter.vx += x_acc_jupiter*dt
    jupiter.vy += y_acc_jupiter*dt

    jupiter.x += jupiter.vx*dt
    jupiter.y += jupiter.vy*dt

    
    #Energy.append(0.5*mearth*(vx**2 + vy**2) - (GM*mearth)/((x**2 + y**2)**0.5))
    

def animate(i):
    global mercury, venus, earth, mars, jupiter

    integrate()

    t.append(i*dt)

    #print(earth.x, earth.y)

    planet1.set_data([mercury.x], [mercury.y])
    planet2.set_data([venus.x], [venus.y])
    planet3.set_data([earth.x], [earth.y])
    planet4.set_data([mars.x], [mars.y])
    planet5.set_data([jupiter.x], [jupiter.y])
    
    return planet1, planet2, planet3, planet4, planet5,

ani = animation.FuncAnimation(fig, animate,
                           frames = 60, interval=1, init_func = init )


plt.show()


#plt.plot(t, Energy)
#plt.show()
