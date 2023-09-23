#we are going to learn about function call and how to use it
def square(x): #this is a function definition
    return x*x  #this is a function body
def sub(x,y):
    return x-y

print(square(3)) #this is a function call
print(sub(5,2)) 

#now use those 2 functions to calculate the following
print(square(5) + 2) #it will call the square function first then add 2 in answer of square function then print it
print(square(5) + square(2)) #square(5) = 25 and square(2) = 4 then add(25,4) = 29
print(sub(square(5),square(2))) # square(5) = 25 and square(2) = 4 then sub(25,4) = 21