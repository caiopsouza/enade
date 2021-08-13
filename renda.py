import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    df.drop(df[df.QE_I04 == ' '].index, inplace=True)
    df.drop(df[df.QE_I05 == ' '].index, inplace=True)

    return df


def count_and_rename_labels(df, labels, normalize=False):
    return df \
        .value_counts(normalize=normalize) \
        .sort_index() \
        .rename(labels)


def plot_pie(df, labels, title):
    print(df)

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

    plt.suptitle(f'Quantidade total de alunos: {df.count() / 2}',
                 fontsize=14,
                 ha='center',
                 va='baseline',
                 x=mid,
                 y=.85)

    ax.legend(title='Escolaridade',
              labels=labels.values(),
              labelcolor='#303030',
              loc="center left",
              bbox_to_anchor=(-.35, .5))

    plt.tight_layout()
    plt.show()


#data = load_and_prepare_data()

renda_familiar_labels = {
    'A': 'Nenhuma',
    'B': 'Fundamental até o 5º',
    'C': 'Fundamental até o 9º',
    'D': 'Médio',
    'E': 'Superior',
    'F': 'Pós-graduação',
}

plot_pie(pd.concat([data.QE_I04, data.QE_I05]), renda_familiar_labels, 'Renda familiar todos os cursos')

'''renda_medicina = data[data.CO_GRUPO == 23].QE_I08
plot_pie(renda_medicina, renda_familiar_labels, 'Renda familiar: Curso de Enfermagem')

renda_medicina = data[data.CO_GRUPO == 12].QE_I08
plot_pie(renda_medicina, renda_familiar_labels, 'Renda familiar: Curso de Medicina')'''
