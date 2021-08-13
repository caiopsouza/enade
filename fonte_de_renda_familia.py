import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    df.drop(df[df.QE_I08 == ' '].index, inplace=True)
    df.drop(df[df.QE_I09 == ' '].index, inplace=True)

    return df


def plot_pie(df, labels, title):
    ax = count_and_rename_labels(df, labels) \
        .plot.pie(figsize=(12.8, 8),
                  colors=renda_colors,
                  labels=[''] * len(labels),
                  ylabel='',
                  autopct='%.2f%%',
                  textprops={'backgroundcolor': (1, 1, 1, 0.5), 'color': '#303030'})

    mid = (ax.figure.subplotpars.right + ax.figure.subplotpars.left) / 2

    plt.title(title,
              fontsize=20,
              ha='center',
              va='baseline',
              x=mid)

    plt.suptitle(f'Quantidade total de alunos: {df.count()}',
                 fontsize=14,
                 ha='center',
                 va='baseline',
                 x=mid,
                 y=.85)

    ax.legend(title='Situação finaceira',
              labels=labels.values(),
              labelcolor='#303030',
              loc="center left",
              bbox_to_anchor=(-.45, .5))

    plt.tight_layout()
    # plt.show()
    plt.savefig('plots/situacao-finaceira-familia.png', transparent=True)


valores_08 = {
    'A': 'Até 1,5',
    'B': 'De 1,5 a 3',
    'C': 'De 3 a 4,5',
    'D': 'De 4,5 a 6',
    'E': 'De 6 a 10',
    'F': 'De 10 a 30',
    'G': 'Acima de 30',
}

valores_09 = {
    'A': 'Sem renda.\nGastos financiados\npor programas\ngovernamentais.',
    'B': 'Sem renda.\nGastos financiados\npor família ou outros.',
    'C': 'Com renda.\nRecebe ajuda\nda família ou outros.',
    'D': 'Com renda.\nNão recebe ajuda\ncom gastos.',
    'E': 'Com renda.\nContribue com\ngastos da família.',
    'F': 'Principal responsável\npelo sustento da família.',
}

#data = load_and_prepare_data()

data_grouped = data.groupby(by=['QE_I08', 'QE_I09']).size()
#data_grouped = data_grouped / data_grouped.groupby(by=['QE_I08']).sum()
data_grouped = data_grouped.reset_index()

data_grouped.QE_I08.replace(valores_08, inplace=True)
data_grouped.QE_I09.replace(valores_09, inplace=True)

data_sorted = data_grouped

ax = data_sorted.plot.scatter(
    x='QE_I08',
    y='QE_I09',
    s=data_sorted[0],
    figsize=(19.2, 10.8),
    fontsize=16,
)

plt.title('Comparativo da renda pessoal e familiar\n', fontsize=20)
plt.xlabel('')
plt.ylabel('')

plt.tight_layout()
#plt.show()
plt.savefig('plots/situacao-finaceira-comparativo.png', transparent=True)

