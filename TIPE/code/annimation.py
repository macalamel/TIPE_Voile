import matplotlib.pyplot as plt
from test_algo_coef import algorithme_3
from carte_vect import map
from matplotlib.animation import FuncAnimation,PillowWriter
 

way=algorithme_3()

# Configuration de la figure et de l'axe
fig, ax = plt.subplots()
xdata, ydata = [], []
map.make_map()
courbe, = plt.plot([], [], 'b-')
point, =plt.plot([],[],'ro')
angle, =plt.plot([],[],'g-')


def init():
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 50)
    return courbe,

def update(frame):
    if frame%2==0:
        xdata=[way[i][0] for i in range(int(frame/2))]
        ydata=[way[i][1] for i in range(int(frame/2))]
        courbe.set_data(xdata,ydata)
        point.set_data(xdata,ydata)
    else:
        xdata=[way[int(((frame+1)//2)-2)][0],25]
        ydata=[way[int(((frame+1)//2)-2)][1],40]
        angle.set_data(xdata,ydata)
    return courbe,point

ani = FuncAnimation(fig, update, frames=range(len(way)*2),init_func=init, interval=500,repeat=True, blit=False)
plt.show()

# writer = PillowWriter(fps=2,metadata=dict(artist='Me'),bitrate=1800)
# ani.save('résolution.gif', writer=writer)