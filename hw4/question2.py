# Ozan Yetkin | 1908227

example_input = [4, 3, 2, 6]

def find_min_cost(stick_list):
    total_cost = 0
    if len(stick_list) > 1:
        stick_list.sort()

        s1 = stick_list.pop(0)
        s2 = stick_list.pop(0)
        total_cost += s1 + s2
        stick_list.append(s1 + s2)
        find_min_cost(stick_list)
    else:
        return stick_list

print(find_min_cost(example_input))
