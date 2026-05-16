# ****************************************************************************
#
#    ft_harvest_total.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/04/26
#
# ****************************************************************************

def ft_harvest_total() -> None:
    day_one = input("Day 1 harvest: ")
    day_two = input("Day 2 harvest: ")
    day_three = input("Day 3 harvest: ")
    total_harvest = int(day_one) + int(day_two) + int(day_three)
    print(f"Total harvest: {total_harvest}")
