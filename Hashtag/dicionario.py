#criando um dicionário
empresa = {
    "nome": "joao", #nome = chave, joao = item
    "idade": 20     #idade = chave, 20 = item
}
print(empresa)

#substituir um item 'valor'
empresa['nome'] = 'x'
print(empresa)

#adicionar uma nova chave
empresa['email'] = 'bola@if.vbf'
print(empresa)

#checagem do nome da chave em chaves
print('ano' in empresa)
print('nome' in empresa)

#exibir o valor retornado de uma chave, caso não queria que retorne, como o padrão, none, coloca ('nome', 0) ou ausente
print(empresa.get('idade'))

#exibe as chaves do dicionário
print(empresa.keys())

#exiber os valores do dicionário
print(empresa.values())

#checagem do valores do itens
print('x' in empresa.values())

#exibe tudo que tem no dicionário em forma de tupla
print(empresa.items())

#podemos criar um dicionário a partir de uma lista de tuplas ou uma tuplas de tuplas
exemplo = [('nome', 'pedro'), ('idade', 20)]
exemplo2 = dict(exemplo)
print(exemplo2)