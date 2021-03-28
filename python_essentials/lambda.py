def mod_checker(value_from_external_func, mod=0):
    return lambda final_value : final_value % value_from_external_func == mod

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True



