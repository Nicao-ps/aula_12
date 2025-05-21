import pandas as pd

subjects = ['Brazilian Lit.', 'Foreign Lit.', 'Science', 'Math', 'History']
qtt_stock = [12, 9, 18, 14, 20]
qtt_books = [4, 2, 7, 5, 6]

stock = pd.Series(qtt_stock, index=subjects)
books = pd.Series(qtt_books, index=subjects)
stock.loc['Filosofy'] = None
print((stock - books)[stock > 5])
