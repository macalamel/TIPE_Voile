#test reccursive n°2
from math import pi,cos,sin
from copy import deepcopy
from time import time
from os import system
from deplacement import dep
import threading

def deg_to_rad(angle:float)->float:
    '''
    convertie les degrets en radian
    '''
    return angle*pi/180

def eval_time(fonct,*arg)->tuple[int,None]:
    '''
    fonction calcul temps que prend la fonction fonct pour fonctionner
    '''
    t1=time()
    if len(arg)!=0:
        result=fonct(arg)
    else:
        result=fonct()
    return result,time()-t1

def deplace(pos:list,angle:float)->list:
    pos[0]+=cos(deg_to_rad(angle))
    pos[1]+=sin(deg_to_rad(angle))
    pos[0]=round(pos[0],3)
    pos[1]=round(pos[1],3)
    return pos



def all_way():
    '''
    fonction qui utilise la recursivité pour
    chercher tous les chemins


    il retourne une liste avec la syntaxe suivante

    [gain,chemin]

    -le gain indique si oui ou non le chemin menne à l'objectif

    -le chemin indique le parcours effectué.

    '''
    global result,nombre_etape,nombre_arriver,nombre_long,nombre_sortie
    nombre_etape=0
    nombre_sortie=0
    nombre_long=0
    nombre_arriver=0
    result=[[0 for i in range(100)]]
    time1=time()
    def calculer_le_temps_restant(nb_etapes,total):
        return (time()-time1)*total/nb_etapes
    def rec(angle:int,speed:list,pos:list,way:list):
        '''
        fonction recursive,
        prend en argument la vitesse precedentente, la position precedente
        '''
        global result,nombre_etape,nombre_arriver,nombre_long,nombre_sortie
        way1=deepcopy(way)
        for i in range(angle-1,angle+1,1):
            way2=deepcopy(way1)
            pos2,speed2=dep.set_new_pos(speed,pos,i)
            pos3=[(pos2[0]*10)//10,(pos2[1]*10)//10]
            if 0<pos3[0]<50 and 0<pos3[1]<50:
                if 28<=pos3[0]<=32 and 38<=pos3[1]<=42: # si l'objectif est atteint
                    way2.append(pos2)
                    result=[i for i in result if len(i)<=len(way2)]
                    result.append(deepcopy(way2))
                    nombre_arriver+=1
                elif len(way2)<=len(result[0]):         # si le chemin n'est pas trop long
                    way2.append(pos2)
                    rec(i,speed2,pos2,deepcopy(way2))
                else:                                   #le chemin est trop
                    nombre_long+=1
            nombre_etape+=1
            print(nombre_etape,"/10000000000   temps restant estimé : ",round(calculer_le_temps_restant(nombre_etape,100000000000000000000)/3600,1),end="\r")
            #,"temps passée : ",round((time()-time1)/60,1),"nombre de bateaux arrivés : ",nombre_arriver,"nombre de bateau sortis de la map : ",nombre_sortie,"nombre de bateau au chemin trop long : ",nombre_long,end='\r')

        nombre_sortie+=1
    rec(53,[0,0],[0,0],[[0,0],])
    return result

a,dure=eval_time(all_way)
print(len(a),dure,'s')
print(len([i for i in a if i[0]==1]))
system("pause")
