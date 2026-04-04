#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Siyahıdakı ilk x element arasından yalnız tam ədədləri çap edir.
    """
    count = 0
    for i in range(x):
        try:
            # {:d} yalnız integer qəbul edir. 
            # Əgər my_list[i] integer deyilsə, ValueError/TypeError atacaq.
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Integer olmayanları səssizcə keçirik.
            continue
    print("")
    return count
