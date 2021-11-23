# Partyoutlier

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns this "outlier" N


def find_outlier(var):
    if var[0]%2 == 0 and var[1]%2 == 0 and var[2]%2 == 0 :
        for n in var:
            if n%2 == 1:
                return n
    elif var[0]%2 == 0 and var[1]%2 == 0 and var[2]%2 == 1:
        return var[2]
    elif var[0]%2 == 0 and var[1]%2 == 1 and var[2]%2 == 0:
        return var[1]
    elif var[0]%2 == 0 and var[1]%2 == 1 and var[2]%2 == 1:
        return var[0]
    elif var[0]%2 == 1 and var[1]%2 == 0 and var[2]%2 == 0:
        return var[0]
    elif var[0]%2 == 1 and var[1]%2 == 0 and var[2]%2 == 1:
        return var[1]
    elif var[0]%2 == 1 and var[1]%2 == 1 and var[2]%2 == 0:
        return var[2]
    elif var[0]%2 == 1 and var[1]%2 == 1 and var[2]%2 == 1:
        for n in var:
            if n %2 == 0:
                return n

        
            

find_outlier([2, 4, 6, 8, 10, 3])
