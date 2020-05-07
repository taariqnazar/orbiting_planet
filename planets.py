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
        self.x = [x]
        self.y = [y]
        #Always starts at x,y = (*, 0)
        self.vx = [0]
        self.vy = [(GM/(x**2+y**2)**0.5)**0.5]
        self.ax = []
        self.ay = []
    
    def set_pos(self, x, y):

        self.x.append(x)
        self.y.append(y)

    def set_vel(self, vx, vy):
        self.vx.append(vx)
        self.vy.append(vy)

    #Returns distance between this planet and given planet
    def distance(self,planet):
        dx = self.x[-1] - planet.x[-1]
        dy = self.y[-1] - planet.y[-1]

        return (dx**2 + dy**2)**0.5

    

    def acceleration(self,planets = [], time= -1):
        x_acc = -(GM*self.x[time])/((self.x[time]**2 + self.y[time]**2)**(1.5)) 
        y_acc = -(GM*self.y[time])/((self.x[time]**2 + self.y[time]**2)**(1.5))

        for planet in planets:
            x_acc -= GM*(planet.mass/M)*(1/(self.distance(planet))**1.5)*(self.x[time] - planet.x[time])
            
            y_acc -= GM*(planet.mass/M)*(1/(self.distance(planet))**1.5)*(self.y[time] - planet.y[time])
            
        return x_acc, y_acc
        

    def mek_energy(self):
        Ek = 0.5*self.mass*(self.vx[-1]**2 + self.vy[-1]**2)*4743.2**2
        Ep = - GM*self.mass*(1/((self.x[-1]**2 + self.y[-1]**2)**0.5))*4743.2**2
        return Ek + Ep

class Asteroid(Planet):
    def __init__(self, mass, x, y, vx = 0, vy = 0):
        self.mass = mass
        self.x = [x]
        self.y = [y]
        self.vx = [vx]
        self.vy = [vy]

        
#Parameters to Study -------------------------------------------#
Energy = []
t = []


#Plot setup ----------------------------------------------------#
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))




#initailitze celestial bodies
sun, = ax.plot([0], [0], "y.", ms=10)

planet1, = ax.plot([], [], ".", color="#CA6651", ms = 8,)
planet1trail, = ax.plot([], [], ":",color="#CA6651", ms = 1, label = "Mercury")
mercury = Planet(3.285*10**23,AU*0.387,0)

planet2, = ax.plot([], [], ".", color="#FFB2A1", ms = 8)
planet2trail, = ax.plot([], [], ":", color="#FFB2A1", ms = 1, label = "Venus")
venus = Planet(4.867*10**24,AU*0.723,0)

planet3, = ax.plot([], [], ".", color="#2E8F56", ms = 8)
planet3trail, = ax.plot([], [], ":", color="#2E8F56", ms = 1, label = "Earth")
earth = Planet(5.972*10**24,AU*1,0)

planet4, = ax.plot([], [], "m.",color="#CCB582", ms = 8)
planet4trail, = ax.plot([], [], "m:",color="#CCB582", ms = 1, label = "Mars")
mars = Planet(6.39*10**23,AU*1.523, 0)

planet5, = ax.plot([], [], ".", color="#FFF0CD", ms = 8)
planet5trail, = ax.plot([], [], ":",color="#FFF0CD", ms = 1, label = "Jupiter")
jupiter = Planet(1.898*10**27,AU*5.202, 0)

planet6, = ax.plot([], [], "g.",color="#9D8776", ms = 8)
planet6trail, = ax.plot([], [], "g:",color="#9D8776", ms = 1, label = "Saturn")
saturn = Planet(5.683*10**26,AU*9.539, 0)

planet7, = ax.plot([], [], "y.",color="#97D9DF", ms = 8)
planet7trail, = ax.plot([], [], "y:",color="#97D9DF", ms = 1, label = "Uranus")
uranus = Planet(8.681*10**25,AU*19.18, 0)

planet8, = ax.plot([], [], "b.",color="#295B5F", ms = 8)
planet8trail, = ax.plot([], [], "b:",color="#295B5F", ms = 1, label = "Neptune")
neptune = Planet(1.024*10**26,AU*30.06, 0)


asteroidplt, = ax.plot([], [], "ro",color="#808788", ms = 8)
asteroidtrail, = ax.plot([], [], "r:",color="#808788", ms = 1, ) #label = "Asteroid")
asteroid = Asteroid(10**26, 2, -0.5, -5, 0)


tstep = 0
dt = 0.001

