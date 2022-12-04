input = ''
# read from input file
with open('input.txt') as f:
    input = f.read()

def find_most_calories(input):
    calorie_groups = input.split('\n\n')
    most_calories = 0
    for calorie_group in calorie_groups:
        calories = calorie_group.split('\n')
        total = 0
        for calorie in calories:
            total += int(calorie)
        if total > most_calories:
            most_calories = total
    return most_calories


print(find_most_calories(input))
