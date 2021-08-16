import plot
from data_keys import renda_colors, renda_familiar_names, load_and_prepare_data

data = load_and_prepare_data()

legend = 'Salários mínimos\n(Ano ref. 2018, R$ 945,00)'
bbox_to_anchor = (-.35, .5)

plot.pie(data.QE_I08,
         renda_familiar_names,
         'Renda familiar: Todos os cursos',
         legend,
         bbox_to_anchor)

renda_medicina = data[data.CO_GRUPO == 23].QE_I08
plot.pie(renda_medicina,
         renda_familiar_names,
         'Renda familiar: Curso de Enfermagem',
         legend,
         bbox_to_anchor)

renda_medicina = data[data.CO_GRUPO == 12].QE_I08
plot.pie(renda_medicina,
         renda_familiar_names,
         'Renda familiar: Curso de Medicina',
         legend,
         bbox_to_anchor)
