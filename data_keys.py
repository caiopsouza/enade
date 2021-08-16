import pandas as pd

renda_colors = [
    '#440154',
    '#46327E',
    '#365C8D',
    '#277F8E',
    '#1FA187',
    '#4AC16D',
    '#A0DA39',
    # '#FDE725',
]

cursos_names = {
    0: 'Geral',
    5: 'Veterinária',
    6: 'Odontologia',
    12: 'Medicina',
    17: 'Agronomia',
    19: 'Farmácia',
    21: 'Arquitetura e Urbanismo',
    23: 'Enfermagem',
    27: 'Fonoaudiologia',
    28: 'Nutrição',
    36: 'Fisioterapia',
    51: 'Zootecnia',
    55: 'Biomedicina',
    69: 'Tec. em Radiologia',
    90: 'Tec. em Agronegócios',
    91: 'Tec. em Gestão Hospitalar',
    92: 'Tec. em Gestão Ambiental',
    95: 'Tec. em Estética e Cosmética',
    3501: 'Educação Física (Bacharelado)',
    4003: 'Eng. da Computação',
    5710: 'Eng. Civil',
    5806: 'Eng. Elétrica',
    5814: 'Eng. de Controle e Automação',
    5902: 'Eng. Mecânica',
    6002: 'Eng. de Alimentos',
    6008: 'Eng. Química',
    6208: 'Eng. de Produção',
    6307: 'Eng. Ambiental',
    6405: 'Eng. Florestal',
    6410: 'Tec. em Segurança no Trabalho',
}

escolaridade_names = {
    'A': 'Nenhuma',
    'B': 'Fundamental até o 5º',
    'C': 'Fundamental até o 9º',
    'D': 'Médio',
    'E': 'Superior',
    'F': 'Pós-graduação',
}

renda_familiar_names = {
    'A': 'Até 1,5',
    'B': 'De 1,5 a 3',
    'C': 'De 3 a 4,5',
    'D': 'De 4,5 a 6',
    'E': 'De 6 a 10',
    'F': 'De 10 a 30',
    'G': 'Acima de 30',
}

situacao_financeira_names = {
    'A': 'Sem renda.\nGastos financiados\npor programas\ngovernamentais.',
    'B': 'Sem renda.\nGastos financiados\npor família ou outros.',
    'C': 'Com renda.\nRecebe ajuda\nda família ou outros.',
    'D': 'Com renda.\nNão recebe ajuda\ncom gastos.',
    'E': 'Com renda.\nContribue com\ngastos da família.',
    'F': 'Principal responsável\npelo sustento da família.',
}


def load_and_prepare_data():
    df = pd.read_csv('data/microdados_enade_2019/3.DADOS/microdados_enade_2019.txt', sep=";")

    df['CO_GRUPO'] = pd.to_numeric(df['CO_GRUPO'])
    df['CO_GRUPO_DESC'] = df['CO_GRUPO'].replace(cursos_names)

    # Remove raça ou cor não informada
    df.drop(df[df.QE_I02 == ' '].index, inplace=True)

    # Remove escolaridade não informada do pai ou mãe
    df.drop(df[df.QE_I04 == ' '].index, inplace=True)
    df.drop(df[df.QE_I05 == ' '].index, inplace=True)

    # Remove renda familiar e pessoal não informada
    df.drop(df[df.QE_I08 == ' '].index, inplace=True)
    df.drop(df[df.QE_I09 == ' '].index, inplace=True)

    return df
