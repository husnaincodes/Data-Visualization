import pandas as pd
import matplotlib.pyplot as plt

data  = pd.read_csv("data_visualization_dataset.csv")
plt.bar(data["Sales_Units"],data["Revenue_USD"])

plt.xlabel("Sales_Units")
plt.ylabel("Revenue_USD")

plt.title("Weekly Sales")
plt.show()