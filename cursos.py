import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors
import math
import matplotlib.patches as mpatches


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    df.drop(df[df.QE_I08 == ' '].index, inplace=True)

    df.QE_I08.replace(renda_familiar_values, inplace=True)

    return df


def count_and_rename_labels(df, labels, normalize=False):
    return df \
        .value_counts(normalize=normalize) \
        .sort_index() \
        .rename(labels)


renda_familiar_values = {
    'A': 1.5,
    'B': (1.5 + 3) / 2,
    'C': (3 + 4.5) / 2,
    'D': (4.5 + 6) / 2,
    'E': (6 + 10) / 2,
    'F': (10 + 30) / 2,
    'G': 30
}

cursos_values = {
    0: 'Geral',
    5: 'Veterinária',
    6: 'Odontologia',
    12: 'Medicina',
    17: 'Agronomia',
    19: 'Farmácia',
    21: 'Arquitetura e Urbanismo',
    23: 'Enfermagem',
    27: 'Fonoaudiologia',
    28: 'Nutrição',
    36: 'Fisioterapia',
    51: 'Zootecnia',
    55: 'Biomedicina',
    69: 'Tec. em Radiologia',
    90: 'Tec. em Agronegócios',
    91: 'Tec. em Gestão Hospitalar',
    92: 'Tec. em Gestão Ambiental',
    95: 'Tec. em Estética e Cosmética',
    3501: 'Educação Física (Bacharelado)',
    4003: 'Eng. da Computação',
    5710: 'Eng. Civil',
    5806: 'Eng. Elétrica',
    5814: 'Eng. de Controle e Automação',
    5902: 'Eng. Mecânica',
    6002: 'Eng. de Alimentos',
    6008: 'Eng. Química',
    6208: 'Eng. de Produção',
    6307: 'Eng. Ambiental',
    6405: 'Eng. Florestal',
    6410: 'Tec. em Segurança no Trabalho',
}

df = load_and_prepare_data()

renda_por_curso = df[['CO_GRUPO', 'QE_I08']] \
    .groupby(by='CO_GRUPO') \
    .mean() \
    .reset_index()

renda_por_curso['CO_GRUPO'].replace(cursos_values, inplace=True)

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
plt.savefig('plots/renda-media-curso.png')
