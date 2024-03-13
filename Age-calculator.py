a = int(input("what's your age?: \n"))
year = 365
weeks = 52
month = 12 

time1 = a * year 
time2 = a * weeks 
time3 = a * month 

total_life = 365 * 90
total_weeks = 52 * 90
total_months = 12 * 90

your_age = total_life - time1
weeks_left = total_weeks - time2 
months_left = total_months - time3 

print(f"you have {your_age} days  and {weeks_left} weeks and {months_left} months to live ")
