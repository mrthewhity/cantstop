import os
from joueur import *
from GUI import *
from wait import *


class Jeu():


	def __init__(self, listeJoueur, IA_level):
		'''
		Cette fonction initalise la classe Jeu
		:param listeJoueur : liste
		'''
		
		self.HEIGHT = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}		
		
		self.blocked_routes=[]
		self.listeJoueur = listeJoueur		
		self.wait_Form =QtGui.QDialog()
		self.waitObjet = wait()
		self.waitObjet.init(self.wait_Form)
		self.players = Joueur(listeJoueur,IA_level,self.waitObjet)
		
		

		

	def reset_bonzes(self):
		'''
		Cette fonction permet de reset le dico bonzes et de nettoyer le board des bonzes
		'''
		
		for vert,hori in self.players.bonzes.items(): 
			couleur="B"
			
			vert = int(vert)
			self.Gui.__dict__["B"+str(vert)].hide()		
		

		self.players.bonzes = {}



	def throw_dice(self):
	    '''
	    Renvoie un tuple contenant 4 entiers entre 1 et 6
	    :return: tuple(int,int,int,int) 
	    '''
	    return (randint(1 ,6) ,randint(1 ,6) ,randint(1 ,6) ,randint(1 ,6))
	
	

	
	def F5_dice(self,res_dice):
		'''
		Cette fonction permet d'afficher les dés générer par le lancement de ceux-ci
		:param res_dice : tuple
		'''


		self.Gui.choix1_1.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[0])+".gif"))
		self.Gui.choix1_2.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[1])+".gif"))
		self.Gui.choix1_3.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[2])+".gif"))
		self.Gui.choix1_4.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[3])+".gif"))

		self.Gui.choix2_1.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[0])+".gif"))
		self.Gui.choix2_2.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[2])+".gif"))
		self.Gui.choix2_3.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[1])+".gif"))
		self.Gui.choix2_4.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[3])+".gif"))

		self.Gui.choix3_1.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[0])+".gif"))
		self.Gui.choix3_2.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[3])+".gif"))
		self.Gui.choix3_3.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[1])+".gif"))
		self.Gui.choix3_4.setPixmap(QtGui.QPixmap("image/de"+str(res_dice[2])+".gif"))
	
		self.Gui.groupBox.setTitle("Choose 2 routes")
		self.Gui.routes1.setText(str(res_dice[0]+res_dice[1])+" and " +str(res_dice[2]+res_dice[3]))
		self.Gui.routes2.setText(str(res_dice[0]+res_dice[2])+" and " +str(res_dice[1]+res_dice[3]))
		self.Gui.routes3.setText(str(res_dice[0]+res_dice[3])+" and " +str(res_dice[1]+res_dice[2]))
		


	

	def F5_board(self,player_id):

		'''
		Cette fonction permet d'actualiser la fenêtre en modifiant les informations de joueurs
		:parma player_id : int
		'''

		nb_route_hold =0
		for key,value in self.HEIGHT.items():
			if key in self.players.pawns[player_id] and  self.players.pawns[player_id][key]== value:
				nb_route_hold+=1

		self.Gui.label_player_name.setText( self.Gui.pseudo_joueur[player_id])
		self.Gui.logo_joueur_t.setPixmap(QtGui.QPixmap("image/pawn"  +  str(self.players.__dict__["Color_Player"+str(player_id)])  +  ".png"))
		self.Gui.player_Nb_pawns.setText("* The player has "+str(len(self.players.pawns[player_id]))+" pawns on the board")
		self.Gui.routes_free.setText("Routes free :  "+str(11- len(set(self.blocked_routes))))
		self.Gui.player_Nb_routes.setText("* The player hold " +str( nb_route_hold )+ " routes")
		self.Gui.Conquered_routes.setText("Conquered routes :  "+str(len(set(self.blocked_routes))))
		self.Gui.Nb_players.setText("Number of players :  "+str(len(self.listeJoueur)))
		self.Gui.player_Nb_routes_2.setText("* Type of player : "+ str(self.players.__dict__["Player"+str(player_id)]))


	def is_blocked(self,res_dice):
	    '''
	    Verifie si un joueur peut après avoir fait un lancement de dés, continuer son tour de jeu.
	    :param res_dice: tuple(int,int,int,int
	    :return: boolean
	    '''
	    bonzes=self.players.bonzes
	    blocked_routes = self.blocked_routes
	    flag=False
	    VarPossible1= res_dice[0]+res_dice[1], res_dice[2]+res_dice[3]
	    VarPossible2= res_dice[0]+res_dice[2], res_dice[1]+res_dice[3]
	    VarPossible3= res_dice[0]+res_dice[3], res_dice[1]+res_dice[2]
	    test1,test2,test3=False,False,False
	    blocked_routesLocale =  self.blocked_routes

	    blocked_routesLocale.append(13)

	    

	    if (VarPossible1[0] in blocked_routes and VarPossible1[1]in blocked_routes )or (VarPossible1[0]in blocked_routes and not(VarPossible1[1] in bonzes ) )or (VarPossible1[1]in blocked_routes and not(VarPossible1[0] in bonzes ))or ((not(VarPossible1[0] in bonzes) and not(VarPossible1[1] in bonzes))  and not(len(bonzes)<3)) \
	    or self.is_blocked_addon(VarPossible1[1],VarPossible1[0]) or not(VarPossible1[0] in bonzes) and VarPossible1[1]in blocked_routes or (not(VarPossible1[1] in bonzes) and VarPossible1[0]in blocked_routes):
	        test1=True
	        
	    if (VarPossible2[0]in blocked_routes and VarPossible2[1]in blocked_routes )or (VarPossible2[0]in blocked_routes and not(VarPossible2[1] in bonzes )) or (VarPossible2[1]in blocked_routes and not(VarPossible2[0] in bonzes ))or ((not(VarPossible2[0] in bonzes) and not(VarPossible2[1] in bonzes))  and not(len(bonzes)<3)) \
	    or self.is_blocked_addon(VarPossible2[1],VarPossible2[0]) or not(VarPossible2[0] in bonzes) and VarPossible2[1]in blocked_routes or (not(VarPossible2[1] in bonzes) and VarPossible2[0]in blocked_routes):
	        test2=True
	        
	    if (VarPossible3[0]in blocked_routes and VarPossible3[1] in blocked_routes) or (VarPossible3[0]in blocked_routes and not(VarPossible3[1] in bonzes ) )or (VarPossible3[1]in blocked_routes and not(VarPossible3[0] in bonzes ))or ((not(VarPossible3[0] in bonzes) and not(VarPossible3[1] in bonzes)) and not(len(bonzes)<3) ) \
	    or self.is_blocked_addon(VarPossible3[1],VarPossible3[0])or not(VarPossible3[0] in bonzes) and VarPossible3[1]in blocked_routes or (not(VarPossible3[1] in bonzes) and VarPossible3[0]in blocked_routes):
	        test3=True
	        
	    if test1 ==True and test2 ==True and test3 == True:
	    	flag=True
	    else:
	    	
	    	test1,test2,test3 =False,False,False

	   

	    blocked_routesLocale.remove(13)

	    return flag 


	def is_blocked_addon(self,var1,var2):
	    '''
	    Cette fonction teste des cas assez spécifique pour la fonction isblocked.
	    :param var1: int
	    :param var2: int
	    :return: boolean
	    '''
	    res=False
	    if var1 in self.players.bonzes and self.players.bonzes[var1]==self.HEIGHT[var1] and not(var2 in self.players.bonzes):
	        res =True
	    if var2 in self.players.bonzes and self.players.bonzes[var2]==self.HEIGHT[var2] and not(var1 in self.players.bonzes):
	        res =True
	    if var2 in self.players.bonzes and self.players.bonzes[var2]==self.HEIGHT[var2] and var1 in self.players.bonzes and self.players.bonzes[var1]==self.HEIGHT[var1]:
	        res=True

	    
	    return res




	

	def move_bonzes(self,routes,player_id,AI):
	    '''
	    Avance les bonzes dans les routes
	    :param routes: tuple(int,int)
	    :param player_id: int
	    :param AI: bool
	    :return: boolean
	    '''
	    # Cas ou un choix est possible pour placer le dernier bonze
	    	    
	    if len(self.players.bonzes) == 2 and routes[0] not in self.players.bonzes.keys() and routes[1] not in self.players.bonzes.keys() and routes[0]!=routes[1]:
	        choice = self.players.choose_route_human(routes) if AI == False else self.players.choose_route_AI(routes,player_id)
	      
	        res = self.move_one_bonze(routes[choice-1],player_id)	        

	    else:

	        res = self.move_one_bonze(routes[0],player_id)	        
	       
	        res = self.move_one_bonze(routes[1],player_id) or res
	            
	    return res



	def move_one_bonze(self,v,player_id):
	    '''
	    Avance un bonze ou le place dans la route v
	    :param v: int
	    :param player_id: int
	    :return: boolean
	    '''
	    
	    v = int(v)
	    res = False
	    # Cas où un bonze peut être placé
	    if v not in self.players.bonzes.keys() and len(self.players.bonzes) < 3 and not(v in self.blocked_routes):
	        res = True        
	        n=1 # Nombre de case que le bonze devra monter pour être dans une case libre (init à 1)
	        dico= self.players.pawns[player_id]

	        if v in dico:
	            n=dico[v]

	        if v in self.players.pawns[player_id]:
	            self.players.bonzes[v] = dico[v]
	            
	            for fourIteration in range(4):
	                n = self.placeBonze_correctly_notin_voies(v,n)            
	            
	            self.players.bonzes[v] = int(n)    
           
	        else:
	            for four in range(4):
	                n = self.placeBonze_correctly_notin_voies(v,n)          
	            
	            self.players.bonzes[v] = int(n)          
	           

	    # Cas où un bonze peut être avancé

	    elif v in self.players.bonzes.keys() and self.players.bonzes[v] < self.HEIGHT[v] and not(v in self.blocked_routes):

	    	
	    	res = True
	    	dico= self.players.pawns[player_id]
	    	n= 1
	    	if v in dico:
	    		n=dico[v]
	    	flag=True
	    	if v in dico and not(v in self.players.bonzes):
	    		self.players.bonzes[v] = dico[v]
	    		while flag==True:
	    			n,flag = self.placeBonze_correctly_in_voies(v,n)
	    		self.players.bonzes[v] = int(n )
	    		
	    		
	    	else:
	    		
	    		n=1
	    		while flag==True:
	    			n,flag = self.placeBonze_correctly_in_voies(v,n)
	    		self.players.bonzes[v] +=int(n)  
	            
	    return res

	

	def delete_Pawns(self,player_id):
	    '''
	    Cette fonction ajoute dans une liste toutes les voies bloquées,
	    et supprime les pions ou bonzes qui seraient dans une de celle-ci.
	    :param player_id: int
	    '''

	    for voieLimite , hauteurLimite in self.HEIGHT.items():
	        for voiePawn, hauteurPawn in (self.players.pawns[player_id]).items():
	            if voieLimite==voiePawn and hauteurLimite==hauteurPawn:
	               	self.blocked_routes.append(voieLimite)

	    ID=0
	    for pawn in self.players.pawns:
	        to_delete = []
	        for keys, values in pawn.items():
	            if keys in self.blocked_routes and values < self.HEIGHT[keys]:
	                to_delete.append(keys)


	        for voies in to_delete:
	        	
	        	self.Gui.__dict__[str(self.players.__dict__["Color_Player"+str(ID)])+str(voies)].hide()	

	        	del pawn[voies]

	       	ID+=1
	        


	def placeBonze_correctly_in_voies(self,v,n):
	    '''
	    Place le bonze correctement à la première place libre si v est dans bonzes,
	    le bonze montra de "n" unité.
	    :param v: int
	    :param n: int
	    :return: tuple(int,bool)
	    '''
	    flag =False        
	    if v in self.players.pawns[0] and (self.players.pawns[0][v]) == (self.players.bonzes[v]+n) :        
	        flag =True
	        n+=1
	    elif v in self.players.pawns[1] and (self.players.pawns[1][v]) == (self.players.bonzes[v]+n):        
	        flag =True
	        n+=1

	    elif v in self.players.pawns[2] and (self.players.pawns[2][v]) == (self.players.bonzes[v]+n) :        
	        flag =True
	        n+=1

	    elif v in self.players.pawns[3] and (self.players.pawns[3][v]) == (self.players.bonzes[v]+n):        
	        flag =True
	        n+=1

	    return n,flag

	def placeBonze_correctly_notin_voies(self,v,n):
	    '''
	    Place le bonze correctement à la première place libre si v n'est pas dans bonzes,
	    le bonze montra de "n" unité.
	    :param v: int
	    :param n: int
	    :return: int 
	    '''
	    
	    if v in self.players.pawns[0] and (self.players.pawns[0][v]) == n:
	        n+=1
	    elif v in self.players.pawns[1] and (self.players.pawns[1][v]) == n:
	        n+=1

	    elif v in self.players.pawns[2] and (self.players.pawns[2][v]) == n:
	        n+=1

	    elif v in self.players.pawns[3] and (self.players.pawns[3][v]) == n:
	        n+=1

	    return n

	
	def check_top(self):
	    '''
	    Vérifie si les trois bonzes sont au sommet d'une route.
	    :return: bool
	    '''
	    res = False
	    if len(self.players.bonzes)==3 :
	        res = True
	        for v in self.players.bonzes.keys():
	        	v = int(v)
	        	if v in self.players.bonzes and self.players.bonzes[v]!=self.HEIGHT[v]:
	        		res=False   

	    return  res 

	def check_top_pawns(self,player_id):
	    '''
	    Vérifie si trois pions sont au sommet d'une route.
	    :param player_id: int
	    :return: bool
	    '''
	    pawn=self.players.pawns[player_id]
	    itemsSame = set(self.HEIGHT.items()) & set(pawn.items())
	    val = len(itemsSame)
	    return val>2

	def game_round(self,player_id,AI):
	    '''
	    Premier tour de jeu

	    :param player_id: int
	    :param AI: bool
	    :return: boolean
	    '''
	    self.reset_bonzes()
	    self.F5_board(player_id)
	    
	    
	    flag = False
	    res = False
	    while not flag:
	        res_dice = self.throw_dice()
	        
	        mauvaisLancer = self.is_blocked(res_dice) 
	       
	        flag2=False
	        while not(flag2) and not(mauvaisLancer):
	        	self.F5_dice(res_dice)
	        	if AI==False:
	        		self.Gui.image_lancer.setEnabled(True)
	        		move_bonzesNotAI = self.move_bonzes(self.players.choose_dice_human(res_dice),player_id,AI)
	        		self.affiche_bonzes()
	        		if move_bonzesNotAI==True:
	        			flag2= True
	        		else:
	        			# si une erreur de choix de voies alors MESSAGE BOX s'ouvre
	        			self.Gui.warningBox()
	        			self.Gui.image_lancerDe.setEnabled(False)
	        			self.Gui.imageStop.setEnabled(False)
	        			self.Gui.image_lancer.setEnabled(True)
	        	elif AI==True:
	        		move_bonzesAI = self.move_bonzes(self.players.choose_dice_AI(res_dice,player_id),player_id,AI)
	        		self.affiche_bonzes()
	        		self.waitObjet.attente_IA()
	        		self.Gui.image_lancer.setEnabled(False)
	        		if move_bonzesAI==True:
	        			flag2= True
	                
	        if AI==False and not(mauvaisLancer) and  move_bonzesNotAI or AI==True  and not(mauvaisLancer) and move_bonzesAI :
	           
	            if AI==False and self.players.decide_stop_human():
	                flag = True
	                
	                
	                if self.players.pawns[player_id]=={}:
	                    self.players.pawns[player_id] = self.players.bonzes
	                else:
	                    dico=self.players.pawns[player_id]
	                    self.players.pawns[player_id]= self.melange_dico(dico)
	                
	                
	            if AI==True and self.players.decide_stop_AI(player_id) :
	                flag = True
	                if self.players.pawns[player_id]=={}:

	                    self.players.pawns[player_id] = self.players.bonzes
	                else:
	                    dico=self.players.pawns[player_id]
	                    self.players.pawns[player_id]= self.melange_dico(dico)
	            self.delete_Pawns(player_id)
	            if self.check_top_pawns(player_id):
	                res=True
	                flag=True            
	                
	        
	            
	        else:
	            
	            flag = True
	           
	    return res

	def melange_dico(self,dico):
		'''
		Cette fonction permet de concaténer deux dico
		'''

		for key,value in dico.items():
			if not(key in self.players.bonzes):
				self.players.bonzes[key]=value
		return self.players.bonzes

	def affichePionsGui(self):
		'''
		Cette fonction permet d'afficher les pions sur le plateau
		'''

		ID=0
		for pawns in self.players.pawns:
			for vert_data,hori_data in pawns.items():

				
				couleur=self.players.__dict__["Color_Player"+str(ID)]
			
				
				Coord_H = ((int(vert_data)-2)*40 +403)
				if int(vert_data) <8:
					Coord_V = 328 + ((int(vert_data)-2)*35) -((int(hori_data)-1)*35)
				else:
					Coord_V = 503 - ((int(vert_data)-7)*35) -((int(hori_data)-1) *35)
				self.Gui.move_Bonze_Paws_Board(str(couleur)+str(vert_data),Coord_H,Coord_V)

			ID+=1


	def affiche_bonzes(self):
		'''
		Cette fonction permet d'afficher les bonzes sur le plateu
		'''

		
		for vert_data,hori_data in self.players.bonzes.items(): 
			couleur="B"
			
			Coord_H = ((int(vert_data)-2)*40 +403)
			if int(vert_data) <8:
				Coord_V = 328 + ((int(vert_data)-2)*35) -((int(hori_data)-1)*35)
			else:
				Coord_V = 503 - ((int(vert_data)-7)*35) -((int(hori_data)-1) *35)
			self.Gui.move_Bonze_Paws_Board(str(couleur)+str(vert_data),Coord_H,Coord_V)

		

	def affichage_end_game(self,gagnant):
		'''
		Cette fonction permet de mettre à jour la fenêtre à la fin du jeu
		:param gagant : int
		'''
		self.waitObjet.gestion_time_stop()
		self.F5_board(gagnant)
		self.reset_bonzes()
		self.Gui.label_winner.show()
		self.Gui.image_winner.setPixmap(QtGui.QPixmap("image/pawn"+str(self.players.__dict__["Color_Player"+str(gagnant)])+".png"))
		self.Gui.image_lancer.setEnabled(False)


	def main(self,GUIobjet):
		'''
		cette fonction appelle la boucle principale du jeu
		:param GUIobjet : GUI
		'''

		self.Gui = GUIobjet
		self.players.Gui = GUIobjet
		player_id = 0		
		gagner = False
		while(not gagner):
			

		
			gagner = self.game_round(player_id,self.listeJoueur[player_id])
			player_id_board = player_id +1 if player_id < len(self.listeJoueur)-1 and gagner == False else 0

			self.F5_board(player_id_board)
			self.affichePionsGui()						
			
			gagnant = player_id
			
			
			player_id = player_id +1 if player_id < len(self.listeJoueur)-1 and gagner == False else 0


		self.affichage_end_game(gagnant)
		
		

		
		


