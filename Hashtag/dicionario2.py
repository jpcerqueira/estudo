inventario = {
    'camiseta': {'quantidade': 100, 'preco': 50},
    'calca': {'quantidade': 50, 'preco': 80}
}
#consulta de chaves
print(inventario['camiseta'])

#consulta de chaves dentro de chaves
print(inventario['camiseta']['quantidade'])

#consulta atraves do .get
print(inventario.get('calca').get('preco'))