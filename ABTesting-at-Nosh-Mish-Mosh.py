"""
Codecademy Project - A/B Testing at Nosh Mish Mosh
Project Goal: Determine a sample size for a new experiment 
"""
import noshmishmosh
import numpy as np
import math

all_visitors = noshmishmosh.customer_visits
total_visitor_count = float(len(noshmishmosh.customer_visits))

paying_visitors = noshmishmosh.purchasing_customers
paying_visitor_count = len(paying_visitors)

baseline_percent = (paying_visitor_count/total_visitor_count)*100

print("Baseline Conversion Rate = " + str(baseline_percent)+" %")
payment_history = noshmishmosh.money_spent
average_payment = float(np.mean(payment_history))
new_customers_needed = np.ceil(1240 / average_payment)
print("Number of new customers needed = " + str(math.trunc(new_customers_needed)))

percent_point_increase = (new_customers_needed * 100.0) / total_visitor_count

print("New Customers required as a percent of total visitors = " + str(percent_point_increase) + " %")

minimum_detectable_effect = float((percent_point_increase * 100.0) / baseline_percent)

print("Minimum Detectable Effect = " + str(round(minimum_detectable_effect, 2)) + " %")

statistical_significance_percent = 90
print("Statistical Significance = "+ str(statistical_significance_percent)+ " %")

"""
Based on the output from the calculator
"""
ab_sample_size = 290

print("The number of people (sample size) need to see the artisanal-looking vegetable section is " + str(ab_sample_size))
