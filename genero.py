import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors
import matplotlib.patches as mpatches


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")
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

df = data.groupby(by=['CO_GRUPO', 'TP_SEXO']).size().reset_index()
df_pivotted = df.pivot_table(index='CO_GRUPO', columns='TP_SEXO', values=0).reset_index()

total = df_pivotted['F'] + df_pivotted['M']
df_pivotted['F_PERC'] = df_pivotted['F'] / total
df_pivotted['M_PERC'] = df_pivotted['M'] / total

df_pivotted['CO_GRUPO'] = pd.to_numeric(df_pivotted['CO_GRUPO'])

df_sorted = df_pivotted.sort_values(by='M_PERC')
df_sorted['CO_GRUPO_DESC'] = df_sorted['CO_GRUPO'].replace(cursos_values)

ax = df_sorted.plot.barh(figsize=(19.2, 10.8),
                         x='CO_GRUPO_DESC',
                         y=['F_PERC', 'M_PERC'],
                         color=['#A0DA39', '#1FA187'],
                         xlabel='',
                         rot=0,
                         stacked=True,
                         fontsize='14')

plt.title('\nPorcentagem de gênero por curso\n',
          fontsize=20,
          va='top',
          x=0.425)

ax.grid(axis='x')

ax.set(xlim=[0, 1])
plt.legend(prop={'size': 18}, handles=[
    mpatches.Patch(color='#A0DA39', label='Feminino'),
    mpatches.Patch(color='#1FA187', label='Masculino'),
])

cursos_valores = [x[1].F_PERC for x in df_sorted.iterrows()]
for i, v in enumerate(cursos_valores):
    if (v > .98): continue
    ax.text(v + .005, i, "{:2.2f}%%".format(100 * v), color='k', fontsize=12, fontweight='bold', va='center')

plt.tight_layout()
plt.show()
