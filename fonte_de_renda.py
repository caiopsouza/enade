import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    df.drop(df[df.QE_I08 == ' '].index, inplace=True)
    df.drop(df[df.QE_I09 == ' '].index, inplace=True)

    return df


def count_and_rename_labels(df, labels, normalize=False):
    return df \
        .value_counts(normalize=normalize) \
        .sort_index() \
        .rename(labels)


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
    plt.savefig('plots/situacao-finaceira.png', transparent=True)


data = load_and_prepare_data()

renda_familiar_labels = {
    'A': 'Sem renda. Gastos financiados\npor programas governamentais.',
    'B': 'Sem renda. Gastos financiados\npor família ou outros.',
    'C': 'Com renda, Rrecebe ajuda\nda família ou outros.',
    'D': 'Com renda.\nNão recebe ajuda com gastos.',
    'E': 'Com renda.\nContribue com gastos da família.',
    'F': 'Principal responsável\npelo sustento da família.',
}

plot_pie(data.QE_I09, renda_familiar_labels, 'Situação financeira todos os cursos')
