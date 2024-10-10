import pandas as pd

df = pd.DataFrame({
    'frutas': ['maçã', 'banana', 'laranja', 'uva', 'pera'],
    'quantidade': [3, 2, 3, 1, 4]
})

df = pd.notnull(df.pivot(columns='frutas'))


print(df)