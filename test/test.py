import pandas as pd

df1 = pd.DataFrame({'A': ['aa', 'bb'],
                    'M': ['cc', 'dd'],
                    'C': ['ee', 'ff']})
print(df1)

value1 = df1.at[0, 'C']
print(value1)

value2 = df1.at[1, 'A']
print(value2)