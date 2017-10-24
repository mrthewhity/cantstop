import time
from PyQt4 import QtCore, QtGui

class wait():
    def init(self,wait_Form):
        '''
        Cette fonction initialise la classe wait, celle-ci a pout but
        de faire attendre le programme quand l'utilisateur doit faire un choix sur l'interface
        :param wait_Form : QtGui.QDialog()
        '''

        self.chrono = False
        QtCore.QMetaObject.connectSlotsByName(wait_Form)

    def gestion_time_start(self):
        '''
        cette fonction permet de faire fonctionner le compteur
        '''
        
        self.chrono = True
        while self.chrono:            
            QtGui.qApp.processEvents()
            time.sleep(0.05)        
                 

    def gestion_time_stop(self):
        '''
        Cette fonction permet de faire arrêter le compteur
        '''
        self.chrono = False       


    def attente_IA(self):
        '''
        Cette fonction permet de laisser un petit interval de temps lorsque
        l'IA joue ,..., voir l'avancement du jeu de l'IA
        '''
        QtGui.qApp.processEvents()
        time.sleep(0.02)
        

 

