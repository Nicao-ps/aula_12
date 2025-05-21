import pandas as pd

products = ['Notebook', 'Smartphone', 'Tablet', 'Smartwatch', 'Camera']
qtt_stock = [15, 30, 20, 10, 25]

stock = pd.Series(qtt_stock, index=products)

print('Série Estoque de Produtos: ')
print(stock)

print('\nQuantidade de notebooks em estoque: ')
print(stock['Notebook'])

print('\nEstoque de Notebook e Camera: ')
print(stock[['Notebook', 'Camera']].values)

print('\nProdutos com estoque abaixo de 20 unidades: ')
print(stock[stock < 20])

print('\nAumentando o estoque em 5 unidades para todos os produtos: ')
print(stock + 5)

stock.loc['Headphone'] = None
print('\nEstoque com um valor nulo (Headphone): ')
print(stock)

prices = pd.Series([3500, 2500, 1200, 900, 1500], index=products)

print('\nValor total do estoque por produto (preço * quantidade): ')
print(prices * stock)
