import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def barras(x, y, titulo, xlabel, ylabel, archivo, horizontal=False, color="#1f77b4"):
    fig, ax = plt.subplots(figsize=(10, 6))
    if horizontal:
        ax.barh(x[::-1], y[::-1], color=color)
        ax.set_xlabel(ylabel)
        ax.set_ylabel(xlabel)
    else:
        ax.bar(x, y, color=color)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
    ax.set_title(titulo)
    plt.tight_layout()
    fig.savefig(archivo, dpi=120)
    plt.close(fig)

barras(["1", "2", "3", "4"], [38381, 606235, 352187, 3197],
       "Accidentes por gravedad", "Gravedad", "Accidentes", "g1_gravedad.png")

barras(["2016", "2017", "2021", "2022"], [281261, 230956, 251601, 236182],
       "Accidentes por año", "Año", "Accidentes", "g2_anio.png", color="#2ca02c")

barras(["CA","TX","FL","PA","NY","SC","MI","IL","GA","OH"],
       [256244,122752,96380,49406,43114,41131,37564,36415,32170,27999],
       "Top 10 estados con más accidentes", "Estado", "Accidentes", "g3_estados.png", color="#ff7f0e")

horas = list(range(24))
conteo = [7072,5593,6844,6359,27365,32816,62841,98288,103530,57916,52767,51330,
          41558,40766,44333,50070,65979,67836,57178,42233,31740,21594,16678,7314]
barras([str(h) for h in horas], conteo,
       "Accidentes por hora del día", "Hora", "Accidentes", "g4_hora.png", color="#d62728")

barras(["Fair","Clear","Mostly Cloudy","Partly Cloudy","Overcast","Cloudy",
        "Scattered Clouds","Light Rain","Desconocido","Fog"],
       [237311,208905,134344,93409,80265,69424,47595,41845,18211,10837],
       "Top 10 condiciones climáticas", "Condición", "Accidentes", "g5_clima.png",
       horizontal=True, color="#9467bd")

barras(["CA","TX","FL","GA","NY","MI","IL","VA","OH","PA"],
       [105539,36446,28170,20177,19457,14095,13220,12391,11686,10085],
       "Accidentes graves (gravedad 3 y 4) por estado", "Estado", "Accidentes", "g6_graves.png",
       color="#8c564b")

print("Listo: 6 graficos creados")
