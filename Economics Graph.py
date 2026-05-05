import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

x = [2020, 2021, 2022, 2023, 2024]
y = [160,170, 225,280,281]

plt.plot(x, y, color="r", marker="o", label="Line Graph")

# Force x-axis ticks to show only the year values.
plt.xticks(x, [str(year) for year in x])

plt.xlabel("Year")
plt.ylabel("Exchange Rate (USD to PKR)")

# Format y-axis tick labels as PKR for readability.
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda value, _: f"PKR {value:,.0f}"))

plt.title("Economics Graph")
plt.legend()
plt.show()