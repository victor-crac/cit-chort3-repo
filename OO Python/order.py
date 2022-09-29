#3
def sumLargestNumbers(arr):
    return sum(sorted(arr)[-2:])

print(sumLargestNumbers([4,5,6]))

#4
def up_low(s):      
    u = sum(1 for i in s if i.isupper())
    l = sum(1 for i in s if i.islower())
    print( "No. of Upper case characters : %s,No. of Lower case characters : %s" % (u,l))

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")

#Class attributres #6

class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

teacher = Teacher("Lokesh", 36)
print("Teacher class's object  all properties")

print(dir(teacher))


#7Using only functions and lists, Implement a queue data structure. The queue should have the following methods: enqueue, dequeue, and size. The queue should be "first-in-first-out" (FIFO).

# create a list with 7 ]
 
# display the result
data=[1,2,3,4,5,6,7]
 
# use list comprehension to get square
# of odd numbers
result = [i*i for i in data if i!=0]
 
# display the result
print(result)