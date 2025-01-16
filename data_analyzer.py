import pandas as pd

data = pd.read_csv("data.csv")
summary = data.describe()
print(summary)

summary.to_html("summary.html")