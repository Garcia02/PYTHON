import pandas as pd

# Criando um DataFrame de exemplo
df = pd.DataFrame({
    'frutas': ['maçã', 'banana', 'laranja', 'uva', 'pera'],
    'quantidade': [3, 2, 5, 1, 4]
})

selection = ["banana","uva"]

df = df[df['frutas'].isin(selection)]


print(2>=3)