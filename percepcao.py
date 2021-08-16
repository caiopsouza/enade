import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.patches as mpatches

from data_keys import load_and_prepare_data, cursos_names

columns_questionario = [f'QE_I{c}' for c in range(27, 69)]


def load_and_prepare_questionario_data():
    df = load_and_prepare_data()

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


data = load_and_prepare_questionario_data()

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

df['CO_GRUPO'] = df['CO_GRUPO'].replace(cursos_names)

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
plt.close()
