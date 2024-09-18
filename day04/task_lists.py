# Lists in Python

states_of_brazil = [ "acre", "alagoas", "amapa", "amazonas", "bahia", "ceara", "distrito-federal", "espirito-santo", "goias", "maranhao", "mato-grosso-do-sul", "mato-grosso", "minas-gerais", "para", "paraiba", "parana", "pernambuco", "piaui", "rio-de-janeiro", "rio-grande-do-norte", "rio-grande-do-sul", "rondonia", "roraima", "santa-catarina", "sao-paulo", "sergipe", "tocantins" ]

acronym = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MS','MT','MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO',]

print(states_of_brazil[0]) # First
print(states_of_brazil[-1]) # Last

brazil = [states_of_brazil, acronym]
print(brazil)


# print: sao-paulo and SP
print(f"{brazil[0][-3]} - {brazil[1][-3]}")