from thymio import Thymio
from serveur import Serveur

robot = Thymio()
server = Serveur(robot, 1234)
server.Run()
