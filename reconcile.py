import pandas as pd
internal_data = pd.DataFrame({
    'Trade_ID': [1, 2, 3, 4, 5],
    'Amount': [100000, 250000, 175000, 
300000, 225000],
    'Currency': ['USD', 'EUR', 'GBP',
'USD', 'EUR']
})
external_data = pd.DataFrame({
    'Trade_ID': [1, 2, 3, 4, 6],
    'Amount': [100000, 250000, 180000,
300000, 50000],
    'Currency': ['USD', 'EUR', 'GBP',
'USD', 'EUR']
})
print(internal_data)
print(external_data)