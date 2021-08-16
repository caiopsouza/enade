import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

from data_keys import load_and_prepare_data, cursos_names


def load_and_prepare_renda_data():
    df = load_and_prepare_data()

    renda_familiar_values = {
        'A': 1.5,
        'B': (1.5 + 3) / 2,
        'C': (3 + 4.5) / 2,
        'D': (4.5 + 6) / 2,
        'E': (6 + 10) / 2,
        'F': (10 + 30) / 2,
        'G': 30
    }

    df.QE_I08.replace(renda_familiar_values, inplace=True)

    return df


df = load_and_prepare_renda_data()

renda_por_curso = df[['CO_GRUPO', 'QE_I08']] \
    .groupby(by='CO_GRUPO') \
    .mean() \
    .reset_index()

renda_por_curso['CO_GRUPO'].replace(cursos_names, inplace=True)

renda_geral_mean = df.QE_I08.mean()

renda_geral = pd.DataFrame([['Geral', renda_geral_mean]], columns=['CO_GRUPO', 'QE_I08'], index=[29])

renda_por_curso = renda_por_curso.append(renda_geral)

renda_por_curso = renda_por_curso.sort_values(by='QE_I08', ascending=False)

color_less_than = '#EB548C'
color_greater_than = '#29066B'
color_equal_to = '#AF4BCE'


def color(v):
    if v < renda_geral_mean:
        return color_less_than
    if v > renda_geral_mean:
        return color_greater_than
    return color_equal_to


cursos_valores = [x[1].QE_I08 for x in renda_por_curso.iterrows()]
cursos_colors = [color(x) for x in cursos_valores]

ax = renda_por_curso.plot.barh(figsize=(19.2, 10.8),
                               color=cursos_colors,
                               x='CO_GRUPO',
                               y='QE_I08',
                               xlabel='',
                               rot=0,
                               fontsize='14')

mid = (ax.figure.subplotpars.right + ax.figure.subplotpars.left) / 2

ax.grid(axis='x')

plt.title('\nRenda média por curso\n',
          fontsize=20,
          va='top',
          x=0.425)

for i, v in enumerate(cursos_valores):
    ax.text(v + .05, i, "{:2.2f}".format(v), color=cursos_colors[i], fontsize=12, fontweight='bold', va='center')

plt.legend(prop={'size': 18}, handles=[
    mpatches.Patch(color=color_less_than, label='Menor que a média geral'),
    mpatches.Patch(color=color_equal_to, label='Renda média geral'),
    mpatches.Patch(color=color_greater_than, label='Maior que a média geral'),
])

plt.tight_layout()
plt.show()
plt.close()
