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
AU = 1           #1.496*10**11 #Astronomical unit
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

    def force(self,planets = []):
        x_acc = -(GM*self.x)/((self.x**2 + self.y**2)**(1.5)) 
        y_acc = -(GM*self.y)/((self.x**2 + self.y**2)**(1.5))

        for planet in planets:
            x_acc -= GM*(planet.mass/M)*(1/(self.distance(planet))**1.5)*(self.x - planet.x)
            

            y_acc -= GM*(planet.mass/M)*(1/(self.distance(planet))**1.5)*(self.y - planet.y)
            
        
        return x_acc, y_acc

    def mek_energy():
        return 0




#Parameters to Study -------------------------------------------#
Energy = []
t = []


#Plot setup ----------------------------------------------------#
fig = plt.figure()
ax = plt.axes(xlim=(-35, 35), ylim=(-35, 35))

#initailitze celestial bodies
sun, = ax.plot([0], [0], "y.", ms=10)

planet1, = ax.plot([], [], "r.", ms = 5)
mercury = Planet(3.285*10**23,AU*0.387,0)

planet2, = ax.plot([], [], "b.", ms = 5)
venus = Planet(4.867*10**24,AU*0.723,0)

planet3, = ax.plot([], [], "g.", ms = 5)
earth = Planet(5.972*10**24,AU*1,0)

planet4, = ax.plot([], [], "b.", ms = 3)
mars = Planet(6.39*10**23,AU*1.523, 0)

planet5, = ax.plot([], [], "r.", ms = 8)
jupiter = Planet(1.898*10**27,AU*5.202, 0)

planet6, = ax.plot([], [], "g.", ms = 7)
saturn = Planet(5.683*10**26,AU*9.539, 0)

planet7, = ax.plot([], [], "y.", ms = 5)
uranus = Planet(8.681*10**25,AU*19.18, 0)

planet8, = ax.plot([], [], "b.", ms = 5)
neptune = Planet(1.024*10**26,AU*30.06, 0)


comet, = ax.plot([], [], "ro", ms = 10)
cx = 0
cy = 0
vx = 0
vy = 0

dt = 0.001

def init():
    global planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8
    comet.set_data([],[])
    planet1.set_data([], [])
    planet2.set_data([], [])
    planet3.set_data([], [])
    planet4.set_data([], [])
    planet5.set_data([], [])
    planet6.set_data([], [])
    planet7.set_data([], [])
    planet8.set_data([], [])
    
    return planet1,planet2,planet3,planet4,planet5,planet6,planet7,planet8,

