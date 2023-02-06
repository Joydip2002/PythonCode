# numpy Package used for to help printing multi-dimensional array in pyhton. Python does not support multi-dimensional array.It's have two arguments that reason.

# What is numpy: numpy stands numerical Python. It is used for mathematical calculation. That  saves running time.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important 

# Why is NumPy Faster Than Lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

# This behavior is called locality of reference in computer science.

# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

# Single Dimensional Array
# from array import *

# data = array('i',[1,2,3])
# print(data)

# Multi-dimensional Array
from array import *
import random as rad
import numpy as np

# data = np.array([1,2,3,4,5,6],int)
# print(data)

# arange() method => use 10 => 0 to (n-1) => print 0,1,2,3,4,5,6,7,8,9
# data = np.arange(1,10,2)
# print(data)

#reshape() => use for shapping matrix
# data = np.arange(1,10).reshape(3,3)
# print(data)

#random() method
# data = rad.randrange(1,100)
# print(data)

# data = rad.SystemRandom()
# print(data)

# data = rad.sample(range(1,100),5)
# print(data)

# data = np.array([1,2,3,5,6])
# print(data.dtype)

# data = np.linspace(0,10,16)
# print(data)

# data = np.logspace(1,10,5)
# print(data)

# data = np.ones(5)
# print(data)

# data = np.zeros(5)
# print(data)


