#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

Given a sorted list with an unsorted number e in the rightmost cell, can you write some simple code to insert e
into the array so that it remains sorted?

def insertionSort1(n, arr):
    # Write your code here
    target=arr[-1] #fetches last element if array
    i=n-1 #selects from last indes
    while i > 0 and arr[i-1]>target: #traverses backwards
       arr[i]=arr[i-1] #copies previous element to current index
       print(*arr) #prints array
       i=i-1
    arr[i]=target #assigning target to corresponding index
    print(*arr)
    
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