def init():
    global asteroidtrail, planet1trail, planet2trail, planet3trail, planet4trail, planet5trail, planet6trail,planet7trail,planet8trail, asteroidplt, planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8

    asteroidtrail.set_data([], [])
    asteroidplt.set_data([],[])

    planet1trail.set_data([], [])
    planet1.set_data([], [])

    planet2trail.set_data([], [])
    planet2.set_data([], [])
    
    planet3.set_data([], [])
    planet3trail.set_data([], [])
    
    planet4.set_data([], [])
    planet4trail.set_data([], [])
    
    planet5.set_data([], [])
    planet5trail.set_data([], [])
    
    planet6.set_data([], [])
    planet6trail.set_data([], [])
    
    planet7.set_data([], [])
    planet7trail.set_data([], [])
    
    planet8.set_data([], [])
    planet8trail.set_data([], [])
    
    return asteroidtrail, planet1trail, planet2trail,planet3trail, planet4trail, planet5trail, planet6trail,planet7trail,planet8trail, asteroidplt, planet1,planet2,planet3,planet4,planet5,planet6,planet7,planet8

def integrate():
    global tstep, asteroid, mercury, venus, earth, mars, jupiter, uranus, neptune

    planets = [asteroid, mercury, venus, earth, mars,
               jupiter, uranus, neptune]

    
    ##EULER CROMER

    #ASTEROID acceleration
    x_acc_asteroid, y_acc_asteroid = asteroid.acceleration([mercury,venus, earth,
                                                 mars, jupiter, saturn,
                                                 uranus, neptune])
    #MERCURY acceleration
    x_acc_mercury, y_acc_mercury = mercury.acceleration([asteroid,venus, earth,
                                                 mars, jupiter, saturn,
                                                 uranus, neptune])

    #VENUS acceleration
    x_acc_venus ,y_acc_venus = venus.acceleration([asteroid,mercury, earth,
                                            mars, jupiter,saturn,
                                            uranus, neptune])

    #EARTH acceleration
    x_acc_earth, y_acc_earth = earth.acceleration([asteroid, mercury, venus,
                                            mars, jupiter, saturn,
                                            uranus, neptune])

    #MARS acceleration
    x_acc_mars, y_acc_mars = mars.acceleration([asteroid, mercury, venus, earth,
                                            jupiter, saturn,
                                            uranus, neptune])

    #JUPITER acceleration
    x_acc_jupiter, y_acc_jupiter = jupiter.acceleration([asteroid, mercury, venus, earth,
                                            mars, saturn,
                                            uranus, neptune])

    #SATURN acceleration
    x_acc_saturn, y_acc_saturn =saturn.acceleration([asteroid, mercury, venus, earth,
                                            mars, jupiter,
                                            uranus, neptune])

    #URANUS acceleration
    x_acc_uranus, y_acc_uranus = uranus.acceleration([asteroid, mercury, venus, earth,
                                            mars, jupiter, saturn,
                                            neptune])

    #NEPTUNE acceleration
    x_acc_neptune, y_acc_neptune = neptune.acceleration([asteroid, mercury, venus, earth,
                                            mars, jupiter, saturn,
                                            uranus])
    
    
    asteroid.set_vel(asteroid.vx[-1] + x_acc_asteroid*dt,
                     asteroid.vy[-1] + y_acc_asteroid*dt)
    asteroid.set_pos(asteroid.x[-1] + asteroid.vx[-1]*dt,
                     asteroid.y[-1] + asteroid.vy[-1]*dt)


    mercury.set_vel(mercury.vx[-1] + x_acc_mercury*dt,
                     mercury.vy[-1] + y_acc_mercury*dt)
    mercury.set_pos(mercury.x[-1] + mercury.vx[-1]*dt,
                     mercury.y[-1] + mercury.vy[-1]*dt)
    
    venus.set_vel(venus.vx[-1] + x_acc_venus*dt,
                     venus.vy[-1] + y_acc_venus*dt)
    venus.set_pos(venus.x[-1] + venus.vx[-1]*dt,
                     venus.y[-1] + venus.vy[-1]*dt)

    
    earth.set_vel(earth.vx[-1] + x_acc_earth*dt,
                     earth.vy[-1] + y_acc_earth*dt)
    earth.set_pos(earth.x[-1] + earth.vx[-1]*dt,
                     earth.y[-1] + earth.vy[-1]*dt)

    mars.set_vel(mars.vx[-1] + x_acc_mars*dt,
                     mars.vy[-1] + y_acc_mars*dt)
    mars.set_pos(mars.x[-1] + mars.vx[-1]*dt,
                     mars.y[-1] + mars.vy[-1]*dt)


    jupiter.set_vel(jupiter.vx[-1] + x_acc_jupiter*dt,
                     jupiter.vy[-1] + y_acc_jupiter*dt)
    jupiter.set_pos(jupiter.x[-1] + jupiter.vx[-1]*dt,
                     jupiter.y[-1] + jupiter.vy[-1]*dt)

    saturn.set_vel(saturn.vx[-1] + x_acc_saturn*dt,
                     saturn.vy[-1] + y_acc_saturn*dt)
    saturn.set_pos(saturn.x[-1] + saturn.vx[-1]*dt,
                     saturn.y[-1] + saturn.vy[-1]*dt)

    uranus.set_vel(uranus.vx[-1] + x_acc_uranus*dt,
                     uranus.vy[-1] + y_acc_uranus*dt)
    uranus.set_pos(uranus.x[-1] + uranus.vx[-1]*dt,
                     uranus.y[-1] + uranus.vy[-1]*dt)


    neptune.set_vel(neptune.vx[-1] + x_acc_neptune*dt,
                     neptune.vy[-1] + y_acc_neptune*dt)
    neptune.set_pos(neptune.x[-1] + neptune.vx[-1]*dt,
                     neptune.y[-1] + neptune.vy[-1]*dt)
    #END EULER CROMER

    ##VERLET
