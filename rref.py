import numpy as np

def rref(arr):
    for col in range(arr.shape[1] - 1):
        for row in range(arr.shape[0]):
            idx = list(arr[:,col]).index(max(arr[:,col]))
            arr = swap_rows(arr, row, idx)
            arr = row_scale(arr, row)
            arr = eliminate(arr, row)
    arr = backsolve(arr)

def swap_rows(arr, row, idx):
    arr_new = arr.copy()
    arr_new[row,:] = arr[idx,:]
    arr_new[idx,:] = arr[row,:]
    return arr_new

def row_scale(arr, row):
    factor = arr[row,row]
    for col in range(arr.shape[1]):
        arr[row,col] = arr[row,col] / factor
    return arr

def eliminate(arr, target_row):
    target_col = target_row
    for row in range(target_row + 1, arr.shape[0]):
        factor = arr[row,target_col]
        for col in range(target_col, arr.shape[1]):
            arr[row,col] = arr[row,col] - factor * arr[target_row,col]
    return arr

def backsolve(arr):
    augColIdx = arr.shape[1] - 1
    for row in range(0,arr.shape[0])[::-1]:
        for col in range(0,row)[::-1]:
            factor = arr[row,col]
            arr[row,col] = arr[row,col] - (factor * matrix[row,col])
            arr[row,col] = arr[row,augColIdx] - (factor * matrix[row,augColIdx])
    return arr
