import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from data_keys import load_and_prepare_data

data = load_and_prepare_data()

# Agrupa por gênero
df = data.groupby(by=['CO_GRUPO_DESC', 'TP_SEXO']).size().reset_index()

# Pivota a tabela de alunos por gênero
df_pivotted = df.pivot_table(index='CO_GRUPO_DESC', columns='TP_SEXO', values=0).reset_index()

# Porcentagem de alunos com gênero informado
total = df_pivotted['F'] + df_pivotted['M']
df_pivotted['F_PERC'] = df_pivotted['F'] / total
df_pivotted['M_PERC'] = df_pivotted['M'] / total

# Ordena por feminino descrescente
df_sorted = df_pivotted.sort_values(by='F_PERC', ascending=False)

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
    if v > .98: continue
    ax.text(v + .005, i, "{:2.2f}%%".format(100 * v), color='k', fontsize=12, fontweight='bold', va='center')

plt.tight_layout()
plt.show()
plt.close()
