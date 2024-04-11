from random import choice


def charger(fichier, nb_lettres):
  with open(fichier, "r") as f:
    mots = [ligne.rstrip() for ligne in f]

  mots_filtres = [mot for mot in mots if len(mot) == nb_lettres] #choisi un mot du bon nombre de lettres
  mot_choisi = choice(mots_filtres) #et prends un mot aléatoire dans cette liste

  return mot_choisi

def ecrire(fichier: str, mot: str) -> None:
    '''
    Ecrit dans un fichier un mot a la ligne
    '''
    with open(fichier, "a") as f:
        f.write(mot + "\n")
    
 
def vider(fichier: str) -> None:
  with open(fichier, "w") as f:
    f.truncate()
    
  
def recherche(mot, niveau, premiere_lettre):
    '''
    Args: 
      mot -> le mot a verifier
      niveau -> le nombre de lettres
      premiere_lettre -> la premiere lettre du mot
    return un booleen si le mot fait le bon nombre de lettre
    commence par la bonne lettre et fait partie du dico.
    '''
    
    if len(mot) != niveau: # si il fait pas la bonne taille
        print("Le mot doit avoir", niveau, "lettres.") # on lui dit
        return False
    if mot[0] != premiere_lettre:
        print("Le mot doit commencer par la lettre", premiere_lettre) # si cest pas la bonne lettre au debut
        return False
    return True


def camoufler(mot_propose, mot_cible):
    '''
    Args:
      mot_prpose and mot_cible -> 2 chaine de caractere qui vont etre comparée
    Ecrit le lettre Bien placé du mot cible en majuscule. 
    Les lettre mal placé en minuscule.
    Et les lettre qui ne font pas partie du mot sont remplacée par des _.
    Return: -> une chaine de caractere des indices.
    '''
    indices = [] #init les indices
    for i in range(len(mot_cible)): #se promene dans toute les lettres
        if mot_propose[i] == mot_cible[i]: # si la lettre est bien placé
            indices.append(f"{mot_propose[i].upper()}") # on la rajoute en majuscules
        elif mot_propose[i] in mot_cible: # si la lettre est dans le mot mais mal placé
            indices.append(f"{mot_propose[i].lower()}") # On l'ecrit en minuscules
        else:
            indices.append("#") # Sinon on mais des #
    return "".join(indices) # on revoie une chaine de caractere de tout les indices de la liste.


def jouer_partie(niveau):
    '''
    Args:niveau -> est un nombre de lettre pour le jeu
        
        Affiche la premiere lettre du mot.
        Et vous devez le devinez.
        Une fois trouvez la partie s'arrete et vous pouvez rejouez si vous le voulez.
    '''
    mot_cible = charger('data_mots.txt',niveau) #definis le mot a deviner
    premiere_lettre = mot_cible[0] # Prends la premiere lettre du  mot
    essais = 0 # init le nombre d'essaie sachant quand a le droit a 6 esaie max
    trouve = False #init si il a trouver
    print(f'La première lettre est {premiere_lettre.upper()}') #ecrit la premiere lettre qu'on a trouvez
    while not trouve and essais < 6: # Tant qu'on a pas trouvez le mot et qu'on a pas fait tou nos essaie on joue
        # input du mot propose
        mot_propose = input("Proposez un mot : ").lower()
        
        # verif de la validité du mot
        if not recherche(mot_propose, niveau, premiere_lettre):
            print("Mot invalide !")
            continue
        
        essais += 1
        ecrire('game.txt', mot_propose)
        # Affichage des indices
        indices = camoufler(mot_propose, mot_cible)
        print(indices)
        
        # Verif si le mot est trouvé
        if mot_propose.upper() == mot_cible.upper():
            trouve = True
    
    if trouve: #si cest True
        print(f"Bravo ! Vous avez trouvé le mot en {essais} essais.")
    else: #Sinon
        print(f"Dommage ! Le mot était : {mot_cible}")


def main():
    '''
    Creer une partie Motus
    '''
    vider('game.txt')
    niveau = int(input("Choisissez le nombre de lettre : ")) #definis le nombre de lettre du mot
    jouer_partie(niveau)

main()