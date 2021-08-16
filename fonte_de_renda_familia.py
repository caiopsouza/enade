import matplotlib.pyplot as plt
from data_keys import load_and_prepare_data, situacao_financeira_names, renda_familiar_names

data = load_and_prepare_data()

df = data.groupby(by=['QE_I08', 'QE_I09']).size()
df = df.reset_index()

df['QE_I08_DESC'] = df['QE_I08'].replace(renda_familiar_names)
df['QE_I09_DESC'] = df['QE_I09'].replace(situacao_financeira_names)

ax = df.plot.scatter(
    x='QE_I08_DESC',
    y='QE_I09_DESC',
    s=df[0],
    figsize=(19.2, 10.8),
    fontsize=16,
)

plt.title('Comparativo da renda pessoal e familiar\n', fontsize=20)
plt.xlabel('\nSalários mínimos (Ano ref. 2018, R$ 954,00)', fontsize=16)
plt.ylabel('')

plt.tight_layout()
plt.show()
plt.close()
