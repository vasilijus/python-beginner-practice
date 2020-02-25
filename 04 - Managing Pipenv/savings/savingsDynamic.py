import math

# --- Display a greeting ---
print("Hello, please enter your name: ")
greeting = "Hello "
name = input()
print(greeting + name)

print("Please enter how much you earn, work hours, weeks per year")
print("Example format: 10, 40, 52")
wage = input()
wage_arr = wage.split(',')
wage_arr_int = []
for num in wage_arr:
    wage_arr_int.append( int(num) )

hourly_wage = 0
hours_per_week = 0
weeks_per_year = 0
income_per_year = 0
# --- Calculate the yearly income ---
def calc_income(wage, hours_p_w, weeks_p_y):
    hourly_wage = wage
    hours_per_week = hours_p_w
    weeks_per_year = weeks_p_y
    income_per_week = hourly_wage * hours_per_week
    income_per_year = income_per_week * weeks_per_year
    return income_per_year

calc_income(wage_arr_int[0], wage_arr_int[1], wage_arr_int[2])
print(name + "'s yearly income is: ${0}".format(income_per_year) )

# hourly_wage = 10
# hours_per_week = 40
# weeks_per_year = 46
# income_per_week = hourly_wage * hours_per_week
# income_per_year = income_per_week * weeks_per_year
# print(name + "'s yearly income is: ${0}".format(income_per_year) )

print(" --- ")

print("Please enter how much you Spend: Rent (p/m) , Petrol (p/w) , Food (p/w)")
print("Example format: 500, 100, 80")
spent = input()
spent_arr = spent.split(',')
spent_arr_int = []
for amount in spent_arr:
    spent_arr_int.append( int(amount) )
    print( int(amount))

print(spent_arr_int)

print(" --- ")

spend_rent_per_month = 0
spend_petrol_per_week = 0
spend_food_per_week = 0
total_spend_per_year = 0
# --- Calculate yearly spend ---
def calc_spend(rent_p_m, petro_p_w, food_p_w):
    spend_rent_per_month = rent_p_m
    print("spend_rent_per_month: " + str(spend_rent_per_month) )
    spend_petrol_per_week = petro_p_w
    print("spend_petrol_per_week: " + str(spend_petrol_per_week) )
    spend_food_per_week = food_p_w
    print("spend_food_per_week: " + str(spend_food_per_week) )
    total_spend_per_month = spend_rent_per_month + (spend_food_per_week * 4) + (spend_petrol_per_week * 4)
    print("total_spend_per_month: " + str(total_spend_per_month) )
    total_spend_per_year = total_spend_per_month * 12
    print("total_spend_per_year*12: " + str(total_spend_per_year) )
    return total_spend_per_year

calc_spend(spent_arr_int[0], spent_arr_int[1], spent_arr_int[2])
print(name + "'s yearly spend is: ${0}".format(total_spend_per_year) )

# spend_rent_per_month = 750
# spend_petrol_per_week = 20
# spend_food_per_week = 40






# --- Calculate yearlt savings --- 

savings_per_year = income_per_year - total_spend_per_year
print(" - - - - - - - ")
print("You manage to save: ${0}".format(savings_per_year) )
