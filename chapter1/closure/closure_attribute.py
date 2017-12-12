###################################
# File Name : closure_attribute.py
###################################
#!/usr/bin/python3


def closure():
    x = 10
    def inner():
        y = 20
        return x+y

    return inner


p = closure()

print ("=== attribute closure ===")
print (p.__closure__)
