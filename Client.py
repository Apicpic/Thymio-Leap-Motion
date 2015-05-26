import xmlrpclib
import Sample2
import time

proxy = xmlrpclib.ServerProxy("http://adresse_IP_Thymio:1234")

last_event = 0

def TropRecent():
  global last_event
  t = time.time()
  if t < last_event:
    return True
  frequence_seconde = 0.1
  last_event = t + frequence_seconde
  return False

def Arrondi(a):
    seuil = 75
    return int(round(a / (2 * seuil)))

def Position(x, y, z):
    if TropRecent():
      return
    xx = Arrondi(x)
    zz = Arrondi(z)
    yy = (y/400.0)
    print(x, y, z)

    if (xx == 0 and zz == 0) or (xx != 0 and zz != 0):
      print("Centre %d %d" % (xx, zz))
      proxy.Arret()
      return
    if xx < 0:
        print("Gauche")
        proxy.Gauche(1)
    elif xx > 0:
        print ("Droite")
        proxy.Droite(1)
    elif zz > 0:
        print("Recule")
        proxy.Recule(yy)
    else:
        print("Avance")
        proxy.Avance(yy)
    return

def Rien():
    if TropRecent():
      return
    print("Arret")
    proxy.Arret()

#    global last_event
#    t = time.time()
#    if t < last_event:
#        return
#    last_event = t + 0.5
#    print("Recule "  + str(t ))
#    proxy.Recule(0.5-0.02)

#while 1:
#    t = time.time()
#    print(proxy.CapteursHorizontaux())
#    print(time.time()-t)
#    time.sleep(1)


Leap = Sample2.Leap_position(Position, Rien)


while True:
    pass


