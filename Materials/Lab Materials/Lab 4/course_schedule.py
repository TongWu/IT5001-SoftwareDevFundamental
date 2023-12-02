# HELPER FUNCTIONS
def make_course(code, units):
    return (code, units)

def make_units(lec, tut, lab, hw, prep):
    return (lec, tut, lab, hw, prep)

def get_course_code(course):
    return course[0]

def get_course_units(course):
    return course[1][0] + course[1][1] + course[1][2] + course[1][3] + course[1][4]

# Q1
def make_empty_schedule():
    '''
    Returns an empty schedule.
    '''
    return []

# Q2
def add_course(course, schedule):
    '''
    Returns a new schedule with the added course.

    If the course is already in the schedule,
    returns the schedule unchanged.
    '''
    if schedule == make_empty_schedule():
        return [course]
    else:
        for curr_course in schedule:
            if get_course_code(curr_course) == \
               get_course_code(course):
                return schedule
        return schedule + [course]

# Q3
def total_scheduled_units_i(schedule):
    '''
    Returns the total number of units from
    all courses in the given schedule.
    
    Iterative.
    '''
    total = 0
    for curr_course in schedule:
        total += get_course_units(curr_course)
    return total

def total_scheduled_units_r(schedule):
    '''
    Returns the total number of units from
    all courses in the given schedule.
    
    Recursive.
    '''
    if schedule == make_empty_schedule():
        return 0
    else:
        return get_course_units(schedule[0]) + total_scheduled_units_r(schedule[1:])
    
# Q4
def drop_course_i(course, schedule):
    '''
    Returns a new schedule with a particular course dropped
    from the given schedule.

    If there are duplicate courses to be removed, drop all.

    Iterative.
    '''
    new_schedule = make_empty_schedule()
    for curr_course in schedule:
        if get_course_code(curr_course) != get_course_code(course):
            new_schedule = add_course(curr_course, new_schedule)
    return new_schedule

def drop_course_r(course, schedule):
    '''
    Returns a new schedule with a particular course dropped
    from the given schedule.

    If there are duplicate courses to be removed, drop all.

    Recursive.
    '''
    if schedule == make_empty_schedule():
        return schedule
    else:
        curr_course, next_courses = schedule[0], schedule[1:]
        if get_course_code(curr_course) == get_course_code(course):
            return drop_course_r(course, next_courses)
        else:
            return add_course(curr_course, drop_course_r(course, next_courses))

# Q5
def valid_schedule(schedule, max_units):
    '''
    Returns a new schedule that has total number of
    units less than or equal to max_units by
    removing courses from the specified schedule.
    
    Naive.
    '''
    new_schedule = make_empty_schedule()
    units_left = max_units
    for course in schedule:
        if get_course_units(course) <= units_left:
            new_schedule = add_class(course, new_schedule)
            units_left -= get_course_units(course)
    return new_schedule
  
def valid_schedule(schedule, max_units):
    '''
    Returns a new schedule that has total number of
    units less than or equal to max_units by
    removing courses from the specified schedule.
    
    Optimized (valid schedule with the maximum no. of units).
    '''
    if schedule == make_empty_schedule():
        return schedule
    else:
        curr_course, new_schedule = schedule[0], schedule[1:]
        untaken = valid_schedule(new_schedule, max_units)
        if get_course_units(curr_course) <= max_units:
            taken = add_course(curr_course, valid_schedule(new_schedule, max_units - get_course_units(curr_course)))
            return max(taken, untaken, key=total_scheduled_units_i)
        else:
            return untaken

# TESTS
try:
    course1 = make_course('course1', make_units(1, 2, 3, 4, 5)) # get_course_units(course1) == 15
    course2 = make_course('course2', make_units(1, 0, 1, 5, 6)) # get_course_units(course2) == 13
    course3 = make_course('course3', make_units(1, 0, 1, 5, 6)) # get_course_units(course3) == 13
    course4 = make_course('course4', make_units(1, 2, 3, 4, 4)) # get_course_units(course4) == 14
    course5 = make_course('course5', make_units(1, 2, 3, 4, 6)) # get_course_units(course5) == 16

    def is_same(schedule1, schedule2):
        return set(schedule1) == set(schedule2)

    my_schedule = make_empty_schedule()
    assert my_schedule == []

    my_schedule = add_course(course1, my_schedule)
    my_schedule = add_course(course2, my_schedule)
    my_schedule = add_course(course3, my_schedule)
    assert is_same(my_schedule, [course1, course2, course3])
    my_schedule = add_course(course2, my_schedule)
    assert is_same(my_schedule, [course1, course2, course3])

    assert total_scheduled_units_i(my_schedule) ==  41
    assert total_scheduled_units_r(my_schedule) ==  41

    assert is_same(drop_course_i(course2, my_schedule), [course1, course3])
    assert is_same(drop_course_r(course2, my_schedule), [course1, course3])

    my_schedule.append(course3) # illegal
    assert is_same(drop_course_i(course3, my_schedule), [course1, course2])
    assert is_same(drop_course_r(course3, my_schedule), [course1, course2])

    my_schedule = [course1, course2, course3, course4, course5] # illegal
    assert is_same(valid_schedule(my_schedule, 20), [course5])
    assert is_same(valid_schedule(my_schedule, 26), [course2, course3])
    assert is_same(valid_schedule(my_schedule, 14), [course4])
except AssertionError:
    print(f'my_schedule = {my_schedule}')
    raise
