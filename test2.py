import pandas as pd
observation = [1, 2, 3, 4, 5]
variable = [3.55, 3.4, 3.60, 4.02, 3.11]
df = pd.DataFrame({
    'Observation': observation,
    'Variable': variable
})

df.to_csv('Test_DF.csv', index=False)