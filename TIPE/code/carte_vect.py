from math import cos,sin,pi
import matplotlib.pyplot as plt
from random import randint
class Math:
    def deg_to_rad(angle):
        return angle*pi/180

class MapVector:
    def __init__(self) -> None:
        self.vector={}
        self.list_coord=[]
    def add_vector(self,startx:float=0,starty:float=0,lenght:float=0,angle:float=0)->None:
        """
        ajoute des vecteurs dans le dictionnaire des vecteurs et calcule leurs coordonnées pour les ajouter dans la liste

        paramètres:
            - startx: point de départ du vecteur en x
            - starty: point de départ du vecteur en y
            - lenght: norme du vecteur
            - angle: direction du vecteur par rapport au nord
        """
        self.vector[(startx,starty)]=[(cos(Math.deg_to_rad(angle))*lenght),(sin(Math.deg_to_rad(angle))*lenght)]
        self.list_coord.append([startx,starty,(cos(Math.deg_to_rad(angle))*lenght),(sin(Math.deg_to_rad(angle))*lenght)])
    def make_map(self):
        """
        Créé la carte en ajoutant les vecteurs 
        """
        plt.plot(30,40,"rx",markersize=12)
        for i in self.list_coord:
            plt.quiver(i[0],i[1],i[2],i[3],width=0.0025,angles='xy', scale_units = 'xy', scale = 1)

###################### fabrication des différentes cartes #################################
    def set_map_1(self):
        big_list=[]
        for i in range(3):
            for j in range(30):
                big_list.append([i*10,j*10,5,0])
        for i in range(30):
            for j in range(3):
                big_list.append([i*10,j*10,5,90])
        for i in range(3,30):
            for j in range(3,30):
                big_list.append([i*10,j*10,5,(i)*90/30+(j)*90/30])
        for i in big_list:
            self.add_vector(i[0],i[1],i[2],i[3])
    def set_map_2(self):
        big_list=[]
        for i in range(10):
            for j in range(10):
                big_list.append([i*5,j*5,5,(i)*90/15+(j)*90/15])
        for i in big_list:
            self.add_vector(i[0],i[1],i[2],i[3])
    def set_map_3(self):
        big_list=[]
        for i in range(10):
            for j in range(10):
                big_list.append([i*5,j*5,5,(i)*90/(-15)+(j)*90/(-15)])
        for i in big_list:
            self.add_vector(i[0],i[1],i[2],i[3])
    def set_map_4(self):
        big_list=[]
        for i in range(10):
            for j in range(10):
                big_list.append([i*5,j*5,5,(i)*90/(15)+(j)*90/(-15)])
        for i in big_list:
            self.add_vector(i[0],i[1],i[2],i[3])
    def set_map_droite(self):
        big_list=[]
        for i in range(10):
            for j in range(10):
                big_list.append([i*5,j*5,5,90])
        for i in big_list:
            self.add_vector(i[0],i[1],i[2],i[3])
##############################################################################################""

    def show_way(self,position):
        """
        permet d'ajouter un chemin à la carte vectorielle
        """
        self.make_map()
        x=[i[0] for i in position]
        y=[i[1] for i in position]
        plt.plot(x,y,"ro",markersize=3)
        plt.plot(x,y)
    def show_map(self):
        """
        affiche la carte
        """
        plt.show()


map=MapVector()
map=MapVector()
map.set_map_2()
map.make_map()


if __name__=="__main__":
    plt.show()
