import json,sys
from math import pi
import matplotlib.pyplot as plt
import numpy as np


class Polaire:
    """
    classe pour la creation et gestion des polaire\n
    utiliser la fonction set_rapport pour connaître\n
    le report de force du vent en fonction d'un angle
    """
    def __init__(self,name_boat:str):
        self.verify_variables_type(name_boat,str)
        self.verify_variables_value(name_boat,("bonface","bondos"))
        self.name_boat=name_boat
        self.data=self.import_data()
        self.name_angle=["pres1","travers1","largue1","arriere1","pres2","travers2","largue2","arriere2"]
        self.dico_fonc={self.name_angle[i]:self.data[self.name_boat][self.name_angle[i]] for i in range(len(self.name_angle))}
    def verify_variables_value(self,variable,_value:tuple):
        """"
        check if the value is possible
        """
        if variable in _value:
            return True
        print(f"Error value for {variable}, please check value")
        sys.exit()
    def verify_variables_type(self,variable,_type):
        "check the type of the value"
        if type(variable)==_type:
            return True
        print(f"Error type for {variable}, {_type} is needed not {type(variable)}")
        sys.exit()
    def import_data(self):
        """
        import la base de donnée data.json
        stocke les données dans le dictionnaire self.data
        """
        try:
            path="..\\Database\\data.json"
            with open(path,"r") as f :
                data=json.load(f)
        except:
            path="Database/data.json"
            with open(path,"r") as f :
                data=json.load(f)
        return data
    def chose_name(self,angle:float)->str:
        """
        renvoi le nom de l'angle\n
        est utile pour utiliser la base de donnée
        """
        if angle<=(pi/4):
            return "pres1"
        if angle<(pi/2):
            return "travers1"
        if angle<(3*pi/4):
            return "largue1"
        if angle<pi:
            return "arriere1"
        if angle<(5*pi/4):
            return "arriere2"
        if angle<(3*pi/2):
            return "largue2"
        if angle<(7*pi/4):
            return "travers2"
        return "pres2"
    def set_rapport(self,angle:float)->float:
        """
        prend en paramètre l'angle entre la poupe et le vent\n
        retourne un coefficient de prise au vent\n
        en fonction de l'angle entre le vent et le bateau
        """
        para=self.dico_fonc[self.chose_name(angle)]
        x=lambda téta: (para[0]*téta+para[1])/5
        return x(angle)
    def plot_angle(self):
        """
        trace une courbe de 200000 point\n
        avec x entre 0 et 2pi et y le rapport de vent
        """
        liste_angles=np.linspace(0,2*pi,200000)
        result1=[self.set_rapport(i) for i in liste_angles]
        plt.figure()
        plt.title("polaire")
        plt.xlabel("angle téta entre le vent et le voilier")
        plt.ylabel("pourcentage de prise au vent")
        plt.plot(liste_angles,result1)
        plt.show()

polaire_bon_face=Polaire('bonface')
polaire_bon_dos=Polaire('bondos')

if __name__=="__main__":
    test1=Polaire('bondos')
    test1.plot_angle()
