###################################
# File Name : variable_read_example.py
###################################
#!/usr/bin/python3

msg = "Hello"

def read_work():
    print (msg)
    print ("World")

def read_exception():
    print (msg)
    msg = "World"
    print (msg)


print ("=== first read ===")
read_work()

print ("=== second read ===")
read_exception()