##    
##    #ASTEROID acceleration
##    x_acc_asteroid, y_acc_asteroid = asteroid.acceleration([mercury,venus, earth,
##                                                 mars, jupiter, saturn,
##                                                 uranus, neptune])
##    #MERCURY acceleration
##    x_acc_mercury, y_acc_mercury = mercury.acceleration([asteroid,venus, earth,
##                                                 mars, jupiter, saturn,
##                                                 uranus, neptune])
##
##    #VENUS acceleration
##    x_acc_venus ,y_acc_venus = venus.acceleration([asteroid,mercury, earth,
##                                            mars, jupiter,saturn,
##                                            uranus, neptune])
##
##    #EARTH acceleration
##    x_acc_earth, y_acc_earth = earth.acceleration([asteroid, mercury, venus,
##                                            mars, jupiter, saturn,
##                                            uranus, neptune])
##
##    #MARS acceleration
##    x_acc_mars, y_acc_mars = mars.acceleration([asteroid, mercury, venus, earth,
##                                            jupiter, saturn,
##                                            uranus, neptune])
##
##    #JUPITER acceleration
##    x_acc_jupiter, y_acc_jupiter = jupiter.acceleration([asteroid, mercury, venus, earth,
##                                            mars, saturn,
##                                            uranus, neptune])
##
##    #SATURN acceleration
##    x_acc_saturn, y_acc_saturn =saturn.acceleration([asteroid, mercury, venus, earth,
##                                            mars, jupiter,
##                                            uranus, neptune])
##
##    #URANUS acceleration
##    x_acc_uranus, y_acc_uranus = uranus.acceleration([asteroid, mercury, venus, earth,
##                                            mars, jupiter, saturn,
##                                            neptune])
##
##    #NEPTUNE acceleration
##    x_acc_neptune, y_acc_neptune = neptune.acceleration([asteroid, mercury, venus, earth,
##                                            mars, jupiter, saturn,
##                                            uranus])
##
##
##    asteroid.set_pos(asteroid.x[-1] + asteroid.vx[-1]*dt + 0.5*x_acc_asteroid*dt**2,
##                     asteroid.y[-1] + asteroid.vy[-1]*dt + 0.5*y_acc_asteroid*dt**2)
##
##
##    mercury.set_pos(mercury.x[-1] + mercury.vx[-1]*dt + 0.5*x_acc_mercury*dt**2,
##                     mercury.y[-1] + mercury.vy[-1]*dt + 0.5*y_acc_mercury*dt**2)
##    
##    venus.set_pos(venus.x[-1] + venus.vx[-1]*dt + 0.5*x_acc_venus*dt**2,
##                     venus.y[-1] + venus.vy[-1]*dt + 0.5*y_acc_venus*dt**2)
##
##    earth.set_pos(earth.x[-1] + earth.vx[-1]*dt + 0.5*x_acc_earth*dt**2,
##                     earth.y[-1] + earth.vy[-1]*dt + 0.5*y_acc_earth*dt**2)
##
##    mars.set_pos(mars.x[-1] + mars.vx[-1]*dt + 0.5*x_acc_mars*dt**2,
##                     mars.y[-1] + mars.vy[-1]*dt + 0.5*y_acc_mars*dt**2)
##
##
##    jupiter.set_pos(jupiter.x[-1] + jupiter.vx[-1]*dt + 0.5*x_acc_jupiter*dt**2,
##                     jupiter.y[-1] + jupiter.vy[-1]*dt + 0.5*y_acc_jupiter*dt**2)
##
##    saturn.set_pos(saturn.x[-1] + saturn.vx[-1]*dt + 0.5*x_acc_saturn*dt**2,
##                     saturn.y[-1] + saturn.vy[-1]*dt + 0.5*y_acc_saturn*dt**2)
##
##    uranus.set_pos(uranus.x[-1] + uranus.vx[-1]*dt + 0.5*x_acc_uranus*dt**2,
##                     uranus.y[-1] + uranus.vy[-1]*dt + 0.5*y_acc_uranus*dt**2)
##
##
##    neptune.set_pos(neptune.x[-1] + neptune.vx[-1]*dt + 0.5*x_acc_neptune*dt**2,
##                     neptune.y[-1] + neptune.vy[-1]*dt + 0.5*y_acc_neptune*dt**2)
##
##     #ASTEROID acceleration
##    nx_acc_asteroid, ny_acc_asteroid = asteroid.acceleration([mercury,venus, earth,
##                                                 mars, jupiter, saturn,
##                                                 uranus, neptune])
##    #MERCURY acceleration
##    nx_acc_mercury, ny_acc_mercury = mercury.acceleration([asteroid,venus, earth,
##                                                 mars, jupiter, saturn,
##                                                 uranus, neptune])
##
##    #VENUS acceleration
##    nx_acc_venus ,ny_acc_venus = venus.acceleration([asteroid,mercury, earth,
##                                            mars, jupiter,saturn,
##                                            uranus, neptune])
##
##    #EARTH acceleration
##    nx_acc_earth, ny_acc_earth = earth.acceleration([asteroid, mercury, venus,
##                                            mars, jupiter, saturn,
##                                            uranus, neptune])
##
##    #MARS acceleration
##    nx_acc_mars, ny_acc_mars = mars.acceleration([asteroid, mercury, venus, earth,
##                                            jupiter, saturn,
##                                            uranus, neptune])
##
##    #JUPITER acceleration
##    nx_acc_jupiter, ny_acc_jupiter = jupiter.acceleration([asteroid, mercury, venus, earth,
##                                            mars, saturn,
##                                            uranus, neptune])
##
##    #SATURN acceleration
##    nx_acc_saturn, ny_acc_saturn =saturn.acceleration([asteroid, mercury, venus, earth,
##                                            mars, jupiter,
##                                            uranus, neptune])
##
##    #URANUS acceleration
##    nx_acc_uranus, ny_acc_uranus = uranus.acceleration([asteroid, mercury, venus, earth,
##                                            mars, jupiter, saturn,
##                                            neptune])
##
##    #NEPTUNE acceleration
##    nx_acc_neptune, ny_acc_neptune = neptune.acceleration([asteroid, mercury, venus, earth,
##                                            mars, jupiter, saturn,
##                                            uranus])
##
##    asteroid.set_vel(asteroid.vx[-1] + 0.5*( nx_acc_asteroid + x_acc_asteroid)*dt,
##                     asteroid.vy[-1] + 0.5*( ny_acc_asteroid + y_acc_asteroid)*dt)
##
##
##    mercury.set_vel(mercury.vx[-1] + 0.5*( nx_acc_mercury + x_acc_mercury)*dt,
##                    mercury.vy[-1] + 0.5*( ny_acc_mercury + y_acc_mercury)*dt)
##
##    
##    venus.set_vel(venus.vx[-1] + 0.5*( nx_acc_venus + x_acc_venus)*dt,
##                  venus.vy[-1] + 0.5*( ny_acc_venus + y_acc_venus)*dt)
##
##    
##    earth.set_vel(earth.vx[-1] + 0.5*( nx_acc_earth + x_acc_earth)*dt,
##                     earth.vy[-1] + 0.5*( ny_acc_earth + y_acc_earth)*dt)
##
##    mars.set_vel(mars.vx[-1] + 0.5*( nx_acc_mars + x_acc_mars)*dt,
##                     mars.vy[-1] + 0.5*( ny_acc_mars + y_acc_mars)*dt)
##
##
##
##    jupiter.set_vel(jupiter.vx[-1] + 0.5*( nx_acc_jupiter + x_acc_jupiter)*dt,
##                     jupiter.vy[-1] + 0.5*( ny_acc_jupiter + y_acc_jupiter)*dt)
##
##
##    saturn.set_vel(saturn.vx[-1] + 0.5*( nx_acc_saturn + x_acc_saturn)*dt,
##                     saturn.vy[-1] + 0.5*( ny_acc_saturn + y_acc_saturn)*dt)
##
##
##    uranus.set_vel(uranus.vx[-1] + 0.5*( nx_acc_uranus+ x_acc_uranus)*dt,
##                     uranus.vy[-1] + 0.5*( ny_acc_uranus + y_acc_uranus)*dt)
##
##
##    neptune.set_vel(neptune.vx[-1] + 0.5*( nx_acc_neptune + x_acc_neptune)*dt,
##                     neptune.vy[-1] + 0.5*( ny_acc_neptune + y_acc_neptune)*dt)
##
##    
    
    t.append(tstep*dt)
    tstep += 1

    E = 0

    for p in planets:
        E += p.mek_energy()
    
    Energy.append(E)
    

