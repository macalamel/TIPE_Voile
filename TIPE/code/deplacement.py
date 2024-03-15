from carte_vect import map
from polaires import polaire_bon_face,polaire_bon_dos
from math import sin,cos,pi,atan2

class Deplacement:
    """
    classe pour donner une position en fonction du vent et de la position précédente
    """
    def __init__(self,map,polaire,size_box:int=10,debug=False) -> None:
        self.size_box=size_box
        self.map=map
        self.polaire=polaire
        self.debug=debug
    def set_case(self,pos:tuple) -> tuple:
        """
        retourne la case dans laquelle est le bateau en fonction de sa position
        """
        x=pos[0]//self.size_box
        y=pos[1]//self.size_box
        res=(int(x*10),int(y*10))
        if self.debug:
            print("case actuelle =",res) 
        return res
    def get_wind(self,pos:tuple)->list:
        """
        retourne les caractéristiques du vent de la case dans laquelle le bateau se trouve.
        """
        try:
            res=self.map.vector[self.set_case(pos)]
        except:
            print(self.set_case(pos))
        if self.debug:
            print("vitesse du vents =",res)
        return res
    def set_relatif_wind(self,angle:int,vents:list):
        """
        retourne le vent relatif au bateau
        """
        if vents[0]==0:
            res=angle-pi/2
        elif vents[1]==0:
            res=angle
        elif vents[0]>0 and vents[1]>0:
            res=angle-atan2(abs(vents[1]),abs(vents[0]))
        elif vents[0]<0 and vents[1]>0:
            res=angle-atan2(abs(vents[1]),abs(vents[0]))+pi/2
        elif vents[0]<0 and vents[1]<0:
            res=angle-atan2(abs(vents[1]),abs(vents[0]))+pi
        else:
            res=angle-atan2(abs(vents[1]),abs(vents[0]))+3*pi/2
        if self.debug:
            print("vent relatif =",res)
        return res
    def get_rapport(self,angle:float)->float:
        """
        retourne le rapport de prise au vent en fonction de l'angle entre le vent et le bateau
        """

        res=self.polaire.set_rapport(angle)
        if self.debug:
            print("pourcentage du vents =",res)
        return res
    def borne_speed(self,speed:list,max:list)->list:
        """
        borne la vitesse pour ne pas dépasser la vitesse du vent
        """
        result=[0,0]
        if speed[0]>max[0]:
            result[0]=max[0]
        if speed[1]>max[1]:
            result[1]=max[1]
        if result!=[0,0]:
            return result
        if self.debug:
            print("vitesse bornée =",speed)
        return speed
    def set_new_speed(self,speed:list,pos:tuple,angle:float)->list:
        """
        retourne la nouvelle valeur de la vitesse en fonction du vent et de l'angle entre celui-ci et le bateau
        """
        wind=self.get_wind(pos)
        rapport=self.get_rapport(self.set_relatif_wind(angle,wind))
        #################################################################################
        new_speed=[(speed[0]*0.5)+(rapport*wind[0]),(speed[1]*0.5)+(rapport*wind[1])]  #partie a changer
        #################################################################################
        real_speed=self.borne_speed(new_speed,wind)
        if self.debug:
            print("vitesse =",real_speed)
        return real_speed
    
    def set_new_speed_2(self,speed:list,pos:tuple,angle:float)->list:
        """
        retourne la nouvelle valeur de la vitesse en fonction du vent et de l'angle entre celui-ci et le bateau
        """
        wind=self.get_wind(pos)
        rapport=self.get_rapport(self.set_relatif_wind(angle,wind))
        ##################################  Constantes  ###############################################
        if 90<angle<=180:
            Cxva=1.2
            Czva=0
        else:
            Cxva=0.83
            Czva=0.8
        Cxce=0.09
        Cxca=0.09
        Sv=22.2
        Sa=6.1458
        Se=21.8064
        Roa=1.225
        Roe=1029
        m=3945
        K=0.5*(Roa*(Sv*(Czva-Cxva)-Sa*Cxca)-Roe*Se*Cxce)
        #############################################################################################

        new_speed=[((K/m)*(speed[0]**2))+speed[0],((K/m)*(speed[1]**2))+speed[1]] # équation discrétisée

        
        real_speed=self.borne_speed(new_speed,wind)
        if self.debug:
            print("vitesse =",real_speed)
        return real_speed
    def deg_to_rad(self,angle:float)->float:
        '''
        convertie les degrets en radian
        '''
        return angle*pi/180
    def set_new_pos(self,speed:list,pos:tuple,angle:float)->tuple:
        """
        retourne la nouvelle position a partir de l'ancienne
        l'angle doit être en degrés
        """
        angle=self.deg_to_rad(angle)
        new_speed=self.set_new_speed(speed,pos,angle)
        norme_speed=(new_speed[0]**2+new_speed[1]**2)**0.5
        new_pos=[pos[0]+norme_speed*cos(angle),pos[1]+norme_speed*sin(angle)]
        if self.debug:
            print("nouvelle position =",new_pos)
        return new_pos,new_speed

dep=Deplacement(map,polaire_bon_face,debug=False)

if __name__=="__main__":
    test=Deplacement(map,polaire_bon_face,debug=True)
    position=[[0,0]]
    pos=[0,0]
    i=0
    while test.set_case(pos)!=(30,40):
        pos=test.set_new_pos([0,0],position[i], 53)[0]
        position.append(pos)
        i+=1
    print(i)
    map.show_way(position)
    map.show_map()
