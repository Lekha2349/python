from array import array
arr1=array('q',[1,2,3,4,5])
total_item_size=len(arr1) * arr1.itemsize
print("Total size of items in bytes:",total_item_size)