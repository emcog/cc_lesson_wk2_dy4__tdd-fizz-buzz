# variable = [expression for item in list if condition]

# evens_squared_03 = [ number * number for number in range(1,11) if number % 2 == 0 ]

#  --- > how to use return here?
ages_01 = [ age for age in range(5,85) if age %2 != 0]
print(ages_01)


ages = [5, 15, 64, 27, 84, 26]
ages_02 = [ age for age in ages if age %2 != 0 ]
print('ages_02', ages_02)


chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
ten_char_chicks =  [ chicken for chicken in chicken_names if len(chicken) >= 10 ]
print('ten_char_chicks', ten_char_chicks)

chick_with_an_H = [ chicken for chicken in chicken_names if chicken[0].upper() == 'H']
print('chick_with_an_H', chick_with_an_H)


words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
all_first_letters = [word[0] for word in words if word]
print(all_first_letters)
all_first_lower = [word[0].lower() for word in words if word]
print(all_first_lower)