from random import uniform, randint, seed


class Joueur():

	def __init__(self, listeJoueur,IA_level,waitObjet):
		'''
		Cette fonction va initialiser l'objet player, elles possède les attributs, pawns et bonzes
		Elle possède des méthodes qui font intervenir l'utlisateur ou l'IA
		:param listeJoueur : liste
		:param ui : wait
		'''

		

		self.P = 0.2 # probalité que le joueur s'arrête
		self.waitObjet=waitObjet
		self.bonzes = {}
		self.pawns=[{},{},{},{}]
		self.HEIGHT = {2: 3, 3: 5, 4: 7, 5: 9, 6: 11, 7: 13, 8: 11, 9: 9, 10: 7, 11: 5, 12: 3}
		self.proba= {2:1/36, 3:1/18, 4:1/12, 5:1/9, 6:5/36, 7:1/6, 8:5/36,9:1/9,10 : 1/12, 11:1/18,12: 1/36 }
		self.level_AI= [ int(valeur) if type(valeur) == str else valeur for valeur in IA_level ]
	
		color=["P","G","Y","C"]
		for x in range(len(listeJoueur)):
			self.__dict__["Player"+str(x)] = "IA" if listeJoueur[x]==True else "PLAYER"
			self.__dict__["Color_Player"+str(x)] = color[x]
		


		
	def choose_dice_human(self,res_dice):
	    '''
	    Permet de choisir les paires de dés dans res_rice
	    :param res_dice: tuple(int,int,int,int)
	    :param player_id: int
	    :return: tuple(int,int)
	    '''	    
	   
	    self.waitObjet.gestion_time_start()   

	    res = self.getRoutes()

	    return res

	def getRoutes(self):
		'''
		Cette fonction permet de prendre les valeurs des checkboxs cliqués
		par l'utilisateur
		:return : tuple
		'''		

		for x in range(1,4):
			if self.Gui.__dict__["routes"+str(x)].isChecked():

				save = x

		label_Route = self.Gui.__dict__["routes"+str(save)].text()
		couple = label_Route.split("and")


		return (int(couple[0]), int(couple[1]))

	def choose_route_human(self,available_routes):
	    '''
	    Cette fonction demande au joueur où le dernier bonze doit être placé.
	    :param available_routes: tuple(int,int)
	    return: int

	    ''' 

	    for i in range(1,4):
        	self.Gui.__dict__["routes"+str(i)].setEnabled(True)
	    self.Gui.routes1.setText("Routes "+str(available_routes[0]))
	    self.Gui.routes1.setChecked(True)
	    self.Gui.routes2.setText("Routes "+str(available_routes[1]))
	    self.Gui.groupBox.setTitle("Choose 1 route")	   
	    self.Gui.__dict__["routes"+str(3)].hide()
	    self.Gui.image_lancerDe.setEnabled(False)
	    self.Gui.imageStop.setEnabled(False)
	    self.Gui.image_lancer.setEnabled(True)

	    self.waitObjet.gestion_time_start()	    

	    self.Gui.groupBox.setTitle("Throw dice or stop right now !")
	    
	    self.Gui.__dict__["routes"+str(3)].show()

	    for x in range(1,4):
	    	self.Gui.__dict__["routes"+str(x)].setText("")

	    

	    return self.get_One_routes()


	def get_One_routes(self):
		'''
		Cette fonction permet de prendre la valeur du checkbox cliqué par l'utilisateur
		:return : int
		'''

		for x in range(1,3):
                        
			if self.Gui.__dict__["routes"+str(x)].isChecked():
				save = x

		self.Gui.routes1.setChecked(True)

		return save


	def decide_stop_human(self):
	    '''
	    Cette fonction demande au joueur si il veut continuer.
	    return:  boolean

	    '''	    
	    self.waitObjet.gestion_time_start()

	    return self.Gui.etat


	def bonzes_not_top(self,voies):
		'''
		Cette fonction vérifie si un bonze est à une hauteur max d'une voie
		:param voies: int
		:return boolean:
		'''
		flag =True
		for x in self.pawns:
			
			if voies in x and x[voies]==self.HEIGHT[voies]:
				flag=False


		return flag	

	def bonzes_top_and_in_bonzes(self,v1,v2):
		'''
		Si le joueur à dans un dés une voie qui serait la même qu'un bonze qui serait tout à fait au-dessus d'une voie
		il ne pourrait pas le jouer donc le score de cette voie vaut 0
		:param v1 : int
		:param v2 : int
		:return boolean:
		'''

		flag = False
		if (len(self.bonzes)!=3 and not( v1 in self.bonzes) and self.bonzes_not_top(v1)) or (len(self.bonzes)!=3  and not( v2 in self.bonzes) and self.bonzes_not_top(v2))\
		or v1 in self.bonzes and not( self.bonzes[v1] == self.HEIGHT[v1]) or v2 in self.bonzes and not( self.bonzes[v2] == self.HEIGHT[v2]) :
			flag =True			

		return flag

	def choose_dice_AI(self,res_dice, player_id):
	    '''
	    Cette fonction choisi deux paires de dés pour le joueur AI en fonction d'une certaine difficulté
	    :param res_dice: tuple(int,int,int,int)
	    return: tuple(int, int)

	    '''

	    # on calcule les différentes possibilités de combinaisons
	    combi_1 = res_dice[0]+res_dice[1], res_dice[2]+res_dice[3]
	    combi_2 = res_dice[0]+res_dice[2], res_dice[1]+res_dice[3]
	    combi_3 = res_dice[0]+res_dice[3], res_dice[1]+res_dice[2]
	    

	    if self.level_AI[player_id]==1:
	    	
	    	choice = self.method_AI_random(res_dice)

	    elif self.level_AI[player_id]==2:
	    	score = self.method_AI_det_1(player_id)
	    	listeScore =[score[combi_1[0]] + score[combi_1[1]], score[combi_2[0]] + score[combi_2[1]], score[combi_3[0]] + score[combi_3[1]]]
	    	choice = self.method_AI_non_det_1(listeScore, combi_1,combi_2,combi_3)
	    	


	    elif self.level_AI[player_id] ==3 or self.level_AI[player_id] ==4:


		    # On calcule le score pour chaque voie | méthode déterministe 1 
		    score = self.method_AI_det_1(player_id)

		    if self.level_AI[player_id] == 3:
		    	
		    	score2 = self.method_AI_det_2(player_id) # On calcule le score pour chaque voie | méthode déterministe 2

		    	scoreSomme={}  
		    	for x in score:  # On calcule la somme des deux méthodes  | S1(v) + S2(v)
		    		scoreSomme[x] = score[x]+score2[x]

		    else:
		    	scoreSomme=score

		    
		    # on additione les scores des deux voies

		    listeScore =[scoreSomme[combi_1[0]] + scoreSomme[combi_1[1]], scoreSomme[combi_2[0]] + scoreSomme[combi_2[1]], scoreSomme[combi_3[0]] + scoreSomme[combi_3[1]]]
		   
		   	

		    # ici on va mettre à 0 les scores qui sont liés à des voies non présentes dans les bonzes    
		    	
		    listeScore[0] = 0 if not(self.bonzes_not_top(combi_1[0])) and  not(combi_1[0] in self.bonzes and combi_1[1] in self.bonzes) \
		    		   and not(self.bonzes_not_top(combi_1[1])) and not((combi_1[0] in self.bonzes or combi_1[1] in self.bonzes)) else listeScore[0]

		    listeScore[1] = 0 if not(self.bonzes_not_top(combi_2[0])) and not(combi_2[0] in self.bonzes and combi_2[1] in self.bonzes)  \
		    		   and not(self.bonzes_not_top(combi_2[1]))   and not((combi_2[0] in self.bonzes or combi_2[1] in self.bonzes))  else listeScore[1]

		    listeScore[2] = 0 if not(self.bonzes_not_top(combi_3[0])) and not(combi_3[0] in self.bonzes and combi_3[1] in self.bonzes)   \
		    		   and not(self.bonzes_not_top(combi_3[1]))  and not((combi_3[0] in self.bonzes or combi_3[1] in self.bonzes))  else listeScore[2]
		    
		    if len(self.bonzes)>1 :

			    # On va vérifier qu'un des bonze n'est pas tout au dessus d'une voie, si oui on met le score à 0
			    
			    listeScore[0] = listeScore[0] if combi_1[0] in self.bonzes and not( self.bonzes[combi_1[0]] == self.HEIGHT[combi_1[0]]) or \
			    				combi_1[1] in self.bonzes and not( self.bonzes[combi_1[1]] == self.HEIGHT[combi_1[1]]) \
			    				or self.bonzes_top_and_in_bonzes(combi_1[0],combi_1[1])			else 0

			    listeScore[1] = listeScore[1] if combi_2[0] in self.bonzes and not( self.bonzes[combi_2[0]] == self.HEIGHT[combi_2[0]]) or \
			    				combi_2[1] in self.bonzes and not( self.bonzes[combi_2[1]] == self.HEIGHT[combi_2[1]]) \
			    				or self.bonzes_top_and_in_bonzes(combi_2[0],combi_2[1]) else 0

			    listeScore[2] = listeScore[2] if combi_3[0] in self.bonzes and not( self.bonzes[combi_3[0]] == self.HEIGHT[combi_3[0]]) or \
			    				combi_3[1] in self.bonzes and not( self.bonzes[combi_3[1]] == self.HEIGHT[combi_3[1]]) \
			    				or self.bonzes_top_and_in_bonzes(combi_3[0],combi_3[1]) else 0


			
			# On regarde qu'elle est le meilleur score
		    if max(listeScore) == listeScore[0]:
		    	choice = combi_1
		    		
		    	
		    elif max(listeScore) == listeScore[1] :
		    	choice = combi_2		    		
		    	
		    else:
		    	
		    	choice = combi_3
	    	
	    

		    self.Gui.groupBox.setTitle("IA choose route")	    
		    
		    self.Gui.__dict__["routes"+str(randint(1,3))].setChecked(True)
		  

        
	    return  choice

	def choose_route_AI(self,available_routes,player_id):
	    '''
	    Cette fonction decide quelle route va prendre l'AI en focntion d'une certaine difficulté
	    return: int

	    '''
	    

	    if self.level_AI[player_id]==1 or self.level_AI[player_id]==2:
	    	# si le niveau de difficulté est de 1 ou 2, on fait un random
	    	choice= randint(1,2)

	    else:

	    	
		    # On calcule le score pour chaque voie | méthode déterministe 1 
		    score = self.method_AI_det_1(player_id)

		    if self.level_AI[player_id] == 3:
		    	
		    	score2 = self.method_AI_det_2(player_id) # On calcule le score pour chaque voie | méthode déterministe 2

		    	scoreSomme={}  
		    	for x in score:  # On calcule la somme des deux méthodes  | S1(v) + S2(v)
		    		scoreSomme[x] = score[x]+score2[x]

		    else:
		    	scoreSomme=score
		    listeScore =[scoreSomme[available_routes[0]],scoreSomme[available_routes[1]]]
		   

		    # On mettrai à 0 les scores des mauvaises voies
		    if not(self.bonzes_not_top(available_routes[0])):
		    	listeScore[0] = 0    	

		    if not(self.bonzes_not_top(available_routes[1])):
		    	listeScore[1] = 0   	

	 		#On choisi la voie qui a le meilleur score
		    if max(listeScore) == listeScore[0]:
		    	choice =1
		    	
		    else:
		   		choice = 2

	    return choice

	def decide_stop_AI(self,player_id):
	    '''
	    Cette fonction decide si l'AI doit s'arréter en fonction d'une certaine difficulté
	    return: boolean

	    '''
	    if self.level_AI[player_id]==1 and self.level_AI[player_id]==2 :
	    	# Si la difficulté est de 1 alors on fait un random
	    	valeurFloatRandom = uniform(0,1)
	    	res = True if valeurFloatRandom > self.P else False
	    else:

	    	# sinon on calcule la somme des distances parcourus de chaque bonze par apport aux pions du joueur
		    somme=0
		    for bonze_local in self.bonzes:
		    	if bonze_local in self.pawns[player_id]:
		    		somme += self.bonzes[bonze_local] - self.pawns[player_id][bonze_local]
		    	else:
		    		somme += self.bonzes[bonze_local]	    


		   	# On vas calculer la moyenne arythmétique des positions des pions du joueur
		    sommeAri=0
		    for pion in self.pawns[player_id]:
		    	sommeAri += self.pawns[player_id][pion]

		    value = int(sommeAri/len(self.pawns[player_id])) if len(self.pawns[player_id]) !=0 else 0
		    value = 9 - (value*2)

		    # Plus les pions seront haut , plus cette moyenne sera grande, on va partir du principe que plus l'on monte,
		    # plus il est dangereux de ne pas s'arréter
		    if  somme <= value and somme!=0:
		    	res =False
		    else:
	    		res =True   
                        
	    return res


	def method_AI_det_1(self,player_id):
		'''
		Cette fonction calcule un certain score pour chaque voie en fonction de la probabilité d'avoir ces mêmes voies
		Un score basé sur la distance par rapport au sommet
		:param player_id : int
		:return dico:
		'''

		# La formule utilisé pour calculer est -->   1 / (proba[v] * (HEIGHT[v] - bonzes[v]) ), où v est la voie
		score={}

		for i in range(2,13):

			pions_haut = self.pawns[player_id][i] if i in self.pawns[player_id] else 0

			value = 1/( self.HEIGHT[i] - pions_haut) if ( self.HEIGHT[i] - pions_haut) !=0 else 0

			score[i] = round( self.proba[i]  * value ,4)
		

		return score


	def method_AI_det_2(self,player_id):
		'''
		Cette fonction calcule un certain score pour chaque voie en fonction de la probabilité d'avoir ces mêmes voies
		Un score basé sur les distances des concurrents par rapport au sommet
		:param player_id: int
		:return dico:
		'''
		
		# La formule utilisé pour calculer est -->   1 / (proba[v], max[pawns[v]]) , où v est la voie 

		score={}
		sortList=[] #Cette liste contiendra tout les hauteurs de touts les pions d'une voie

		for i in range(2,13):
			for j in range(4):

				if i in self.pawns[j]:
					sortList.append(self.pawns[j][i])
				else:
					sortList.append(0)

			

			value = 1/ max(sortList) if max(sortList) !=0 else 0

			score[i] = round( ( self.proba[i]  * value ),4)

			sortList=[]

		return score


	def method_AI_non_det_1(self,listescore,combi_1,combi_2,combi_3):
		'''
		Choix non déterministe
		Cette fonction se base sur une fonction déterministe mais utilise du random
		:param listescore: liste
		:param combi_1: tuple
		:param combi_2: tuple
		:param combi_3: tuple
		return tuple

		'''
		res=0
		alpha = uniform(0,1)  # on choisi un nombre aléatoire de 0 à 1

		# On calcule le score total des combinaisons de dés
		scoreTotal = 1/ (listescore[0]+listescore[1]+listescore[2])

		# on divise le premier score par le total , puis on additione le premier score avec le deuxième et on divise avec le total
		# enfin, on additione les 3 scores qu'on divise avec le Total qui fait "1"
		liste=[ listescore[0]*(scoreTotal),(listescore[0]+listescore[1])* scoreTotal,(listescore[0]+listescore[1]+listescore[2])* scoreTotal]

		# on regarde quel combinaison satisfait alpha
		if not(alpha >= liste[0]):
			choice = combi_1

		elif not(alpha >= liste[1]):
			choice = combi_2
		else:
			choice = combi_3
		
		return choice

	def method_AI_random(self,res_dice):
		'''
		Cette fonction choisi deux paires de dés pour le joueur AI, tout à fait aléatoire
		:param res_dice: tuple(int,int,int,int)
		'''

		self.Gui.groupBox.setTitle("IA choose route")
		#self.Gui.__dict__["route"+str(randint(1,3))].setChecked(True)
		nb1,nb2 = 10 ,10
		while nb1==nb2:
			nb1=randint(1,4)
			nb2=randint(1,4)
			liste = [1,2,3,4]
			liste.remove(nb1)
		liste.remove(nb2)

		return  (res_dice[nb1-1]+res_dice[nb2-1] , res_dice[liste[0]-1] + res_dice[liste[1]-1] )


		








