# 8-16. Imports: Using a program you wrote that has one function in it, store that 
# function in a separate file. Import the function into your main program file, and 
# call the function using each of these approaches:

#  import module_name
# import car

# car_details = car.make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car_details)

#  from module_name import function_name
# from car import make_car

# car_details = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car_details)

#  from module_name import function_name as fn
# from car import make_car as mc

# car_details = mc('subaru', 'outback', color='blue', tow_package=True)
# print(car_details)

#  import module_name as mn
# import car as c

# car_details = c.make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car_details)

#  from module_name import *
from car import *

car_details = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car_details)
