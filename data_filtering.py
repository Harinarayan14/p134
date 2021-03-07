import pandas as pd
import matplotlib.pyplot as plt
# nearer stars (<100 light years)
df = pd.read_csv("gravity_data.csv")
for index, data in enumerate(df["Distance"]):
    if(float(data)>100):
        df.drop(index,inplace=True)
del(df["Unnamed: 0"])
df.to_csv("nearer_stars.csv",index=False)

# far stars (150 to 350 stars)
df2 = pd.read_csv("gravity_data.csv")
for index, data in enumerate(df2["Distance"]):
    if(float(data)<150 or float(data)>350  ):
        df2.drop(index,inplace=True)
del(df2["Unnamed: 0"])
print(df2)
df2.to_csv("far_stars.csv",index=False)