# assume size of survey > 1 and they are not the same value

def local_peak_array_version(survey):
    ptr1 = 0
    ptr2 = 1
    while survey[ptr2]:
        if survey[ptr1] < survey[ptr2]:
            ptr1 += 1
            ptr2 += 1
        else:
            return ptr1
    return ''


# print(local_peak_array_version([4,5,2,7,8,2,1,2,3,4,8]))
def local_peak_function_version(a, b, survey):
    # Binary search
    left = a
    right = b
    while left < right:
        # Calculate the middle
        mid = (left + right) // 2
        mid_val = survey(mid)

        # Consider boundary situation
        # When the position of mid is the most left
        if mid == left:  # At the boundary, compare only with the right neighbor
            if mid_val > survey(mid + 1):
                return mid
            else:
                left = mid + 1
        elif mid == right:  # At the boundary, compare only with the left neighbor
            if mid_val > survey(mid - 1):
                return mid
            else:
                right = mid - 1
        else:  # In the middle, compare with both neighbors
            if mid_val > survey(mid + 1) and mid_val > survey(mid - 1):
                return mid
            elif mid_val <= survey(mid + 1):  # Move to the right if the right neighbor is larger or equal
                left = mid + 1
            else:  # Move to the left if the left neighbor is larger
                right = mid - 1

    # If the loop terminates, and we haven't returned, it means `left == right`. Return either.
    return left


survey1 = lambda i: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11][i]
print(local_peak_function_version(0, 10, survey1))
#survey3 = lambda i: [1, 2, 3, 4, 5, 6, 5, 4, 3, 2][i % 10]
#print(local_peak_function_version(1, 9, survey3))
#print(local_peak_function_version(11, 19, survey3))
survey2 = lambda i: i if i <= 1234567890 else (1234567890*2) - i - 1
print(local_peak_function_version(0,12345678900,survey2))