def animate(i):
    global asteroidtrail, planet1trail, planet2trail, planet3trail, planet4trail, planet5trail, planet6trail,planet7trail,planet8trail, asteroid, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune

    integrate()

    asteroidtrail.set_data(asteroid.x, asteroid.y)
    asteroidplt.set_data([asteroid.x[-1]], [asteroid.y[-1]])
    
    planet1.set_data([mercury.x[-1]], [mercury.y[-1]])
    planet1trail.set_data(mercury.x, mercury.y)
    
    planet2.set_data([venus.x[-1]], [venus.y[-1]])
    planet2trail.set_data(venus.x, venus.y)
    
    planet3.set_data([earth.x[-1]], [earth.y[-1]])
    planet3trail.set_data(earth.x, earth.y)
    
    planet4.set_data([mars.x[-1]], [mars.y[-1]])
    planet4trail.set_data(mars.x, mars.y)
    
    planet5.set_data([jupiter.x[-1]], [jupiter.y[-1]])
    planet5trail.set_data(jupiter.x, jupiter.y)
    
    planet6.set_data([saturn.x[-1]], [saturn.y[-1]])
    planet6trail.set_data(saturn.x, saturn.y)
    
    planet7.set_data([uranus.x[-1]], [uranus.y[-1]])
    planet7trail.set_data(uranus.x, uranus.y)
    
    planet8.set_data([neptune.x[-1]], [neptune.y[-1]])
    planet8trail.set_data(neptune.x, neptune.y)
    
    return asteroidtrail, planet1trail, planet2trail,planet3trail, planet4trail,
    planet5trail, planet6trail,planet7trail,planet8trail,
    asteroidplt, planet1, planet2, planet3, planet4,
    planet5, planet6, planet7, planet8

