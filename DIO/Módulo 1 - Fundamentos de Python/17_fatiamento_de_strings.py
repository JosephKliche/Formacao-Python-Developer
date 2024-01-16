# Fatiamento

nome = "Guilherme Arthur de Carvalho"

nome [0]
# >>> "G"

nome [:9]
# >>> "Guilherme"

nome [10:]
# >>> "Arthur de Carvalho"

nome [10:16]
# >>> "Arthur"

nome [10:16:2]
# >>> "Atu"

nome [:]
# >>> "GGuilherme Arthur de Carvalho"

nome [:: -1]
# >>> "ohlavraC ed ruhtrA emrehliuG"