def integrate():
    global t, mercury, venus, earth, mars, jupiter, uranus, neptune

    r13 = mercury.distance(earth) # distance between mercury and earth
    r12 = mercury.distance(venus) # merc-venus
    r14 = mercury.distance(mars) #distance between mars and jupiter
    r15 = mercury.distance(jupiter)
    r16 = mercury.distance(saturn) #merc-saturn
    r17 = mercury.distance(uranus)
    r18 = mercury.distance(neptune)
    
    r23 = venus.distance(earth)
    r24 = venus.distance(mars)
    r25 = venus.distance(jupiter)
    r26 = venus.distance(saturn)
    r27 = venus.distance(uranus)
    r28 = venus.distance(neptune)
    
    r34 = earth.distance(mars) #distance between earth and mars
    r35 = earth.distance(jupiter) #distance between earth and jupiter
    r36 = earth.distance(saturn)
    r37 = earth.distance(uranus)
    r38 = earth.distance(neptune)
    
    r45 = mars.distance(jupiter) #distance between mars and jupiter
    r46 = mars.distance(saturn)
    r47 = mars.distance(uranus)
    r48 = mars.distance(neptune)
    
    r56 = jupiter.distance(saturn)
    r57 = jupiter.distance(uranus)
    r58 = jupiter.distance(neptune)

    r67 = saturn.distance(uranus)
    r68 = saturn.distance(neptune)

    r78 = uranus.distance(neptune)

    #MERCURY FORCE
    x_acc_mercury = -(GM*mercury.x)/((mercury.x**2 + mercury.y**2)**(1.5))
    - GM*(venus.mass/M)*(1/r12**1.5)*( mercury.x - venus.x )
    - GM*(earth.mass/M)*(1/r13**1.5)*( mercury.x - earth.x )
    - GM*(mars.mass/M)*(1/r14**1.5)*( mercury.x - mars.x)
    - GM*(jupiter.mass/M)*(1/r15**1.5)*( mercury.x - jupiter.x)
    - GM*(saturn.mass/M)*(1/r16**1.5)*( mercury.x - saturn.x)
    - GM*(uranus.mass/M)*(1/r17**1.5)*( mercury.x - uranus.x)
    - GM*(neptune.mass/M)*(1/r18**1.5)*( mercury.x - neptune.x)

    y_acc_mercury = -(GM*mercury.y)/((mercury.x**2 + mercury.y**2)**(1.5))
    - GM*(venus.mass/M)*(1/r12**1.5)*( mercury.y - venus.y )
    - GM*(earth.mass/M)*(1/r13**1.5)*( mercury.y - earth.y )
    - GM*(mars.mass/M)*(1/r14**1.5)*( mercury.y - mars.y)
    - GM*(jupiter.mass/M)*(1/r15**1.5)*( mercury.y - jupiter.y)
    - GM*(saturn.mass/M)*(1/r16**1.5)*( mercury.y - saturn.y)
    - GM*(uranus.mass/M)*(1/r17**1.5)*( mercury.y - uranus.y)
    - GM*(neptune.mass/M)*(1/r18**1.5)*( mercury.y - neptune.y)


    #VENUS FORCE
    x_acc_venus = -(GM*venus.x)/((venus.x**2 + venus.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r12**1.5)*( venus.x - mercury.x )
    - GM*(earth.mass/M)*(1/r23**1.5)*( venus.x - earth.x )
    - GM*(mars.mass/M)*(1/r24**1.5)*( venus.x - mars.x)
    - GM*(jupiter.mass/M)*(1/r25**1.5)*( venus.x - jupiter.x)
    - GM*(saturn.mass/M)*(1/r26**1.5)*( venus.x - saturn.x)
    - GM*(uranus.mass/M)*(1/r27**1.5)*( venus.x - uranus.x)
    - GM*(neptune.mass/M)*(1/r28**1.5)*( venus.x - neptune.x)

    y_acc_venus = -(GM*venus.y)/((venus.x**2 + venus.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r12**1.5)*( venus.y - mercury.y )
    - GM*(earth.mass/M)*(1/r23**1.5)*( venus.y - earth.y )
    - GM*(mars.mass/M)*(1/r24**1.5)*( venus.y - mars.y)
    - GM*(jupiter.mass/M)*(1/r25**1.5)*( venus.y - jupiter.y)
    - GM*(saturn.mass/M)*(1/r26**1.5)*( venus.y - saturn.y)
    - GM*(uranus.mass/M)*(1/r27**1.5)*( venus.y - uranus.y)
    - GM*(neptune.mass/M)*(1/r28**1.5)*( venus.y - neptune.y)
    
    #EARTH FORCE
    x_acc_earth = -(GM*earth.x)/((earth.x**2 + earth.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r13**1.5)*( earth.x - mercury.x )
    - GM*(venus.mass/M)*(1/r23**1.5)*( earth.x - venus.x )
    - GM*(mars.mass/M)*(1/r34**1.5)*( earth.x - mars.x )
    - GM*(jupiter.mass/M)*(1/r35**1.5)*( earth.x - jupiter.x)
    - GM*(saturn.mass/M)*(1/r36**1.5)*( earth.x - saturn.x)
    - GM*(uranus.mass/M)*(1/r37**1.5)*( earth.x - uranus.x)
    - GM*(neptune.mass/M)*(1/r38**1.5)*( earth.x - earth.x)

    y_acc_earth = -(GM*earth.y)/((earth.x**2 + earth.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r13**1.5)*( earth.y - mercury.y )
    - GM*(venus.mass/M)*(1/r23**1.5)*( earth.y - venus.y )
    - GM*(mars.mass/M)*(1/r34**1.5)*( earth.y - mars.y )
    - GM*(jupiter.mass/M)*(1/r35**1.5)*( earth.y - jupiter.y)
    - GM*(saturn.mass/M)*(1/r36**1.5)*( earth.y - saturn.y)
    - GM*(uranus.mass/M)*(1/r37**1.5)*( earth.y - uranus.y)
    - GM*(neptune.mass/M)*(1/r38**1.5)*( earth.y - neptune.y)

    #MARS FORCE
    x_acc_mars = -(GM*mars.x)/((mars.x**2 + mars.y**2)**(1.5))
    - GM*(venus.mass/M)*(1/r24**1.5)*( mars.x - venus.x )
    - GM*(mercury.mass/M)*(1/r14**1.5)*( mars.x - mercury.x )
    - GM*(earth.mass/M)*(1/r34**1.5)*(mars.x - earth.x)
    - GM*(jupiter.mass/M)*(1/r45**1.5)*( mars.x - jupiter.x)
    - GM*(saturn.mass/M)*(1/r46**1.5)*( mars.x - saturn.x)
    - GM*(uranus.mass/M)*(1/r47**1.5)*( mars.x - uranus.x)
    - GM*(neptune.mass/M)*(1/r48**1.5)*( mars.x - neptune.x)
    

    y_acc_mars = -(GM*mars.y)/((mars.x**2 + mars.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r14**1.5)*( mars.y - mercury.y )
    - GM*(venus.mass/M)*(1/r24**1.5)*( mars.y - venus.y )
    - GM*(earth.mass/M)*(1/r34**1.5)*(mars.y - earth.y)
    - GM*(jupiter.mass/M)*(1/r45**1.5)*( mars.y - jupiter.y)
    - GM*(saturn.mass/M)*(1/r46**1.5)*( mars.y - saturn.y)
    - GM*(uranus.mass/M)*(1/r47**1.5)*( mars.y - uranus.y)
    - GM*(neptune.mass/M)*(1/r48**1.5)*( mars.y - neptune.y)

    #JUPITER FORCE
    x_acc_jupiter = -(GM*jupiter.x)/((jupiter.x**2 + jupiter.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r15**1.5)*( jupiter.x - mercury.x )
    - GM*(venus.mass/M)*(1/r25**1.5)*( jupiter.x - venus.x )
    - GM*(earth.mass/M)*(1/r35**1.5)*(jupiter.x - earth.x)
    - GM*(mars.mass/M)*(1/r45**1.5)*( jupiter.x - mars.x)
    - GM*(saturn.mass/M)*(1/r56**1.5)*( jupiter.x - saturn.x)
    - GM*(uranus.mass/M)*(1/r57**1.5)*( jupiter.x - uranus.x)
    - GM*(neptune.mass/M)*(1/r58**1.5)*( jupiter.x - neptune.x)

    y_acc_jupiter = -(GM*jupiter.y)/((jupiter.x**2 + jupiter.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r15**1.5)*( jupiter.y - mercury.y )
    - GM*(venus.mass/M)*(1/r25**1.5)*( jupiter.y - venus.y )
    - GM*(earth.mass/M)*(1/r35**1.5)*(jupiter.y - earth.y)
    - GM*(mars.mass/M)*(1/r45**1.5)*( jupiter.y - mars.y)
    - GM*(saturn.mass/M)*(1/r56**1.5)*( jupiter.y - saturn.y)
    - GM*(uranus.mass/M)*(1/r57**1.5)*( jupiter.y - uranus.y)
    - GM*(neptune.mass/M)*(1/r58**1.5)*( jupiter.y - neptune.y)
    
    #SATURN FORCE
    x_acc_saturn = -(GM*saturn.x)/((saturn.x**2 + saturn.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r16**1.5)*( saturn.x - mercury.x )
    - GM*(venus.mass/M)*(1/r26**1.5)*( saturn.x - venus.x )
    - GM*(earth.mass/M)*(1/r36**1.5)*(saturn.x - earth.x)
    - GM*(mars.mass/M)*(1/r46**1.5)*( saturn.x - mars.x)
    - GM*(jupiter.mass/M)*(1/r56**1.5)*( saturn.x - jupiter.x)
    - GM*(uranus.mass/M)*(1/r67**1.5)*( saturn.x - uranus.x)
    - GM*(neptune.mass/M)*(1/r68**1.5)*( saturn.x - neptune.x)
    

    y_acc_saturn = -(GM*saturn.y)/((saturn.x**2 + saturn.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r16**1.5)*( saturn.y - mercury.y )
    - GM*(venus.mass/M)*(1/r26**1.5)*( saturn.y - venus.y )
    - GM*(earth.mass/M)*(1/r36**1.5)*(saturn.y - earth.y)
    - GM*(mars.mass/M)*(1/r46**1.5)*( saturn.y - mars.y)
    - GM*(jupiter.mass/M)*(1/r56**1.5)*( saturn.y - jupiter.y)
    - GM*(uranus.mass/M)*(1/r67**1.5)*( saturn.y - uranus.y)
    - GM*(neptune.mass/M)*(1/r68**1.5)*( saturn.y - neptune.y)

    #URANUS FORCE
    x_acc_uranus = -(GM*uranus.x)/((uranus.x**2 + uranus.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r17**1.5)*( uranus.x - mercury.x )
    - GM*(venus.mass/M)*(1/r27**1.5)*( uranus.x - venus.x )
    - GM*(earth.mass/M)*(1/r37**1.5)*(uranus.x - earth.x)
    - GM*(mars.mass/M)*(1/r47**1.5)*( uranus.x - jupiter.x)
    - GM*(jupiter.mass/M)*(1/r57**1.5)*( uranus.x - jupiter.x)
    - GM*(saturn.mass/M)*(1/r67**1.5)*( uranus.x - saturn.x)
    - GM*(neptune.mass/M)*(1/r78**1.5)*( uranus.x - neptune.x)

    y_acc_uranus = -(GM*uranus.y)/((uranus.x**2 + uranus.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r17**1.5)*( uranus.y - mercury.y )
    - GM*(venus.mass/M)*(1/r27**1.5)*( uranus.y - venus.y )
    - GM*(earth.mass/M)*(1/r37**1.5)*(uranus.y - earth.y)
    - GM*(mars.mass/M)*(1/r47**1.5)*( uranus.y - mars.y)
    - GM*(jupiter.mass/M)*(1/r57**1.5)*( uranus.y - jupiter.y)
    - GM*(saturn.mass/M)*(1/r67**1.5)*( uranus.y - saturn.y)
    - GM*(neptune.mass/M)*(1/r78**1.5)*( uranus.x - neptune.x)

    #NEPTUNE FORCE
    x_acc_neptune = -(GM*neptune.x)/((neptune.x**2 + neptune.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r18**1.5)*( neptune.x - mercury.x )
    - GM*(venus.mass/M)*(1/r28**1.5)*( neptune.x - venus.x )
    - GM*(earth.mass/M)*(1/r38**1.5)*(neptune.x - earth.x)
    - GM*(mars.mass/M)*(1/r48**1.5)*( neptune.x - jupiter.x)
    - GM*(jupiter.mass/M)*(1/r58**1.5)*( neptune.x - jupiter.x)
    - GM*(saturn.mass/M)*(1/r68**1.5)*( neptune.x - saturn.x)
    - GM*(uranus.mass/M)*(1/r78**1.5)*( neptune.x - uranus.x)

    y_acc_neptune = -(GM*neptune.y)/((neptune.x**2 + neptune.y**2)**(1.5))
    - GM*(mercury.mass/M)*(1/r18**1.5)*( neptune.y - mercury.y )
    - GM*(venus.mass/M)*(1/r28**1.5)*( neptune.y - venus.y )
    - GM*(earth.mass/M)*(1/r38**1.5)*(neptune.y - earth.y)
    - GM*(mars.mass/M)*(1/r48**1.5)*( neptune.y - mars.y)
    - GM*(jupiter.mass/M)*(1/r58**1.5)*( neptune.y - jupiter.y)
    - GM*(saturn.mass/M)*(1/r68**1.5)*( neptune.y - saturn.y)
    - GM*(uranus.mass/M)*(1/r78**1.5)*( neptune.y - uranus.y)
    
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

    saturn.vx += x_acc_saturn*dt
    saturn.vy += y_acc_saturn*dt

    saturn.x += saturn.vx*dt
    saturn.y += saturn.vy*dt

    uranus.vx += x_acc_uranus*dt
    uranus.vy += y_acc_uranus*dt

    uranus.x += uranus.vx*dt
    uranus.y += uranus.vy*dt

    neptune.vx += x_acc_neptune*dt
    uranus.vy += y_acc_neptune*dt

    neptune.x += neptune.vx*dt
    neptune.y += neptune.vy*dt

    
    #Energy.append(0.5*mearth*(vx**2 + vy**2) - (GM*mearth)/((x**2 + y**2)**0.5))
    

def animate(i):
    global mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

    integrate()

    t.append(i*dt)

    #print(earth.x, earth.y)

    planet1.set_data([mercury.x], [mercury.y])
    planet2.set_data([venus.x], [venus.y])
    planet3.set_data([earth.x], [earth.y])
    planet4.set_data([mars.x], [mars.y])
    planet5.set_data([jupiter.x], [jupiter.y])
    planet6.set_data([saturn.x], [saturn.y])
    planet7.set_data([uranus.x], [uranus.y])
    planet8.set_data([neptune.x], [neptune.y])
    
    return planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8

ani = animation.FuncAnimation(fig, animate,
                           frames = 60, interval=1, init_func = init )


plt.show()


#plt.plot(t, Energy)
#plt.show()
