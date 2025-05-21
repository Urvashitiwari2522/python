# LAmbda function are often used  in situations where a small function is required  for a shorted period of time
# they are commonly used as argument to higher-ordered functions such as map , filter, reduce
# Using function
def square(x):
    return x*x
print(square(2))
# Using lambda 
sq = lambda x: x*x
print(sq(5))

# cube using lambda
cube = lambda x: x*x*x
print(cube(3))

# avg using lambda
avg = lambda x,y,z: x+y+z/3
print(avg(2,3,4))

# percentage using lambda
percentage = lambda totalMarks : (totalMarks/500)*100
print(percentage(400))