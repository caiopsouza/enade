import matplotlib.pyplot as plt
import pandas as pd
from charts_params import renda_colors


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    df.drop(df[df.QE_I08 == ' '].index, inplace=True)

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

    plt.suptitle(f'Quantidade total de alunos: {df.count()}\nRenda mediana: 3.75 (R$ 3577,50)',
                 fontsize=14,
                 ha='center',
                 va='baseline',
                 x=mid,
                 y=.81)

    ax.legend(title='Salários mínimos\n(Ano ref. 2018, R$ 954,00)',
              labels=labels.values(),
              labelcolor='#303030',
              loc="center left",
              bbox_to_anchor=(-.35, .5))

    plt.tight_layout()
    plt.show()


#data = load_and_prepare_data()

renda_familiar_labels = {
    'A': 'Até 1,5\n(até R$ 1.431,00)',
    'B': 'De 1,5 a 3\n(R$ 1.431,01 \na R$ 2.862,00)',
    'C': 'De 3 a 4,5\n(R$ 2.862,01 \na R$ 4.293,00)',
    'D': 'De 4,5 a 6\n(R$ 4.293,01 \na R$ 5.724,00)',
    'E': 'De 6 a 10\n(R$ 5.724,01 \na R$ 9.540,00)',
    'F': 'De 10 a 30\n(R$ 9.540,01 \na R$ 28.620,00)',
    'G': 'Acima de 30\n(mais de\nR$ 28.620,00)'
}

plot_pie(data.QE_I08, renda_familiar_labels, 'Renda familiar todos os cursos')

'''renda_medicina = data[data.CO_GRUPO == 23].QE_I08
plot_pie(renda_medicina, renda_familiar_labels, 'Renda familiar: Curso de Enfermagem')

renda_medicina = data[data.CO_GRUPO == 12].QE_I08
plot_pie(renda_medicina, renda_familiar_labels, 'Renda familiar: Curso de Medicina')'''
