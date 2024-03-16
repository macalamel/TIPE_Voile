"""
fonctionnement de l'algorithme:

    pour chaque point il s'oriente vers l'objectif,
    puis il calcule son angle relatif au nord de la carte.
    Il prend l'intervalle d'angles de [-45,45] centré sur cet angle.
    pour chaque angle il calcule la vitesse suivante s'il choisissait de s'orienter selon celui-ci.
    il détermine finalement l'angle pour lequel la vitesse est maximale.

"""





from math import pi,cos,sin,atan2
from time import time
from os import system
from deplacement import dep
from carte_vect import map


############# fonction utilitaire ##################

def deg_to_rad(angle:float)->float:
    '''
    convertit les degrés en radians
    '''
    return angle*pi/180

def rad_to_deg(angle:float)->float:
    """
    convertit les radians en degrés 
    """
    return angle*180/pi

def eval_time(fonct,*arg)->tuple[None,int]:
    '''
    Calcule le temps que que la fonction "fonct" met à s'exécuter
    '''
    t1=time()
    if len(arg)!=0:
        result=fonct(arg)
    else:
        result=fonct()
    return result,time()-t1

def norme(vect:list)->float:
    """
    calcule la norme d'un vecteur possédant deux coordonnées
    """
    return (vect[0]**2+vect[1]**2)**0.5

def get_goal(pos:list,goal:list,aprox:float)->bool:
    """
    paramètres:
        - pos : position actuelle dans le repère [x,y]
        - goal: position de l'objectif dans le repère [x,y]
        - aprox: valeur de l’approximation
    
    la fonction retourne si oui ou non le bateau se trouve suffisamment près de l'objectif pour qu'on puisse considérer qu'il est atteint
    """
    if goal[0]-aprox<pos[0]<goal[0]+aprox:
        if goal[1]-aprox<pos[1]<goal[1]+aprox:
            return True
    return False


######################## fonction algo ###############################

def set_next_pos(prec:list,speedpec:list,cible:list)->tuple[list,list]:
    """
    paramètres:
        - prec: position précédente
        - speedpec: vitesse précédente
        - cible: position de l'objectif

    fonction qui choisit la prochaine position
    """
    liste=[] # initialisation de la liste de positions potentielles

    # calcule l'angle entre l'objectif et le nord
    x=cible[0]-prec[0]
    y=cible[1]-prec[1]
    alpha=atan2(y,x)
    
    # on prend un intervalle [alpha-40,alpha+40] et pour chaque angle dans cet intervalle
    # on calcule la prochaine position et vitesse, si celles-ci existent
    for i in range(int(rad_to_deg(alpha)-40),int(rad_to_deg(alpha)+40)):
        try:
            pos,speed=dep.set_new_pos(speedpec,prec,i)
            if 0<pos[0]<50 and 0<pos[1]<50:
                liste.append([speed,pos,i])
        except:
            pass
    # recherche le point suivant pour lequel la vitesse est maximale
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

    # Sert à faire parcourir au bateau le chemin choisi 
    while not get_goal(pos,cible,2):
        speed,pos=set_next_pos(pos,speed,cible)
        way.append(pos)
    
    # affichage et presentation des résultats
    print(way)
    map.show_way(way)
    map.show_map()
    return way

def set_next_pos_2(prec:list,speedpec:list,cible:list,distance_init:float)->tuple[list,list]:
    """
    paramètres:
        - prec: position précédente
        - speedpec: vitesse précédente
        - cible: position de l'objectif

    fonction qui choisit la prochaine position
    """
    liste=[] # initialisation de la liste de positions potentielles

    # calcule l'angle entre l'objectif et le nord
    x=cible[0]-prec[0]
    y=cible[1]-prec[1]

    distance=((abs(x)**2)+(abs(y)**2))**0.5
    alpha=atan2(y,x)
    print((distance/distance_init),end='\r')
    
    # on prend un intervalle [alpha-40,alpha+40] et pour chaque angle dans cet intervalle
    # on calcule la prochaine position et vitesse, si celles-ci existent
    for i in range(int(rad_to_deg(alpha)-45*(3*distance/distance_init)),int(rad_to_deg(alpha)+45*(3*distance/distance_init))):
        try:
            pos,speed=dep.set_new_pos(speedpec,prec,i)
            if 0<pos[0]<50 and 0<pos[1]<50:
                liste.append([speed,pos,i])
        except:
            pass
    # recherche le point suivant pour lequel la vitesse est maximale
    speed_liste=[norme(i[0]) for i in liste]
    max_speed=max(speed_liste)
    return liste[speed_liste.index(max_speed)][:2]

def algorithme_2():
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

    distance_init=((abs(cible[0]-pos[0])**2)+(abs(cible[1]-pos[1])**2))**0.5

    # Sert à faire parcourir au bateau le chemin choisi 
    while not get_goal(pos,cible,2):
        speed,pos=set_next_pos_2(pos,speed,cible,distance_init)
        way.append(pos)
    
    # affichage et presentation des résultats
    print(way)
    map.show_way(way)
    map.show_map()
    return way
###################### fonction qui fait aller le bateau en ligne droite jusqu'a la cible ####################

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
    a,dure=eval_time(algorithme_2)
    print(len(a),dure,'s')
    a,dure=eval_time(algorithme)
    print(len(a),dure,'s')
    a,dure=eval_time(droite)
    print(len(a),dure,'s')

##############################
