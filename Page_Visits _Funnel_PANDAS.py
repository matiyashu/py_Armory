import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
#print(visits)
#print(cart)
#print(checkout)
#print(purchase)

#2 combine visits and cart using left merge
visits_cart_merged = pd.merge(visits, cart, how='left')
#print(visits_cart_merged)
visits_cart_rows = len(visits_cart_merged)
#print(visits_cart_rows)
null_cart_timestamps = len(visits_cart_merged[visits_cart_merged.cart_time.isnull()])
#percentage of users who visited the website but didn't place an order
print(float(null_cart_timestamps) / visits_cart_rows)

#6 repeat left merge for cart and checkout and count null values
cart_checkout = pd.merge(cart, checkout, how = 'left')
#print(cart_checkout)
cart_checkout_rows = len(cart_checkout)
#print(cart_checkout_rows)
null_checkout_times = len(cart_checkout[cart_checkout.checkout_time.isnull()])
#percentage of users that put items in their cart but didn't checkout
print(float(null_checkout_times) / cart_checkout_rows)

#7 Merge all dataframes in order, using a series of left merges. Save it to 
#the variable all_data
all_data = visits.merge(cart, how = 'left')\
								 .merge(checkout, how='left')\
								 .merge(purchase, how = 'left')
#print(all_data.head())

#10 calculate the average time from initial visit to final purchase
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
#print(all_data.head())
print(all_data.time_to_purchase.mean())
