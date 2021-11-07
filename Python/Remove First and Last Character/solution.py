def remove_char(s):
    lst = list(s)
    lst.pop(0)
    lst.pop(-1)

    return "".join(lst)
