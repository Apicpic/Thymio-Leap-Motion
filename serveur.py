import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer

class Serveur:
    def __init__(self, thymio, port=8000):
        self.port = port
        self.server = SimpleXMLRPCServer(("adresse_IP", port))
        self.thymio = thymio
        self.server.register_function(self.Avance,"Avance")
        self.server.register_function(self.Recule,"Recule")
        self.server.register_function(self.Droite,"Droite")
        self.server.register_function(self.Gauche,"Gauche")
        self.server.register_function(self.Arret,"Arret")
        self.server.register_function(self.CapteursHorizontaux, "CapteursHorizo$
    def Run(self):
        print("Listening on port %d ..." %self.port)
        self.server.serve_forever()
        def Avance(self, vitesse):
        self.thymio.Avance(vitesse)
        return True
    def Recule(self, vitesse):
        self.thymio.Recule(vitesse)
        return True
    def Droite(self,vitesse):
        self.thymio.Droite(vitesse)
        return True
    def Gauche(self, vitesse):
        self.thymio.Gauche(vitesse)
        return True
    def Recule(self, vitesse):
        self.thymio.Recule(vitesse)
        return True
    def Droite(self,vitesse):
        self.thymio.Droite(vitesse)
        return True
    def Gauche(self, vitesse):
        self.thymio.Gauche(vitesse)
        return True
    def Arret(self):
        self.thymio.Arret()
        return True
