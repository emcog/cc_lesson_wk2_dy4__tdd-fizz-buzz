# numbers = range(1,11)
# evens_squared = []
# for number in numbers
#     if number % 2 == 0:
#         evens_squared.append(number * number)


# above can be replaced with one line, list comprehension
# evens_squared = [expression for item in list if condition]

numbers = range(1,11)
# evens_squared_02 = [expression for item in list if condition]
evens_squared_02 = [ number * number for number in numbers if number % 2 == 0 ]



# evens_squared_02 = [expression for item in list if condition]
evens_squared_03 = [ number * number for number in numbers if number % 2 == 0 ]



print(evens_squared_02)