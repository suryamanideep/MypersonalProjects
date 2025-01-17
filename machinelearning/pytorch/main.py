import torch 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
Random tensors:

Random tensors are important because the way neural networks learn is thta they start with tensors with random numbers and then adjust those random numbers 
to better represent the data.
start with random numbers ->  look at data -> update random number  -> look at data -> update random numbers

random_tensor = torch.rand(2,3,4)
print(random_tensor)
print(random_tensor.ndim,random_tensor.shape)

random_image_tensor_random = torch.randn(size=(224,224,3))#height width,channels (r g b)
print(random_image_tensor_random.shape)
random_image_tensor_random.dtype-> always float32
torch.zeros(size=(3,4))

print(torch.arange(0,10))-> defaults to integers
also can be written as :
oneToTen = torch.arange(start = 1 , end = 11 , step = 1)
print(torch.range(0,10)) -> defauls to float32

creating tensors like :
torch.zeros_like(input = oneToTen)

'''
oneToTen = torch.arange(start = 1 , end = 11 , step = 1)

print(torch.zeros_like(input = oneToTen))