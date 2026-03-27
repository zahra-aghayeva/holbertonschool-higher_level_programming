#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    # dir() funksiyası modulun içindəki bütün adları siyahı şəklində qaytarır
    names = dir(hidden_4)
    
    # Siyahını əlifba sırasına salırıq
    names.sort()
    
    for name in names:
        # Yalnız __ ilə başlamayan adları çap edirik
        if not name.startswith("__"):
            print("{}".format(name))
