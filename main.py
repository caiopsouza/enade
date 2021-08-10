import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

renda_familiar = 'QE_I08'
renda_familiar_labels = {
    'A': 'Até 1,5\n(até R$ 1.431,00)',
    'B': 'De 1,5 a 3\n(R$ 1.431,01 \na R$ 2.862,00)',
    'C': 'De 3 a 4,5\n(R$ 2.862,01 \na R$ 4.293,00)',
    'D': 'De 4,5 a 6\n(R$ 4.293,01 \na R$ 5.724,00)',
    'E': 'De 6 a 10\n(R$ 5.724,01 \na R$ 9.540,00)',
    'F': 'De 10 a 30\n(R$ 9.540,01 \na R$ 28.620,00)',
    'G': 'Acima de 30\n(mais de\nR$ 28.620,00)',
    'N': 'Não informado'
}

ax = df[renda_familiar] \
    .value_counts() \
    .rename({' ': 'N'}) \
    .sort_index() \
    .rename(renda_familiar_labels) \
    .plot.pie(figsize=(12.8, 8),
              cmap='viridis',
              labels=[''] * len(renda_familiar_labels),
              ylabel='',
              autopct='%.2f%%',
              textprops={'backgroundcolor': (1, 1, 1, 0.5), 'color': '#303030'})

plt.title('Renda familiar do estudante segundo ENADE 2019',
          fontsize=18,
          loc='center',
          position=(.25, 0))

ax.legend(title='Salários mínimos\n(Ano ref. 2018, R$ 954,00)',
          labels=renda_familiar_labels.values(),
          labelcolor='#303030',
          loc="center left",
          bbox_to_anchor=(-.35, .5))

plt.show()
plt.close()
