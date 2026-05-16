# ****************************************************************************
#
#    ft_count_harvest_iterative.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/04/27
#
# ****************************************************************************

def ft_count_harvest_iterative() -> None:
    days_until_harvest = int(input("Days until harvest: "))

    for days in range(1, days_until_harvest + 1):
        print(f"Day {days}")
    print("Harvest time!")
