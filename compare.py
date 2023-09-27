x = int(input("what's x?"))
y = int(input("what's y?"))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y");

#another way more concise
x = int(input("what's x?"))
y = int(input("what's y?"))

if x < y or x > y:
    print("x and y is not equal")
else:
    print("x and y is equal");
#another way 
x = int(input("what's x?"))
y = int(input("what's y?"))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y");
