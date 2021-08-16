import plot
from data_keys import situacao_financeira_names, load_and_prepare_data

data = load_and_prepare_data()

plot.pie(data.QE_I09,
         situacao_financeira_names,
         'Situação financeira todos os cursos',
         'Situação finaceira',
         (-.45, .5))
