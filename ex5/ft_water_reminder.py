# ****************************************************************************
#
#    ft_water_reminder.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/04/27
#
# ****************************************************************************

def ft_water_reminder() -> None:
    days = int(input("Days since last watering: "))

    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
