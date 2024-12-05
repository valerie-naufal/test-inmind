import numpy as np
import pandas as pd 

# dataset = {
#     'names': ["val", "jad", "ray"],
#     'major': ["coe","cs","mkt"]
# }

# varseries = [1,4,8]

# myvar = pd.DataFrame(dataset)
# ser = pd.Series(varseries)

# print(myvar)
# print(ser)
# print(ser[1])

data = {
    'calories':[420,380,390],
    'duration':[50,40,45]
}

df = pd.DataFrame(data, index = ["day1","day2","day3"])

print(df)
print(df.loc["day2"])
print(df.tail(2))