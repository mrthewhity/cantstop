from PyQt4 import QtCore, QtGui
import time
from Jeu import *





class GUI():
    def __init__(self):
    	'''
    	Cette fonction initialise les attributs pour afficher les élements principaux
    	'''

    	self.listeJoueur = []
    	self.pseudo_joueur , self.IA_level= [] , []
    	self.valueTest =False
    	self.formGame = QtGui.QDialog()
    	self.FormLoad = QtGui.QWidget()    	
    	self.formsetup = QtGui.QWidget()
    	self.formLoad()
    	self.etat = False # cette variable nous dit si le joueur va continuer ou non (etat du tour)
    	self.warningBoxFrom = QtGui.QWidget()
        

   

    def formLoad(self):
    	'''
    	cette foonction permet de charger la fenetre de chargement du jeu
    	'''
    	self.load_Ui(self.FormLoad)
    	self.move_center(self.FormLoad)
    	self.FormLoad.show()
    	self.load_progress()
    	self.FormLoad.hide()
    	self.formsetup = QtGui.QWidget()
    	self.setup_Ui(self.formsetup)
    	self.move_center(self.formsetup)
    	self.formsetup.show()

    def load_Ui(self, LoadForm):

        #Paramétrage de la FORM en elle-même
        LoadForm.setObjectName("LoadForm")
        LoadForm.resize(543, 297)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        LoadForm.setPalette(palette)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadForm.sizePolicy().hasHeightForWidth())
        LoadForm.setSizePolicy(sizePolicy)
        LoadForm.setMinimumSize(QtCore.QSize(543, 297))
        LoadForm.setMaximumSize(QtCore.QSize(543, 297))       
        LoadForm.setCursor(QtGui.QCursor(QtCore.Qt.BusyCursor))
		
        LoadForm.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
	
        # Icône
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/pawnR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoadForm.setWindowIcon(icon)
        LoadForm.setAutoFillBackground(False)

        #ProgressBar
        self.progressBar = QtGui.QProgressBar(LoadForm)
        self.progressBar.setGeometry(QtCore.QRect(100, 210, 351, 23))
        self.progressBar.setMaximum(100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.labelGame = QtGui.QLabel(LoadForm)
        self.labelGame.setGeometry(QtCore.QRect(120, 30, 261, 111))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelGame.sizePolicy().hasHeightForWidth())
        self.labelGame.setSizePolicy(sizePolicy)        

        # Paramétrage des polices, couleurs du logo et du titre
        palette = QtGui.QPalette()    
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)    
        self.labelGame.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Utopia")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.labelGame.setFont(font)
        self.labelGame.setObjectName("labelGame")
        self.logoGame = QtGui.QLabel(LoadForm)
        self.logoGame.setGeometry(QtCore.QRect(390, 40, 31, 61))
        self.logoGame.setText("")        
        self.logoGame.setPixmap(QtGui.QPixmap("image/pawnR.png"))
        self.logoGame.setScaledContents(True)
        self.logoGame.setObjectName("logoGame")
                


        # paramétrage des polices, couleurs de la version du jeu et copyright(designed by)
        self.designedLabel = QtGui.QLabel(LoadForm)
        self.designedLabel.setGeometry(QtCore.QRect(359, 280, 210, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.designedLabel.setFont(font)
        self.designedLabel.setObjectName("designedLabel")
        self.version = QtGui.QLabel(LoadForm)
        self.version.setGeometry(QtCore.QRect(10, 280, 100, 17))        
        font = QtGui.QFont()
        font.setItalic(True)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.labelLoading = QtGui.QLabel(LoadForm)
        self.labelLoading.setGeometry(QtCore.QRect(250, 190, 61, 17))




        #Tous les strings affichés sur le FORM, ré-éddition facile
        LoadForm.setWindowTitle( "Welcome     ")
        self.labelGame.setText( "Can\'t Stop !")
        self.designedLabel.setText( "designed by Derras Eiman")
        self.version.setText( "version 1.3")
        self.labelLoading.setText("Loading ...")

        QtCore.QMetaObject.connectSlotsByName(LoadForm)	

    def load_progress(self):
        '''
        Cette fonction permet de faire avancer la progress bar
        '''

        for i in range(101):
            time.sleep(0.02)
            self.progressBar.setProperty("value", i)


    def setup_Ui(self,setupForm):
        '''
        cette fonction permet de charger la fenêtre du setup players avec tous ses éléments
        :param setupForm : QtGui.QDialog()
        '''
        # préparation de la form (backgroud,couleur, etc)
        setupForm.setObjectName("setupForm")
        setupForm.resize(591, 595)        
        setupForm.setMinimumSize(QtCore.QSize(591, 595))
        setupForm.setMaximumSize(QtCore.QSize(591, 595))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        setupForm.setPalette(palette)

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        setupForm.setFont(font)
       
        self.titre_setup = QtGui.QLabel(setupForm)
        self.titre_setup.setGeometry(QtCore.QRect(60, 10, 541, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)      
        self.titre_setup.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.titre_setup.setFont(font)
        self.titre_setup.setObjectName("titre_setup")

        # Icône
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("image/pawnR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        setupForm.setWindowIcon(icon)
        


        # Bloc de commande du nombre de joueurs
        self.GroupBOXhd = QtGui.QGroupBox(setupForm)
        self.GroupBOXhd.setGeometry(QtCore.QRect(0, 190, 581, 351))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.GroupBOXhd.setFont(font)
        self.GroupBOXhd.setTitle("")
        self.GroupBOXhd.setFlat(False)
        self.GroupBOXhd.setCheckable(False)
        self.GroupBOXhd.setObjectName("GroupBOXhd")
        self.label_PlayerX = QtGui.QLabel(self.GroupBOXhd)
        self.label_PlayerX.setGeometry(QtCore.QRect(80, 100, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.label_PlayerX.setFont(font)
        self.label_PlayerX.setObjectName("label_PlayerX")
        self.radioButton_USER = QtGui.QRadioButton(self.GroupBOXhd)
        self.radioButton_USER.setGeometry(QtCore.QRect(70, 230, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_USER.setFont(font)
        self.radioButton_USER.setChecked(True)
        self.radioButton_USER.setAutoExclusive(True)
        self.radioButton_USER.setObjectName("radioButton_USER")
        self.radioButton_IA = QtGui.QRadioButton(self.GroupBOXhd)
        self.radioButton_IA.setGeometry(QtCore.QRect(230, 230, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radioButton_IA.setFont(font)
        self.radioButton_IA.setObjectName("radioButton_IA")
        self.image_user = QtGui.QLabel(self.GroupBOXhd)
        self.image_user.setGeometry(QtCore.QRect(160, 220, 51, 41))
        self.image_user.setText("")
        self.image_user.setPixmap(QtGui.QPixmap("image/personnage.png"))
        self.image_user.setScaledContents(True)
        self.image_user.setObjectName("image_user")
        self.image_IA = QtGui.QLabel(self.GroupBOXhd)
        self.image_IA.setGeometry(QtCore.QRect(300, 220, 41, 41))
        self.image_IA.setText("")
        self.image_IA.setPixmap(QtGui.QPixmap("image/ordi.jpg"))
        self.image_IA.setScaledContents(True)
        self.image_IA.setObjectName("image_IA")
        self.button_OK = QtGui.QPushButton(self.GroupBOXhd)
        self.button_OK.setGeometry(QtCore.QRect(450, 230, 88, 29))
        self.button_OK.setObjectName("button_OK")
        self.windowsBlack = QtGui.QLabel(self.GroupBOXhd)
        self.windowsBlack.setGeometry(QtCore.QRect(20, 70, 551, 261))
        self.windowsBlack.setText("")
        self.windowsBlack.setPixmap(QtGui.QPixmap("image/carre-noir.png"))
        self.windowsBlack.setScaledContents(True)
        self.windowsBlack.setObjectName("windowsBlack")
        self.button_stop = QtGui.QPushButton(self.GroupBOXhd)
        self.button_stop.setGeometry(QtCore.QRect(450, 270, 88, 29))
        self.button_stop.setObjectName("button_stop")
        self.button_stop.setEnabled(False)

        self.button_begin = QtGui.QPushButton(self.GroupBOXhd)
        self.button_begin.setGeometry(QtCore.QRect(70, 110, 150, 50))
        self.button_begin.setObjectName("button_begin")
        self.button_begin.setEnabled(True)
        self.button_begin.hide()
        self.button_begin.setText("BEGIN THE GAME")
            

                                                                                                                                                                                                    
        self.instru2 = QtGui.QLabel(self.GroupBOXhd)
        self.instru2.setGeometry(QtCore.QRect(60, 20, 341, 21))
        self.instru2.setObjectName("instru2")
        self.instru1 = QtGui.QLabel(self.GroupBOXhd)
        self.instru1.setGeometry(QtCore.QRect(60, 0, 360, 16))
        self.instru1.setTextFormat(QtCore.Qt.AutoText)
        self.instru1.setObjectName("instru1")
        self.label = QtGui.QLabel(self.GroupBOXhd)
        self.label.setGeometry(QtCore.QRect(30, 80, 531, 241))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/carre2.png"))
        self.label.setObjectName("label")
        self.windowsBlack.raise_()
        self.label.raise_()
        self.label_PlayerX.raise_()
        self.radioButton_IA.raise_()
        self.image_user.raise_()
        self.button_OK.raise_()
        self.button_stop.raise_()
        self.button_begin.raise_()
        self.instru2.raise_()
        self.instru1.raise_()
        self.image_IA.raise_()
        self.radioButton_USER.raise_()
        self.label_Config = QtGui.QLabel(setupForm)
        self.label_Config.setGeometry(QtCore.QRect(40, 540, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_Config.setFont(font)
        self.label_Config.setObjectName("label_Config")
        self.label_info_config = QtGui.QLabel(setupForm)
        self.label_info_config.setGeometry(QtCore.QRect(300, 540, 331, 41))
        self.label_info_config.setFont(font)
        self.label_info_config.setObjectName("label_info_config")

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_info_config.setFont(font)


        # On peut choisir le choix du nom de joueur (Player ou AI)
        self.nom_joueur = QtGui.QLineEdit(setupForm)
        self.nom_joueur.setGeometry(QtCore.QRect(250, 306, 150, 41))        
        self.nom_joueur.setText("")
        
        self.label_username = QtGui.QLabel(setupForm)
        self.label_username.setGeometry(QtCore.QRect(255, 332, 331, 41))
        self.label_username.setText("username")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_username.setFont(font)


        self.Choix_level_IA = QtGui.QComboBox(setupForm)
        self.Choix_level_IA.setGeometry(QtCore.QRect(301,467,60,30))
        for x in range(1,5):
            self.Choix_level_IA.addItem(str(x))

        self.label_level = QtGui.QLabel(setupForm)
        self.label_level.setGeometry(QtCore.QRect(255,477,100,14))
        self.label_level.setObjectName("designedLabel")
        self.label_level.setText("IA level")
        
      


        #Tous les strings affichés sur le FORM, ré-éddition facile
        setupForm.setWindowTitle("SETUP")
        self.titre_setup.setText("You can select the type of player")
        self.label_PlayerX.setText("Player 1 :")
        self.radioButton_USER.setText("User")
        self.radioButton_IA.setText("IA")
        self.button_OK.setText("OK")
        self.button_stop.setText("STOP")
        self.instru2.setText("<html><head/><body><p>* press STOP if you don\'t want any more players</p></body></html>")
        self.instru1.setText("* choose the type and a username of player and press OK")
        self.label_Config.setText("Your configuration : ")
        self.label_info_config.setText("")

        
        
        # appel des fonctions lorsque boutton préssé
        QtCore.QObject.connect(self.button_OK, QtCore.SIGNAL("clicked()"), self.ajoutPlayer)
        QtCore.QObject.connect(self.button_stop, QtCore.SIGNAL("clicked()"), self.stopChoix)
        QtCore.QObject.connect(self.button_begin, QtCore.SIGNAL("clicked()"), self.stopBegin)
        QtCore.QMetaObject.connectSlotsByName(setupForm)   
        


    
    	
    def ajoutPlayer(self):
        '''
        Cette fonction permet d'ajouter des joueurs à la partie
        On peut également fournir un pseudo dans l'interface
        '''
        mot=""
        if len(self.listeJoueur)>=0 and len(self.listeJoueur) <=3: # on vérifie qu'il a au moins 2 joueurs (max 4)
            
            self.listeJoueur.append(self.radioButton_IA.isChecked())
            if len(self.listeJoueur)+1 !=5:

                self.label_PlayerX.setText("Player "+str(len(self.listeJoueur)+1)+" :")
            else:
                self.label_PlayerX.setText("")
                self.button_begin.show()
                self.button_OK.setEnabled(False)
                self.button_stop.setEnabled(False)


            for joueur in self.listeJoueur:
                if joueur == True:
                    mot+="AI,"
                else:
                    mot+="USER,"

            mot=mot[:len(mot)-1]
            self.label_info_config.setText("["+mot+"]")

        if len(self.listeJoueur)>1 and len(self.listeJoueur)<4:
            self.button_stop.setEnabled(True)


        if self.nom_joueur.text() == "":
            nom_generate=""
            if self.radioButton_IA.isChecked():
                i=0
                for ia in self.listeJoueur:
                    if ia ==True:
                        i+=1
                nom_generate="IA_"+str(i)
                
            else:
                i=0
                for player in self.listeJoueur:
                    if player ==False:
                        i+=1
                nom_generate="USER_"+str(i)
                

            self.pseudo_joueur.append(nom_generate)
        else:
            self.pseudo_joueur.append(self.nom_joueur.text())

        self.IA_level.append(str(self.Choix_level_IA.currentText())) if self.radioButton_IA.isChecked() else self.IA_level.append(None)
        self.nom_joueur.setText("")

        if len(self.pseudo_joueur)==4:
            self.nom_joueur.hide()
            self.label_username.hide()

        
        

    def stopChoix(self):
        '''
        cette fonction permet d'arréter le setup player
        '''

        self.label_PlayerX.setText("")
        self.button_begin.show()
        self.button_OK.setEnabled(False)
        self.button_stop.setEnabled(False)
        self.nom_joueur.hide()
        self.label_username.hide()

    	

    def stopBegin(self):
        '''
        Cette fonction permet de commencer le jeu et fermer le stup player
        '''
        self.gameUi(self.formGame)
        self.move_center(self.formGame)
        self.formGame.show()
        


        self.jeu = Jeu(self.listeJoueur, self.IA_level)
        self.formsetup.hide()
        self.jeu.main(self)   

   
    def gameUi(self,FormGame):
        '''
        Cette fonction affiche la fenêtre du jeu ainsi que tous ses élements principaux
        :param formGame : QtGui.QDialog()
        '''

        # Paramétrage de la FORM en elle-même
        FormGame.setObjectName("FormGame")
        FormGame.resize(1220, 690)        
        FormGame.setMinimumSize(QtCore.QSize(1220, 690))
        FormGame.setMaximumSize(QtCore.QSize(1220, 690))           
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(1, 29, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 29, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(64, 64, 64))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(1, 29, 70))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(56, 56, 56))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        FormGame.setPalette(palette)
        icon = QtGui.QIcon()



        #icône
        icon.addPixmap(QtGui.QPixmap("image/pawnR.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormGame.setWindowIcon(icon)



        # on affiche le plateau du jeu et on crée les pions
        self.plateau = QtGui.QLabel(FormGame)
        self.plateau.setGeometry(QtCore.QRect(338, 39, 543, 527))
        self.plateau.setText("")
        self.plateau.setPixmap(QtGui.QPixmap("image/plateauOf.png"))
        self.plateau.setScaledContents(True)
        self.plateau.setObjectName("label")        
            
        listePawns = []

        for couleur in ["G","Y","C","P","B"]:
            for i in range(2,13):
                listePawns.append(couleur+str(i))    
        
        distancePixelH= 403
        distancePixelV = 328
        partieGauche =0
        partieCoul=0
        for pawnC in listePawns:
            self.__dict__[pawnC]=  QtGui.QLabel(FormGame)
            self.__dict__[pawnC].setGeometry(QtCore.QRect(distancePixelH, distancePixelV, 13, 17)) 
            self.__dict__[pawnC].setPixmap(QtGui.QPixmap("image/pawn"+str(pawnC[:1])+".png"))
            self.__dict__[pawnC].setScaledContents(True)
            self.__dict__[pawnC].setObjectName("pawnC")
            self.__dict__[pawnC].hide()

            if partieGauche < 5:
                distancePixelH +=40
                distancePixelV+=35
            else:
                distancePixelH +=40
                distancePixelV-=35


            partieGauche+=1
            partieCoul+=1
            if partieCoul == 11:
                distancePixelH= 403 
                distancePixelV = 328 
                partieCoul= 0
                partieGauche=0

        
        


        # ce label n'a pas d'importance, il ajoute un charme à l'interface
        self.label_player_name = QtGui.QLabel(FormGame)
        self.label_player_name.setGeometry(QtCore.QRect(927, 20, 261, 70))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_player_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_player_name.setFont(font)
        self.label_player_name.setObjectName("label_Tour_j")
        
        
        
        # on affiche le boutton qui va permettre de faire monter les pions qu'on les dés voies sont connues
        self.image_lancer = QtGui.QPushButton(FormGame)
        self.image_lancer.setGeometry(QtCore.QRect(960, 500, 85, 85))
        self.image_lancer.setIconSize(QtCore.QSize(85, 85))       
        self.image_lancer.setObjectName("image_lancer")
        iconLancer = QtGui.QIcon()
        iconLancer.addPixmap(QtGui.QPixmap("image/continue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.image_lancer.setIcon(iconLancer)

        # on affiche le boutton qui va permettre de lancer les dés
        self.image_lancerDe = QtGui.QPushButton(FormGame)
        self.image_lancerDe.setGeometry(QtCore.QRect(1018, 600, 85, 69))
        self.image_lancerDe.setIconSize(QtCore.QSize(85, 85))        
        self.image_lancerDe.setObjectName("image_lancer")
        iconLancerDe = QtGui.QIcon()
        iconLancerDe.addPixmap(QtGui.QPixmap("image/proba.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.image_lancerDe.setIcon(iconLancerDe)

        # on affiche le boutton qui va permettre d'arréter le tour
        self.imageStop = QtGui.QPushButton(FormGame)
        self.imageStop.setGeometry(QtCore.QRect(1075, 500, 85, 85))        
        self.imageStop.setIconSize(QtCore.QSize(85, 85))        
        self.imageStop.setObjectName("imageStop")
        iconStop = QtGui.QIcon()
        iconStop.addPixmap(QtGui.QPixmap("image/Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.imageStop.setIcon(iconStop)


        # on pointe les différentes fonctions pour chaque boutton
        QtCore.QObject.connect(self.image_lancer, QtCore.SIGNAL("clicked()"), self.playgame)
        QtCore.QObject.connect(self.imageStop, QtCore.SIGNAL("clicked()"), self.STOPgame)
        QtCore.QObject.connect(self.image_lancerDe, QtCore.SIGNAL("clicked()"), self.continueGame)
        
        # On affiche les deux lignes verticales noirs de l'interface
        self.ligneN1 = QtGui.QLabel(FormGame)
        self.ligneN1.setGeometry(QtCore.QRect(320, -20, 10, 761))
        self.ligneN1.setText("")
        self.ligneN1.setPixmap(QtGui.QPixmap("image/carre-noir.png"))
        self.ligneN1.setObjectName("ligneN1")
        self.ligneN2 = QtGui.QLabel(FormGame)
        self.ligneN2.setGeometry(QtCore.QRect(890, -30, 10, 761))
        self.ligneN2.setText("")
        self.ligneN2.setPixmap(QtGui.QPixmap("image/carre-noir.png"))
        self.ligneN2.setObjectName("ligneN2")


        # On créé le label qui affiche l'état du jeu
        self.label_state_game = QtGui.QLabel(FormGame)
        self.label_state_game.setGeometry(QtCore.QRect(19, -30, 331, 181))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setItalic(False)
        font.setUnderline(True)
        self.label_state_game.setFont(font)
        self.label_state_game.setObjectName("label_state_game")
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_state_game.setPalette(palette)
        self.label_state_game.setFont(font)
        self.label_state_game.setObjectName("label_state_game")

        
        # On crée les dés qui seront affichés sur le board, pour une plus grande intéractivité 
        self.choix1_1 = QtGui.QLabel(FormGame)
        self.choix1_1.setGeometry(QtCore.QRect(970, 140, 41, 41))
        self.choix1_1.setPixmap(QtGui.QPixmap("image/de6.gif"))
        self.choix1_1.setScaledContents(True)
        self.choix1_1.setObjectName("choix1_1")
        self.choix1_2 = QtGui.QLabel(FormGame)
        self.choix1_2.setGeometry(QtCore.QRect(1020, 140, 41, 41))
        self.choix1_2.setPixmap(QtGui.QPixmap("image/de5.gif"))
        self.choix1_2.setScaledContents(True)
        self.choix1_2.setObjectName("choix1_2")
        self.choix1_3 = QtGui.QLabel(FormGame)
        self.choix1_3.setGeometry(QtCore.QRect(1110, 140, 41, 41))
        self.choix1_3.setPixmap(QtGui.QPixmap("image/de4.gif"))
        self.choix1_3.setScaledContents(True)
        self.choix1_3.setObjectName("choix1_3")
        self.choix1_4 = QtGui.QLabel(FormGame)
        self.choix1_4.setGeometry(QtCore.QRect(1160, 140, 41, 41))
        self.choix1_4.setPixmap(QtGui.QPixmap("image/de3.gif"))
        self.choix1_4.setScaledContents(True)
        self.choix1_4.setObjectName("choix1_4")
        self.choix2_2 = QtGui.QLabel(FormGame)
        self.choix2_2.setGeometry(QtCore.QRect(990, 200, 41, 41))
        self.choix2_2.setPixmap(QtGui.QPixmap("image/de5.gif"))
        self.choix2_2.setScaledContents(True)
        self.choix2_2.setObjectName("choix2_2")
        self.choix2_4 = QtGui.QLabel(FormGame)
        self.choix2_4.setGeometry(QtCore.QRect(1130, 200, 41, 41))
        self.choix2_4.setPixmap(QtGui.QPixmap("image/de3.gif"))
        self.choix2_4.setScaledContents(True)
        self.choix2_4.setObjectName("choix2_4")
        self.choix2_1 = QtGui.QLabel(FormGame)
        self.choix2_1.setGeometry(QtCore.QRect(940, 200, 41, 41))
        self.choix2_1.setPixmap(QtGui.QPixmap("image/de6.gif"))
        self.choix2_1.setScaledContents(True)
        self.choix2_1.setObjectName("choix2_1")
        self.choix2_3 = QtGui.QLabel(FormGame)
        self.choix2_3.setGeometry(QtCore.QRect(1080, 200, 41, 41))
        self.choix2_3.setPixmap(QtGui.QPixmap("image/de4.gif"))
        self.choix2_3.setScaledContents(True)
        self.choix2_3.setObjectName("choix2_3")
        self.choix3_4 = QtGui.QLabel(FormGame)
        self.choix3_4.setGeometry(QtCore.QRect(1160, 260, 41, 41))
        self.choix3_4.setPixmap(QtGui.QPixmap("image/de3.gif"))
        self.choix3_4.setScaledContents(True)
        self.choix3_4.setObjectName("choix3_4")
        self.choix3_3 = QtGui.QLabel(FormGame)
        self.choix3_3.setGeometry(QtCore.QRect(1110, 260, 41, 41))
        self.choix3_3.setPixmap(QtGui.QPixmap("image/de4.gif"))
        self.choix3_3.setScaledContents(True)
        self.choix3_3.setObjectName("choix3_3")
        self.choix3_1 = QtGui.QLabel(FormGame)
        self.choix3_1.setGeometry(QtCore.QRect(970, 260, 41, 41))
        self.choix3_1.setPixmap(QtGui.QPixmap("image/de6.gif"))
        self.choix3_1.setScaledContents(True)
        self.choix3_1.setObjectName("choix3_1")
        self.choix3_2 = QtGui.QLabel(FormGame)
        self.choix3_2.setGeometry(QtCore.QRect(1020, 260, 41, 41))
        self.choix3_2.setPixmap(QtGui.QPixmap("image/de5.gif"))
        self.choix3_2.setScaledContents(True)
        self.choix3_2.setObjectName("choix3_2")

        #on créé des checkbox qui symboliseront les couples de voies possibles
        self.groupBox = QtGui.QGroupBox(FormGame)
        self.groupBox.setGeometry(QtCore.QRect(950, 320, 241, 131))
        self.groupBox.setObjectName("groupBox")
        self.routes1 = QtGui.QRadioButton(self.groupBox)
        self.routes1.setGeometry(QtCore.QRect(10, 40, 101, 22))
        self.routes1.setObjectName("radioButton")
        self.routes1.setChecked(True)
        self.routes2 = QtGui.QRadioButton(self.groupBox)
        self.routes2.setGeometry(QtCore.QRect(10, 70, 101, 22))
        self.routes2.setObjectName("radioButton_2")
        self.routes3 = QtGui.QRadioButton(self.groupBox)
        self.routes3.setGeometry(QtCore.QRect(10, 100, 101, 22))
        self.routes3.setObjectName("radioButton_3")
        # On crée des éléments en plus dans l'interface, "&" entre les dés affichés
        self.et1 = QtGui.QLabel(FormGame)
        self.et1.setGeometry(QtCore.QRect(1080, 140, 31, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)

        self.et1.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.et1.setFont(font)
        self.et1.setObjectName("et1")
        self.et1_2 = QtGui.QLabel(FormGame)
        self.et1_2.setGeometry(QtCore.QRect(1050, 200, 31, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.et1_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.et1_2.setFont(font)
        self.et1_2.setObjectName("et1_2")
        self.et1_3 = QtGui.QLabel(FormGame)
        self.et1_3.setGeometry(QtCore.QRect(1080, 260, 31, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.et1_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.et1_3.setFont(font)
        self.et1_3.setObjectName("et1_3")


        # dans cette partie on affiche : le nombre de joueurs, les routes libres ou conquises
        # le type du joueur, le logo du joueur...
        self.Nb_players = QtGui.QLabel(FormGame)
        self.Nb_players.setGeometry(QtCore.QRect(20, 400, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Nb_players.setFont(font)
        self.Nb_players.setObjectName("Nb_players")
        
        self.label_player_t = QtGui.QLabel(FormGame)
        self.label_player_t.setGeometry(QtCore.QRect(10, 140, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label_player_t.setFont(font)
        self.label_player_t.setObjectName("label_player_t")
        self.routes_free = QtGui.QLabel(FormGame)
        self.routes_free.setGeometry(QtCore.QRect(20, 440, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.routes_free.setFont(font)
        self.routes_free.setObjectName("routes_free")
        
        self.Conquered_routes = QtGui.QLabel(FormGame)
        self.Conquered_routes.setGeometry(QtCore.QRect(20, 485, 230, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Conquered_routes.setFont(font)
        self.Conquered_routes.setObjectName("Conquered_routes")
        
        self.logo_joueur_t = QtGui.QLabel(FormGame)
        self.logo_joueur_t.setGeometry(QtCore.QRect(120, 150, 21, 31))
        self.logo_joueur_t.setText("")
        self.logo_joueur_t.setPixmap(QtGui.QPixmap("image/pawnP.png"))
        self.logo_joueur_t.setScaledContents(True)
        self.logo_joueur_t.setObjectName("logo_joueur_t")
        self.player_Nb_pawns = QtGui.QLabel(FormGame)
        self.player_Nb_pawns.setGeometry(QtCore.QRect(20, 200, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.player_Nb_pawns.setFont(font)
        self.player_Nb_pawns.setObjectName("player_Nb_pawns")
        self.player_Nb_routes = QtGui.QLabel(FormGame)
        self.player_Nb_routes.setGeometry(QtCore.QRect(20, 230, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.player_Nb_routes.setFont(font)
        self.player_Nb_routes.setObjectName("player_Nb_routes")
        self.player_Nb_routes_2 = QtGui.QLabel(FormGame)
        self.player_Nb_routes_2.setGeometry(QtCore.QRect(20, 260, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.player_Nb_routes_2.setFont(font)
        self.player_Nb_routes_2.setObjectName("player_Nb_routes_2")

        #On affiche le titre du jeu
        self.titre = QtGui.QLabel(FormGame)
        self.titre.setGeometry(QtCore.QRect(465, 560, 301, 61))
        font = QtGui.QFont()
        font.setPointSize(43)
        font.setBold(True)
        font.setWeight(75)
        self.titre.setFont(font)
        self.titre.setObjectName("label_5")

        # On affiche la devise du jeu
        self.devise = QtGui.QLabel(FormGame)
        self.devise.setGeometry(QtCore.QRect(500, 640, 271, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.devise.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.devise.setFont(font)
        self.devise.setObjectName("label_6")


        # On affiche qui a gagné
        self.label_winner = QtGui.QLabel(FormGame)
        self.label_winner.setGeometry(QtCore.QRect(20, 580, 230, 71))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(133, 133, 133))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_winner.setPalette(palette)
        self.label_winner.hide()
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_winner.setFont(font)
        self.label_winner.setObjectName("label_winner")
        self.image_winner = QtGui.QLabel(FormGame)
        self.image_winner.setGeometry(QtCore.QRect(243, 577, 30, 60))
        self.image_winner.setText("")
        self.image_winner.setObjectName("image_winner")
        self.image_winner.setScaledContents(True)


        #on désactive de base les bouttons :  image_lancerDe et imageStop au début du jeu
        self.image_lancerDe.setEnabled(False)
        self.imageStop.setEnabled(False)    

        #Tous les strings affichés sur le FORM, ré-éddition facile
        FormGame.setWindowTitle("Can\'t Stop")
        self.label_player_name.setText("FormGame")        
        self.label_state_game.setText("State of board game")
        self.groupBox.setTitle("Choice your routes")
        self.routes1.setText("Routes 6")
        self.routes2.setText("Routes 10")
        self.routes3.setText("Routes 9")
        self.et1.setText("&")
        self.et1_2.setText("&")
        self.et1_3.setText("&")
        self.Nb_players.setText("Number of players :  4")        
        self.label_player_t.setText("Player : ")
        self.routes_free.setText("Routes free :  6")        
        self.Conquered_routes.setText("Conquered routes :  6")        
        self.player_Nb_pawns.setText("* The player has 7 pawns on the board")
        self.player_Nb_routes.setText("* The player hold 2 routes")
        self.player_Nb_routes_2.setText("* Type of player : IA")
        self.titre.setText("Can\'t stop ")
        self.devise.setText("the Sid Sackson classic")
        self.label_winner.setText("WINNER !")

        QtCore.QMetaObject.connectSlotsByName(FormGame)

        

   


        
    def move_Bonze_Paws_Board(self,nom,distancePixelH,distancePixelV):
        
        """
        Cette fonction permet de déplacer les bonzes ou les pions sur l'interface
        :param nom : string
	    :param distancePixelH: int
	    :param distancePixelV: int
        """
        
        nom = nom.replace(" ","")
        self.__dict__[nom].show()
        self.__dict__[nom].setGeometry(QtCore.QRect(distancePixelH, distancePixelV, 13, 17))



    def playgame(self):
    	
        self.jeu.waitObjet.gestion_time_stop()
        self.image_lancerDe.setEnabled(True)
        self.imageStop.setEnabled(True)
        self.image_lancer.setEnabled(False)
        for x in range(1,4):
        	self.__dict__["routes"+str(x)].setEnabled(False)

        '''
        Cette fonction permet de lancer le jeu quand le checkbox des voies est cliqué 
        '''

    def STOPgame(self):
    	
        self.etat = True
        self.jeu.waitObjet.gestion_time_stop()
        self.image_lancerDe.setEnabled(False)
        self.imageStop.setEnabled(False)
        self.image_lancer.setEnabled(True)
        for x in range(1,4):
        	self.__dict__["routes"+str(x)].setEnabled(True)
        """
        Cette fonction permet d'arréter le tour actuel
        """

    def continueGame(self):
        self.etat = False
        self.jeu.waitObjet.gestion_time_stop()
        self.image_lancerDe.setEnabled(False)
        self.imageStop.setEnabled(False)
        self.image_lancer.setEnabled(True)
        for i in range(1,4):
        	self.__dict__["routes"+str(i)].setEnabled(True)
        """
        Cette fonction permet de relancer les dés
        """

    def warningBox(self):
    	
        QtGui.QMessageBox.warning(self.warningBoxFrom, " Message " ," there is a available route, retry ! " )
        for i in range(1,4):
        	self.__dict__["routes"+str(i)].setEnabled(True)
        """
        Cette fonction permet d'afficher un message box symbolisant qu'il a une voie disponible
        et donc de réassayer
        """
    def move_center(self,form):
    	
        ecran_resolution = QtGui.QDesktopWidget()
        ecran_resolution.screenGeometry()
        width = (ecran_resolution.width()/2)
        height = (ecran_resolution.height() / 2)
        width_frame_local = (form.frameSize().width() / 2)
        height_frame_local = (form.frameSize().height() / 2)        
        form.move( width - width_frame_local, height - height_frame_local)
        '''
    	Cette fonction permet de centrer la fenêtre
    	:param form : QtGui.QWidjet
    	'''
