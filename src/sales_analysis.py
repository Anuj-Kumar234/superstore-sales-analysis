# total_recordsing total records and checking what columns are present there in the csv
import csv
from utils import top_n


with open("data/superstore.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    total_records = 0
    header = next(reader)
    for i in reader:
        total_records+= 1
    print("Total records: ",total_records)
    print(header)
    print(len(header))


# Total Sales
with open("data/superstore.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    total_sales = 0
    next(reader)
    for row in reader :
        total_sales += float(row[-1])
    print(f"Total Sales : ${total_sales:,.2f}")



#Average of sales
with open("data/superstore.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    average = total_sales / float(total_records)
    print(f"Average : ${average:,.2f}")



#Finding best performing category
with open("data/superstore.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    category_sales = {}
    next(reader)
    for row in reader:
        category_sales[row[-4]] = category_sales.get(row[-4], 0) + float(row[-1])   #row[-1] is sales column and row[-4] is category column
    
    print("\nCategory Sales :")
    for category,sale in category_sales.items():
        print(f"{category.title()}- ${sale:,.2f}")
    
    print("\nBest Category:")
    best_category = max(category_sales,key=category_sales.get)
    print(best_category)



#Finding the best performing state
with open("data/superstore.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    state_sales = {}
    for row in reader:
        state = row[10]
        sales = row[-1]
        state_sales[state] = state_sales.get(state,0) + float(sales)
    
    print('\nBest Performing State:')
    best_performing_state = max(state_sales,key=state_sales.get)

    print(f"{best_performing_state} - ${state_sales[best_performing_state]:,.2f}")

    # TOP 5 PERFORMING STATES
    print("\nTop 5 Performing States:")
    top_5 = top_n(state_sales,5)
    for i,tup in enumerate(top_5):
        print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")
    

#Customers by Revenue
with open("data/superstore.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    customer_revenue = {}
    for row in reader:
        name = row[6]
        sales = row[-1]
        customer_revenue[name] = customer_revenue.get(name,0) + float(sales)

    #Top 5 Customers by Revenue   
    print("\nTop 5 Customers:")
    top_customers = top_n(customer_revenue,5)
    
    for i,tup in enumerate(top_customers):
        print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")


#Top Regions by Revenue
with open("data/superstore.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    region_revenue = {}
    for row in reader:
        name = row[12]
        sales = row[-1]
        region_revenue[name] = region_revenue.get(name,0) + float(sales)

    #Top 5 Regions by Revenue   
    print("\nTop 5 Regions:")
    top_regions = top_n(region_revenue,5)
    
    for i,tup in enumerate(top_regions):
        print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")


#Top Segments by Revenue
with open("data/superstore.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    segments_revenue ={}
    for row in reader:
        name = row[7]
        sales = row[-1]
        segments_revenue[name] = segments_revenue.get(name,0) + float(sales)

    #Top 5 Segments by Revenue   
    print("\nTop 5 Segments:")
    top_segments = top_n(segments_revenue,5)
    
    for i,tup in enumerate(top_segments):
        print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")

#Top Products by Revenue
with open("data/superstore.csv","r",encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    product_revenue = {}
    for row in reader:
        name = row[16]
        sales = row[-1]
        product_revenue[name] = product_revenue.get(name,0) + float(sales)

    #Top 5 Products by Revenue   
    print("\nTop 5 Products:")
    top_products = top_n(product_revenue,5)
    
    for i,tup in enumerate(top_products):
        print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")

print("\n===== BUSINESS INSIGHTS =====")

print(f"Highest Revenue Category: {best_category}")
print(f"Best State: {best_performing_state}")
print(f"Top Customer: {top_customers[0][0]}")