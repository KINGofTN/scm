import numpy as np

#creating 1d arry
n = np.array([1,2,3,4,5])
#print(n)

#2d arry
n = np.array([[1,2,3,4,5],[1,2,3,4,5]])
#print(n)

"""
arry in fromation
print(n.shape)
print(n.dtype)
print(n.size)
print(n.dtype)
print(n.ndim)
"""


"""
creating arrays
print(np.zeros(5))
print(np.zeros((5,5)))
print(np.ones((5,5)))
print(np.eye(3))

# create 0 to 9
print(np.arange(1,10))

#create n numbers between 1 to 5
print(np.linspace(1,5,5))
"""

"""
oparations

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b    # [5 7 9]
a - b    # [-3 -3 -3]
a * b    # [4 10 18]
a / b    # [0.25 0.4 0.5]
a ** 2   # [1 4 9]



"""
"""
a = np.arange(1,10+1)
b = np.arange(1,10+1)

print(a)
print(b)
print(a+b)
print(a-b)

print("=================")
print(a*2)"""




"""
slicing

arr = np.array([10, 20, 30, 40, 50])

arr[0]     # first element → 10
arr[-1]    # last element → 50
arr[1:4]   # [20 30 40]
arr[:3]    # [10 20 30]
"""

"""
math funciton

np.mean(a)     # average
np.median(a)
np.std(a)      # standard deviation
np.sum(a)
np.max(a)
np.min(a)


"""

"""
random numpers creation
np.random.rand(3)        # random numbers 0–1
np.random.randint(1, 10, 5)  # 5 random ints from 1–9

"""


#print(np.linspace(1,100,10000))

print(np.pi)
print(np.cos(0))