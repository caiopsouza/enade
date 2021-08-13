import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors
import matplotlib.patches as mpatches


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    df.drop(df[df.QE_I04 == ' '].index, inplace=True)

    return df


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

# data = load_and_prepare_data()

df = data.groupby(by=['CO_GRUPO', 'QE_I02']).size().reset_index()
df_pivotted = df.pivot_table(index='CO_GRUPO', columns='QE_I02', values=0).reset_index()

total = df_pivotted['A'] + df_pivotted['B'] + df_pivotted['C'] + df_pivotted['D'] + df_pivotted['E'] + df_pivotted['F']

for i in ['A', 'B', 'C', 'D', 'E', 'F']:
    df_pivotted[i + '_PERC'] = df_pivotted[i] / total

df_pivotted['CO_GRUPO'] = pd.to_numeric(df_pivotted['CO_GRUPO'])

df_sorted = df_pivotted.sort_values(by='A_PERC', ascending=False)
df_sorted['CO_GRUPO_DESC'] = df_sorted['CO_GRUPO'].replace(cursos_values)

ax = df_sorted.plot.barh(figsize=(19.2, 10.8),
                         x='CO_GRUPO_DESC',
                         y=['A_PERC', 'B_PERC', 'C_PERC', 'D_PERC', 'E_PERC', 'F_PERC'],
                         cmap='Dark2',
                         xlabel='',
                         rot=0,
                         stacked=True,
                         fontsize='14')

plt.title('\nPorcentagem de raça por curso\n',
          fontsize=20,
          va='top',
          x=0.425)

ax.grid(axis='x')

ax.set(xlim=[0, 1])

plt.legend(prop={'size': 16}, handles=[
    mpatches.Patch(color='#1B9E77', label='Branca'),
    mpatches.Patch(color='#D95F02', label='Preta'),
    mpatches.Patch(color='#E7298A', label='Amarela'),
    mpatches.Patch(color='#66A61E', label='Parda'),
    mpatches.Patch(color='#A6761D', label='Indígena'),
    mpatches.Patch(color='#666666', label='Não quero declarar'),
])

plt.tight_layout()
plt.show()
