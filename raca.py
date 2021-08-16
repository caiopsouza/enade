import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from data_keys import load_and_prepare_data

#data = load_and_prepare_data()

# Agrupa por raça ou cor
df = data.groupby(by=['CO_GRUPO_DESC', 'QE_I02']).size().reset_index()

# Pivota a tabela de alunos por raça
df_pivotted = df.pivot_table(index='CO_GRUPO_DESC', columns='QE_I02', values=0).reset_index()

# Porcentagem de alunos com raça informada
total = df_pivotted['A'] + df_pivotted['B'] + df_pivotted['C'] + df_pivotted['D'] + df_pivotted['E'] + df_pivotted['F']
for i in ['A', 'B', 'C', 'D', 'E', 'F']:
    df_pivotted[i + '_PERC'] = df_pivotted[i] / total

# Ordena por raça branca descrescente
df_sorted = df_pivotted.sort_values(by='A_PERC', ascending=False)

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
    mpatches.Patch(color='#666666', label='Não declarado'),
])

plt.tight_layout()
plt.show()
plt.close()
