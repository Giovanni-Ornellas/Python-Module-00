# ****************************************************************************
#
#    ft_count_harvest_recursive.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/04/27
#
# ****************************************************************************

def ft_count_harvest_recursive_stack(day: int) -> None:
    if (day <= 0):
        return
    ft_count_harvest_recursive_stack(day - 1)
    print(f"Day {day}")


def ft_count_harvest_recursive() -> None:
    days_until_harvest = int(input("Days until harvest: "))

    ft_count_harvest_recursive_stack(days_until_harvest)
    print("Harvest time!")
