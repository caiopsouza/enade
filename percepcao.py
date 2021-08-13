import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors
import matplotlib.patches as mpatches

columns_questionario = [f'QE_I{c}' for c in range(27, 69)]


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    columns = ['CO_GRUPO'] + columns_questionario
    df = df[columns]

    nan_value = float("NaN")
    df.replace(' ', nan_value, inplace=True)
    df.replace('', nan_value, inplace=True)

    df.replace(7, 1, inplace=True)
    df.replace(7.0, 1, inplace=True)
    df.replace('7', 1, inplace=True)

    df.replace(8, 1, inplace=True)
    df.replace(8.0, 1, inplace=True)
    df.replace('8', 1, inplace=True)

    df.dropna(inplace=True)

    df = df.apply(pd.to_numeric)
    df[columns_questionario] = df[columns_questionario] - 1

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

data['total'] = data[columns_questionario].sum(axis=1)
df = data[['CO_GRUPO', 'total']]

nota_mean = df.total.mean()

color_less_than = '#EB548C'
color_greater_than = '#29066B'
color_equal_to = '#AF4BCE'


def color(v):
    if v < nota_mean:
        return color_less_than
    if v > nota_mean:
        return color_greater_than
    return color_equal_to


df = df \
    .groupby(by='CO_GRUPO') \
    .mean() \
    .reset_index()

df['CO_GRUPO'] = df['CO_GRUPO'].replace(cursos_values)

nota_geral = pd.DataFrame([['Geral', nota_mean]], columns=['CO_GRUPO', 'total'], index=[29])
df = df.append(nota_geral)

df = df.sort_values(by='total', ascending=False)

cursos_valores = [x[1].total for x in df.iterrows()]
cursos_colors = [color(x) for x in cursos_valores]

ax = df.plot.barh(figsize=(19.2, 10.8),
                  color=cursos_colors,
                  x='CO_GRUPO',
                  y='total',
                  xlabel='',
                  rot=0,
                  fontsize='14')

mid = (ax.figure.subplotpars.right + ax.figure.subplotpars.left) / 2
ax.grid(axis='x')
ax.set(xlim=[145, 185])

plt.title('Satisfação média por curso\n\n',
          fontsize=20,
          va='top',
          x=0.425)

plt.suptitle(f'Notas entre 0 e 210',
                 fontsize=14,
                 ha='center',
                 va='baseline',
                 x=mid,
                 y=.9)

for i, v in enumerate(cursos_valores):
    ax.text(v + .05, i, "{:2.2f}".format(v), color=cursos_colors[i], fontsize=12, fontweight='bold', va='center')

plt.legend(prop={'size': 18}, handles=[
    mpatches.Patch(color=color_less_than, label='Menor que a média geral'),
    mpatches.Patch(color=color_equal_to, label='Satisfação média geral'),
    mpatches.Patch(color=color_greater_than, label='Maior que a média geral'),
])

plt.tight_layout()
plt.show()
