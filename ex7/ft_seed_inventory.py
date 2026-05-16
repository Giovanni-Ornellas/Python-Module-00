# ****************************************************************************
#
#    ft_seed_inventory.py
#
#    By: ganselmo <ganselmo@student.42.rio>
#
#    Created: 2026/04/27
#
# ****************************************************************************

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{seed_type} seeds: covers {quantity} square meters")
    else:
        print(f"{seed_type} seeds: {quantity} {unit} ")