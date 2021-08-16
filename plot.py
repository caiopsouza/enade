import matplotlib.pyplot as plt

from data_keys import renda_colors


def pie(df, labels, title, legend, bbox_to_anchor):
    ax = df \
        .value_counts() \
        .sort_index() \
        .rename(labels) \
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

    ax.legend(title=legend,
              labels=labels.values(),
              labelcolor='#303030',
              loc="center left",
              bbox_to_anchor=bbox_to_anchor)

    plt.tight_layout()
    plt.show()
    plt.close()
