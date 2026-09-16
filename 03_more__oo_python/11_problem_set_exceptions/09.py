numbers = [1, 2, 3, 4, 5]

# LBYL approach
def get_sixth_element_lbyl():
    if len(numbers) > 5:
        return numbers[5]

    return None


# AFNP approach
def get_sixth_element_afnp():
    try:
        return numbers[5]
    except IndexError:
        return None
