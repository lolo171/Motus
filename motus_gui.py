#Importation des bibliotheque
from tkinter import * #pour la mise en page
from random import choice #pour choisir un mot proto aléatoire

def charger_mots(fichier, nb_lettres):
  '''
  FAit une liste de mot du nbr de lettre demander et en choisis juste un avec choice
  '''
  with open(fichier, "r") as f:
    mots = [ligne.rstrip() for ligne in f]
  mots_filtres = [mot for mot in mots if len(mot) == nb_lettres] #fait une liste de mot du nombre de lettre demandé
  return choice(mots_filtres) # renvoie un mot aléatoire parmi eux

def ecrire(fichier: str, mot: str) -> None:
    '''
    Ecrit un mot dans un fichier
    '''
    with open(fichier, "a") as f:
        f.write(mot + "\n") #ecrit un mot et rajoute un retour chariot
def compter_lignes(fichier):
  '''
  Compte le nombre de mot du fichier
  '''
  with open(fichier, "r") as f:
    lignes = f.readlines() #fait une liste de lignes
    nbr=len(lignes) #compte le nombre d'element lignes
  return nbr
  
def vider(fichier: str) -> None:
  '''
  Clear le fichier
  '''
  with open(fichier, "w") as f:
    f.truncate() #vide le fichier avec truncate

def camoufler(mot_propose, mot_cible):
  '''
  Affiche le mot en fonction du mot cible et du mot proposé avec des indices comme dit dans le md
  '''
  indices = []
  for i in range(len(mot_cible)):
    if mot_propose[i] == mot_cible[i]:
      indices.append(f"{mot_propose[i].upper()}") #si la lettre est bien place en la mets en majuscule dans indices
    elif mot_propose[i] in mot_cible:
      indices.append(f"{mot_propose[i].lower()}") #si elle est mal placé en minuscules
    else:
      indices.append("#") #si elle n'est pas dans le mot on ajoute un #
  return "".join(indices)

def jouer_partie(niveau,essais):
  '''
  Joue la partie de Motus en fonction du niveau(nbr lettre) et du nbr d'essais
  '''
  mot_cible = charger_mots("data_mots.txt", niveau) # on charge le mot a trouver
  premiere_lettre = mot_cible[0] #on regarde sa premiere lettre
  trouve = False #initialise pas trouvez le mot

  fenetre = Tk() #creer une fenetre avec tk
  fenetre.title("Motus") # et on l'apelle Motus

  label_lettre = Label(fenetre, text=f"La première lettre est : {premiere_lettre.upper()}") # On dit la premiere lettre
  label_lettre.pack()

  entree_mot = Entry(fenetre) # On creer une entrée pour ecrire les proposition
  entree_mot.pack()

  def valider_mot():
    '''
    valide le mot et affiche les indices
    '''
    mot_propose = entree_mot.get().lower() #on empeche la casse
    ecrire('game.txt', mot_propose) # on rajoute le mot dans le fichier pour pouvoir le compter apres
    if len(mot_propose) != niveau or mot_propose[0] != premiere_lettre: # on verifie que la premiere lettre est la bonne 
      return

    indices = camoufler(mot_propose, mot_cible) # on ffait l'indices
    label_indices = Label(fenetre, text=indices) #et on laffiche dans un labels
    
    label_indices.pack()

    if mot_propose.upper() == mot_cible.upper(): # si c'est le bon mot on le mets en maj
      trouve = True
      label_resultat = Label(fenetre, text=f"Bravo ! Vous avez trouvé le mot en {essais} essais.") # on lui donne une carotte si il trouve
      label_resultat.pack()
    else:
      if compter_lignes('game.txt') == 6:
        label_resultat = Label(fenetre, text=f"Dommage ! Le mot était : {mot_cible}") # sinon on lui dit qu'il est nul
        label_resultat.pack()

  # Bouton de validation
  bouton_valider = Button(fenetre, text="Valider", command=valider_mot)
  bouton_valider.pack()
  
  #Mise en page rapide
  fenetre.config(bg="lightblue") 
  fenetre.minsize(200,100)
  fenetre.mainloop()

  if trouve == True:
    return True
  else:
    return False

def main():
  '''
  Lance la partie et la remets a zero
  '''
  vider('game.txt')
  niveau = int(input("Choisissez le nombre de lettres : "))
  jouer_partie(niveau,6)

main()
