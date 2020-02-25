import math

# --- Display a greeting ---

greeting = "Hello "
name = "Sergej"
print(greeting + name)


# --- Calculate the yearly income ---

hourly_wage = 10
hours_per_week = 40
weeks_per_year = 46
income_per_week = hourly_wage * hours_per_week
income_per_year = income_per_week * weeks_per_year
print(name + "'s yearly income is: ${0}".format(income_per_year) )


# --- Calculate yearly spend ---

spend_rent_per_month = 750
spend_petrol_per_week = 20
spend_food_per_week = 40

total_spend = spend_rent_per_month + (spend_food_per_week * 4) + (spend_petrol_per_week * 4)
print(name + "'s yearly spend is: ${0}".format(total_spend) )


# --- Calculate yearlt savings --- 

savings_per_year = income_per_year - total_spend
print(" - - - - - - - ")
print("You manage to save: ${0}".format(savings_per_year) )
