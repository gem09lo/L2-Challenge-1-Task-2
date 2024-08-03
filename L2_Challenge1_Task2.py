##L2 Challenge 1: Task 2 - python L2_Challenge1_Task2.py
##Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize(n):
    n = str(n)
    lst = [int(d) for d in n]
    return lst[::-1]


print (digitize(35231))
print (digitize(0))
print (digitize(23582357))
