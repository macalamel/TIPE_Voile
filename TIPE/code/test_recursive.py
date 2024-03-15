from math import pi,cos,sin
from copy import deepcopy
from time import sleep,time
from polaires import Polaire

def deg_to_rad(angle:float)->float:
    '''
    convertit les degrés en radians
    '''
    return angle*pi/180

def eval_time(fonct,*arg)->tuple[int,None]:
    '''
    calcule le temps mis par la fonction "fonct" à s'exécuter
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


    elle retourne une liste avec la syntaxe suivante :

    [gain,chemin]

    -le gain indique si oui ou non le chemin mène à l'objectif

    -le chemin indique le parcours effectué.

    '''

    result=[]
    def rec(pos:list,way:list):
        '''
        fonction récursive
        '''
        way1=deepcopy(way)
        for i in range(0,360,36):
            way2=deepcopy(way1)
            pos2=deplace(pos,i)
            if pos2==[8,4]:                       # si le goal est atteint
                way2.append(pos2)
                result.append([1,deepcopy(way2)])
                pass
            elif len(way2)>5:                     # si le chemin est trop long
                way2.append(pos2)
                result.append([0,deepcopy(way2)])
            else:
                way2.append(pos2)
                rec(pos2,way2)
    rec([0,0],[[0,0],])
    return result

a,dure=eval_time(all_way)
print(len(a),dure,'s')
print([i for i in a if i[0]==1])
sleep(20)

