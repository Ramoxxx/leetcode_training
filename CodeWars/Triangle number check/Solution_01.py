# Triangle number check
def is_triangle_number(number: int) -> bool:
    # decreasing loop
    cpt = 1
    while number > 0:
        number -= cpt
        cpt+=1
    return number == 0

    # increasing loop
    # per_line = 1
    # cpt = 0
    # while cpt < number:
    #     cpt += per_line
    #     per_line += 1
    # return cpt == number

    # using formula : 1 + 8 * number == any perfect square
    # return ((1 + 8 * number) ** 0.5) % 1 == 0