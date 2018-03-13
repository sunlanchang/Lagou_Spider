import pandas as pd
df = pd.DataFrame({"A": ["foo", "foo", "foo", "bar"], "B": [
                  0, 1, 1, 1], "C": ["A", "A", "B", "A"]})
print(df)
df2 = df.drop_duplicates(subset=['A', 'C'], keep=False)
print(df2)
