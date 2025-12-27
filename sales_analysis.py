import csv

total_sales = 0
product_sales = {}

with open("sales_data.csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        price = int(row["price"])

        sales = quantity * price
        total_sales += sales

        if product in product_sales:
            product_sales[product] += sales
        else:
            product_sales[product] = sales

print("Total Sales Amount:", total_sales)
print("\nProduct-wise Sales:")
for product, sales in product_sales.items():
    print(product, ":", sales)
