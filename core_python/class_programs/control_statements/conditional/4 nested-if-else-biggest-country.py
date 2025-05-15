# find the biggest country among 3 countries based on the population
country_1 = int(input("Enter population of country_1 "))
country_2 = int(input("Enter population of country_2 "))
country_3 = int(input("Enter population of country_3 "))

if country_1 > country_2:
    if country_1 > country_3:
        print("Country1 is the biggest country based on the population")
    else:
        print("Country3 is the biggest country based on the population")
else:
    if country_2 > country_3:
        print("Country2 is the biggest country based on the population")
    else:
        print("Country3 is the biggest country based on the population")

print("End of program")






