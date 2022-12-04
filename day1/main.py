input = ''
# read from input file
with open('input.txt') as f:
    input = f.read()


calorie_groups = input.split('\n\n')


def calculate_total(i):
    """Calculate the total cals for a group by given index"""
    calories = calorie_groups[i].split('\n')
    total = 0
    for calorie in calories:
        total += int(calorie)

    return total


def find_most_calories(calorie_groups, skipped_groups):
    """Return the index of the most calories in group"""
    most_calories = 0
    group_index = None

    for i in range(len(calorie_groups)):
        if i in skipped_groups:
            continue

        total = calculate_total(i)
        if total > most_calories:
            most_calories = total
            group_index = i

    return group_index


def top_calories(n):
    """Return the total calories of top n groups"""
    top_groups = set()
    for i in range(n):
        group = find_most_calories(calorie_groups, top_groups)
        top_groups.add(group)

    total = 0
    for group in top_groups:
        group_total = calculate_total(group)
        total += group_total
    return total


print(f'Part1: {top_calories(1)}')
print(f'Part2: {top_calories(3)}')
