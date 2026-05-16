# ****************************************************************************
#
#    ft_plant_age.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/04/27
#
# ****************************************************************************

def ft_plant_age() -> None:
    days = int(input("Enter plant age in days: "))
    if (days > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
