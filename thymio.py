import dbus
import time

class Thymio:
    def __init__(self):
        print('Initialisation de thymio...')
        bus = dbus.SessionBus()
        proxy = bus.get_object('ch.epfl.mobots.Aseba', '/')
        self.network = dbus.Interface(proxy, dbus_interface='ch.epfl.mobots.Ase$
        print('Initialisation terminee!')

    def CapteursHorizontaux(self):
       capteurs = self.network.GetVariable("thymio-II", "prox.horizontal")
       return [int(i) for i in capteurs]

    def Avance(self, vitesse=1.0):
        self.network.SetVariable("thymio-II", "motor.left.target", [int(vitesse*$
        self.network.SetVariable("thymio-II", "motor.right.target", [int(vitesse$
    def Droite(self, vitesse=1.0):
       self.network.SetVariable("thymio-II", "motor.left.target", [int(vitesse*$
       self.network.SetVariable("thymio-II", "motor.right.target", [-int(vitess$
    def Gauche(self, vitesse=1.0):
       self.network.SetVariable("thymio-II", "motor.left.target", [-int(vitesse$
       self.network.SetVariable("thymio-II", "motor.right.target", [int(vitesse$
    def Recule(self, vitesse=1.0):
       self.network.SetVariable("thymio-II", "motor.left.target", [-int(vitesse$
       self.network.SetVariable("thymio-II", "motor.right.target", [-int(vitess$
    def Arret(self):
       self.network.SetVariable("thymio-II", "motor.left.target", [0])
       self.network.SetVariable("thymio-II", "motor.right.target", [-int(vitess$
    def Gauche(self, vitesse=1.0):
       self.network.SetVariable("thymio-II", "motor.left.target", [-int(vitesse$
       self.network.SetVariable("thymio-II", "motor.right.target", [int(vitesse$
    def Recule(self, vitesse=1.0):
       self.network.SetVariable("thymio-II", "motor.left.target", [-int(vitesse$
       self.network.SetVariable("thymio-II", "motor.right.target", [-int(vitess$
    def Arret(self):
       self.network.SetVariable("thymio-II", "motor.left.target", [0])
       self.network.SetVariable("thymio-II", "motor.right.target", [0])