##ani = animation.FuncAnimation(fig, animate,
##                          frames = 60, interval=1, init_func = init )
##


ax.legend()
ax.set_title("Solar System")
ax.set_xlabel("AU")
ax.set_ylabel("AU")



#plt.show()

time = 1000

for i in range(0,int(time/dt)): #THOUSAND YEARS
    integrate()
    
##axn = plt.axes()
##axn.set_xlabel("Position [AU]")
##axn.set_ylabel("Velocity [AU/Year]")
##axn.set_title("Phase Portrait [Mercury]")
##p2, = axn.plot(mercury.y, mercury.vy)
##p1, = axn.plot(mercury.x, mercury.vx)
##axn.legend((p1, p2), ("x-coordinate", "y-coordinate"))

##
axn = plt.axes()
axn.set_title("Total Mechanical Energy")
axn.set_xlabel("Time [Years]")
axn.set_ylabel("Energy [Joules]")
axn.plot(t, Energy)

##planet1.set_data([mercury.x[-1]], [mercury.y[-1]])
##planet1trail.set_data(mercury.x, mercury.y)
##
##planet2.set_data([venus.x[-1]], [venus.y[-1]])
##planet2trail.set_data(venus.x, venus.y)
##
##planet3.set_data([earth.x[-1]], [earth.y[-1]])
##planet3trail.set_data(earth.x, earth.y)
##
##planet4.set_data([mars.x[-1]], [mars.y[-1]])
##planet4trail.set_data(mars.x, mars.y)
##
##planet5.set_data([jupiter.x[-1]], [jupiter.y[-1]])
##planet5trail.set_data(jupiter.x, jupiter.y)
##
##planet6.set_data([saturn.x[-1]], [saturn.y[-1]])
##planet6trail.set_data(saturn.x, saturn.y)
##
##planet7.set_data([uranus.x[-1]], [uranus.y[-1]])
##planet7trail.set_data(uranus.x, uranus.y)
##
##planet8.set_data([neptune.x[-1]], [neptune.y[-1]])
##planet8trail.set_data(neptune.x, neptune.y)
##
plt.savefig("euler_ast_m26_E_0001.png")
plt.show()   
