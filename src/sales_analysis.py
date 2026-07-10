#Recording total records and checking what columns are present there in the csv
from utils import top_n , load_data , aggregate

data = load_data("../data/superstore.csv")
total_records = 0
header = data[0]
for i in data[1:]:
    total_records+= 1
print("Total records: ",total_records)
print(header)
print(len(header))

# Total Sales
total_sales = 0
    
for row in data[1:] :
    total_sales += float(row[-1])
print(f"Total Sales : ${total_sales:,.2f}")



#Average of sales
average = total_sales / float(total_records)
print(f"Average : ${average:,.2f}")



#Finding best performing category
category_sales = aggregate(data, 14, 17)
print("\nCategory Sales :")
for category,sale in category_sales.items():
    print(f"{category.title()}- ${sale:,.2f}")
    
print("\nBest Category:")
best_category = max(category_sales,key=category_sales.get)
print(best_category)



#Finding the best performing state
state_sales= aggregate(data,10,17)

print('\nBest Performing State:')
best_performing_state = max(state_sales,key=state_sales.get)

print(f"{best_performing_state} - ${state_sales[best_performing_state]:,.2f}")

# TOP 5 PERFORMING STATES
print("\nTop 5 Performing States:")
top_5 = top_n(state_sales,5)
for i,tup in enumerate(top_5):
    print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")
    

#Customers by Revenue
customer_revenue = aggregate(data, 6, 17)

    #Top 5 Customers by Revenue   
print("\nTop 5 Customers:")
top_customers = top_n(customer_revenue,5)
    
for i,tup in enumerate(top_customers):
    print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")


#Top Regions by Revenue
region_revenue = aggregate(data, 12, 17)

#Top 5 Regions by Revenue   
print("\nTop 5 Regions:")
top_regions = top_n(region_revenue,5)
    
for i,tup in enumerate(top_regions):
    print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")


#Top Segments by Revenue
segments_revenue = aggregate(data,7,-1)
#Top 5 Segments by Revenue   
print("\nTop 5 Segments:")
top_segments = top_n(segments_revenue,5)
    
for i,tup in enumerate(top_segments):
    print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")

#Top Products by Revenue

product_revenue = aggregate(data,16,-1)

#Top 5 Products by Revenue   
print("\nTop 5 Products:")
top_products = top_n(product_revenue,5)
    
for i,tup in enumerate(top_products):
    print(f"{i+1}. {tup[0]} - ${tup[1]:,.2f}")

print("\n===== BUSINESS INSIGHTS =====")

print(f"Highest Revenue Category: {best_category}")
print(f"Best State: {best_performing_state}")
print(f"Top Customer: {top_customers[0][0]}")