#Program 1
for i in range(1,11):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
        
#Program 2
print("-----------------------------------------------------------------------")

import pandas as pd
import numpy as np


data = {
    "Product": ["Pen", "Book", "Pen", "Book"],
    "Category": ["Stationery", "Stationery", "Stationery", "Stationery"],
    "Sales": [100, 200, 150, 300]
}


df = pd.DataFrame(data)

print("Sales Data:")
print(df)

total = np.sum(df["Sales"])
average = np.mean(df["Sales"])

print("\nTotal Sales:", total)
print("Average Sales:", average)

sales = df.groupby("Product")["Sales"].sum()
best = sales.idxmax()

print("Best Selling Product:", best)

print("\nCategory-wise Sales:")
print(df.groupby("Category")["Sales"].sum())
