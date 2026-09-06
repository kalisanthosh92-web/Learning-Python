raw_order = "  oRdEr_ID: #89421-US | CuStOmEr: 'sArAh cOnNoR' | iTeM: \"wireless mechanical keyboard\" | pRiCe: $149.9982 | StAtUs: PENDING  "



#1. cleaning white spaces.
clean_raw_order = raw_order.strip()
parts = clean_raw_order.split('|')



#2.Extracting Order Code & Country.
id = parts[0].split(':')[1].strip()
order_id = id.split('-')[0]
#print(order_id)
#print(type(order_id))

Country = id.split('-')[1]
#print(Country)
#print(type(Country))

#3. Extracting customers name.
Customer_name =  parts[1].split(':')[1].strip().strip('\'').title()
#print(Customer_name)


#4. Format Item Name.
Item_name = parts[2].split(':')[1].strip().strip('\"').title()
#print(Item_name)
#print(type(Item_name))

#5. Formatting Price.
Price = parts[3].split(':')[1].strip().strip('$')
flt_price = float(Price)
rounded_price = round(flt_price, 2)
#print(rounded_price)
#print(type(rounded_price))


#6. Formatting status.
Status = parts[4].split(':')[1].strip()
#print(Status)


print('='*50)
print("ORDER SUMMARY REPORT")
print('='*50)

print(f'Order ID:\t{order_id} (Country: {Country})\nCustomer:\t{Customer_name}\nPurchased:\t{Item_name}\nTotal Paid:\tP{rounded_price}\nStatus: \t{Status}\n')

print('='*50)
