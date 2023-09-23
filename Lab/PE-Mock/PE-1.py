def how_many_male(faculty):
    male_count = 0
    for character in faculty:
        if character == 'M':
            male_count += 1
    return male_count


def how_many_female(faculty):
    female_count = 0
    for character in faculty:
        if character == 'F':
            female_count += 1
    return female_count


def gender_balance(faculty):
    female_count = how_many_female(faculty)
    male_count = how_many_male(faculty)
    if female_count == male_count:
        return 'balanced'
    elif female_count > male_count:
        return 'female'
    else:
        return 'male'
