import pandas
import matplotlib.pyplot as plt

# Step 1: Reading CSV File
df = pandas.read_csv(r'C:\Users\rudmi\Downloads\Data.csv')
print(df)

# Step 2: Total Sale
total_sales = df.sum()[1:].tolist()
years = df.columns[1:].tolist()
with open('stats.txt', 'w') as f:
    f.write('Total sales per year:\n')
    for i, year in enumerate(years):
        f.write(f"{year}: {total_sales[i]}\n")

# Step 3: Bar Plot
plt.bar(years, total_sales)
plt.title('Total Sales Per Year')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.show()

# Step 4: Sale Estimation
sales_2021 = df.loc[df['Year'] == 2021].iloc[:, 1:].sum().tolist()
sales_2022 = df.loc[df['Year'] == 2022].iloc[:, 1:7].sum().tolist()
total_sales_2021 = sum(sales_2021)
total_sales_2022 = sum(sales_2022)
SGR = (total_sales_2022 - total_sales_2021) / total_sales_2021
estimated_sales_2022 = [sales_2021[i] + sales_2021[i] * SGR for i in range(6)]
with open('stats.txt', 'a') as f:
    f.write(f"\nSGR: {SGR:.2%}\n")
    f.write('Estimated sales for last six months of 2022:\n')
    for i, month in enumerate(df.columns[7:]):
        f.write(f"{month} - {estimated_sales_2022[i]:.0f}\n")

# Step 5: Horizontal Bar Plot
months = df.columns[7:]
plt.barh(months, estimated_sales_2022)
plt.title('Estimated Sales for Last Six Months of 2022')
plt.xlabel('Total Sales')
plt.ylabel('Month')
plt.show()
