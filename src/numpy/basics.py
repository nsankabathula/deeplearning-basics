import numpy as np

a = np.array([1,2,3])
print ('Array: ', a);
a = np.arange(10)
print ('Array Arrange: ', a);


matrix = np.array([[1,2,3],[4, 5, 3]])
print ('Matrix: ', matrix);# more than one dimensions
print('Reshape',matrix.reshape(3,2) );


mindim = np.array([1, 2, 3,4,5], ndmin = 2)
print ('Min Dimension', mindim, mindim[0][2]);

studentDtype = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4'),('male','bool')])
studentArray = np.array([('Naveen', 21, 50, True),('Sandy', 18, 75, False)], dtype = studentDtype);
print ('Student Array', studentArray);
print ('Student 0: name - male?', studentArray[0]['name'], studentArray[0]['male']);
print ('ItemSize', studentArray.itemsize )
print ('studentArray flags',studentArray.flags)

a = np.array([[0.0, 0.0, 0.0], [10.0, 10.0, 10.0], [20.0, 20.0, 20.0], [30.0, 30.0, 30.0]])
b = np.array([1.0, 2.0, 3.0])

print(
'First array:',
a);

print(
'Second array:',
b);

print(
'First Array + Second Array\n',
a + b)


print ('Transpose A\n', a.T);

for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2*x + 3;

print ('Modify A\n', a);