def findval(alist, x):
    # alist is the input list
    # x is the value being searched for
    # This function returns a bool True if found
    # and returns a bool False if not found
    for val in alist:
        if (val == x):
            return True
    return False


# end function definitions
# =====================
# main code begins here ...

a = [2, 3, 4, 5, 6, 7, 8]
print(findval(a, 4))
print(findval(a, 29))
b = [45, 34, 78, 89]
print(findval(b, 45))
print(findval(b, 1470))   
