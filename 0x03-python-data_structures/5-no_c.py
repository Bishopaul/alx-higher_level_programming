#!/usr/bin/env python3
def no_c(my_string):
    new_string = []
        for c in my_string:
            if c != 'c' and c != 'C':
                new_string.append(c)
        return "".join(new_string)
