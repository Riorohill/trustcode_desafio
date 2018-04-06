from bisect import bisect_left

def first_index(ordered_list, n):
    'Locate the leftmost value exactly equal to n'
    i = bisect_left(ordered_list, n)
    if i != len(ordered_list) and ordered_list[i] == n:
        return i
    raise ValueError

ordered_list = list(range(300))

try:
    num = int(input("Search for: "))
except ValueError:
    print("Couldn't parse input, only integers allowed.")
    quit()

try:
    answer = first_index(ordered_list, num)
    while ordered_list[answer]==num:
        print("Found {} in position {}".format(num,answer))
        answer+=1
except ValueError:
    print("Number not found")
except IndexError:
    pass
