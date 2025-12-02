import pandas as pd

df = pd.Dataframe({
    "Name":["venu","madhav","Tanveer"],
    "age":[21,19,20],
    "sex":["male","male","female"]
})

# Each column in a dataframe is a series

ages = pd.Series([22,35,58],name="age")

print(df["age"].max())
print(ages.max())
print(ages.min())

print(df.describe())