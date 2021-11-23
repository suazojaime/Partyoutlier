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
