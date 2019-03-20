import array

arr = array.array('i', [0, 1, 2, 4, 5, 6, 7])
print arr
print len(arr)
arr.insert(3, 3)
print arr
print "Array Type: " + arr.typecode
print "Array element size: " + str(arr.itemsize)
arr.pop(2)
arr.remove(0)
print arr