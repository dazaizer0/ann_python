import AILib as a

ret = True

mode = a.Mode(False, 0, 5, ret)
ret = mode.SET_MODE_MOL()
print(ret)
