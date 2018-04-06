ordered_list = list(range(300))

try:
    num = int(input("Search for: "))
except ValueError:
    print("Couldn't parse input, only integers allowed.")
    quit()
try:
    answer = ordered_list.index(num)
    while ordered_list[answer]==num:
        print("Found {} in position {}".format(num,answer))
        answer+=1
except ValueError:
    print("Number not found")
except IndexError:
    pass
