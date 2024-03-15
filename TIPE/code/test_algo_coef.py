"""
fonctionnement de l'algorithme:

    pour chaque point il s'orante vers l'objectif,
    puis il calcule son angle relatif au nord de la carte
    il prend l'interval d'angle de [-45,45] par rapport a cet angle.
    pour chaque angle il calcule la vitesse suivante s'il s’oriente selon celui-ci.
    il prend l'angle pour lequel la vitesse est maximal.

"""





from math import pi,cos,sin,atan2
from time import time
from os import system
from deplacement import dep
from carte_vect import map


############# fonction utilitaire ##################

def deg_to_rad(angle:float)->float:
    '''
    convertie les degrés en radian
    '''
    return angle*pi/180

def rad_to_deg(angle:float)->float:
    """
    convertie les radian en degrés 
    """
    return angle*180/pi

def eval_time(fonct,*arg)->tuple[None,int]:
    '''
    fonction calcul temps que prend la fonction fonct pour fonctionner
    '''
    t1=time()
    if len(arg)!=0:
        result=fonct(arg)
    else:
        result=fonct()
    return result,time()-t1

def norme(vect:list)->float:
    """
    calcule la norme d'un vecteur de dimension 2
    """
    return (vect[0]**2+vect[1]**2)**0.5

def get_goal(pos:list,goal:list,aprox:float)->bool:
    """
    paramètre:
        - pos : position actuel [x,y]
        - goal: position objectif [x,y]
        - aprox: valeur de l’approximation
    
    la fonction retourne si oui ou non l'objectif est atteint avec une approximation
    """
    if goal[0]-aprox<pos[0]<goal[0]+aprox:
        if goal[1]-aprox<pos[1]<goal[1]+aprox:
            return True
    return False


######################## fonction algo ###############################

def set_next_pos(prec:list,speedpec:list,cible:list)->tuple[list,list]:
    """
    paramètre:
        - prec: position précédente
        - speedpec: vitesse précédente
        - cible: position de l'objectif

    fonction qui choisie la prochaine position
    """
    liste=[] # initialisation de la liste de potentiel position

    # calcule l'angle entre l'objectif et le nord
    x=cible[0]-prec[0]
    y=cible[1]-prec[1]
    alpha=atan2(y,x)
    
    # on prend un interval [alpha-40,alpha+40] et pour chaque angle dans cet interval
    # on calcule la prochaine position et vitesse si celles ci existent
    for i in range(int(rad_to_deg(alpha)-40),int(rad_to_deg(alpha)+40)):
        try:
            pos,speed=dep.set_new_pos(speedpec,prec,i)
            if 0<pos[0]<50 and 0<pos[1]<50:
                liste.append([speed,pos,i])
        except:
            pass
    # recherche le point suivant où la vitesse est maximal
    speed_liste=[norme(i[0]) for i in liste]
    max_speed=max(speed_liste)
    return liste[speed_liste.index(max_speed)][:2]

def algorithme()->list:
    """
    fonction qui trouve le chemin optimal 
    pour allez d'un point A a un point B
    en subissant le vent
    """
    # initialisation des conditions initiales
    way=[[0,0],]
    pos=[0,0]
    speed=[0,0]
    cible=[30,40]

    # partie qui fait le chemin
    while not get_goal(pos,cible,2):
        speed,pos=set_next_pos(pos,speed,cible)
        way.append(pos)
    
    # affichage et presentation des résultat
    print(way)
    map.show_way(way)
    map.show_map()
    return way

###################### fonction qui fait allez le bateau en ligne droite jusqu'a la cible ####################

def droite():
    way=[[0,0],]
    pos=[0,0]
    speed=[0,0]
    cible=[30,40]
    while not get_goal(pos,cible,2):
        x=cible[0]-pos[0]
        y=cible[1]-pos[1]
        alpha=atan2(y,x)
        pos,speed=dep.set_new_pos(speed,pos,rad_to_deg(alpha))
        way.append(pos)
    print(way)
    map.show_way(way)
    map.show_map()
    return way



########### main #############

if __name__=="__main__":
    a,dure=eval_time(algorithme)
    print(len(a),dure,'s')
    a,dure=eval_time(droite)
    print(len(a),dure,'s')
    system("pause")

##############################