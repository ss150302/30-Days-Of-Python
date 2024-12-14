
import numpy as np
def use_numpy_array():
    # syntax
    # Create a 1D array
    array_1d = np.array([1, 2, 3, 4, 5])
    print("1D Array:")
    print(array_1d)

    # Access elements
    print("\nElement at index 3:")
    print(array_1d[3])  # Output: 4

    # Create a 2D array (matrix)
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("\n2D Array:")
    print(array_2d)

    # Access elements
    print("\nElement at row 1, column 2:")
    print(array_2d[1, 2])  # Output: 6

    # Create a 3D array
    array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
    print("\n3D Array:")
    print(array_3d)

    # Access elements in 3D array
    print("\nElement at depth 1, row 0, column 1:")
    print(array_3d[1, 0, 1])  # Output: 6

    # Reshape the array
    reshaped_array = array_2d.reshape(1, 9)
    print("\nReshaped Array (1x9):")
    print(reshaped_array)

    # Slicing the array
    print("\nSliced Array (first two rows and columns):")
    print(array_2d[:2, :2])  # Output: [[1, 2], [4, 5]]

    # Perform mathematical operations
    print("\nArray after adding 10 to each element:")
    print(array_2d + 10)
    # Step 1: Create a 2D array (matrix)
    array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("2D Array:")
    print(array_2d)

    # Step 2: Access elements
    print("\nElement at row 1, column 2:")
    print(array_2d[1, 2])  # Output: 6

    # Step 3: Create a 3D array
    array_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
    print("\n3D Array:")
    print(array_3d)

    # Step 4: Access elements in 3D array
    print("\nElement at depth 1, row 0, column 1:")
    print(array_3d[1, 0, 1])  # Output: 6

    # Step 5: Reshape the array
    reshaped_array = array_2d.reshape(1, 9)
    print("\nReshaped Array (1x9):")
    print(reshaped_array)

    # Step 6: Slicing the array
    print("\nSliced Array (first two rows and columns):")
    print(array_2d[:2, :2])  # Output: [[1, 2], [4, 5]]

    # Step 7: Perform mathematical operations
    print("\nArray after adding 10 to each element:")
    print(array_2d + 10)
    # Output: [[11, 12, 13], [14, 15, 16], [17, 18, 19]]

def numpy_multi_diamentional_array():
    data = np.array([[1.5, -0.1, 3], [0, -3, 6.5]])
    print('data:', data)
    print('data * 10', data * 10)
    print('data + data:', data + data)
    print('data.shape:', data.shape)
    print('data.dtype:', data.dtype)
    print('data.ndim:', data.ndim)
    print('data.size:', data.size)
    print('data.itemsize:', data.itemsize)
    print('data.nbytes:', data.nbytes)
    print('data.strides:', data.strides)
    print('data.T:', data.T)
    print('data.flatten():', data.flatten())
    print('data.ravel():', data.ravel())
    print('data.reshape(3, 2):', data.reshape(3, 2))
    print('data.reshape(1, 6):', data.reshape(1, 6))
    print('data.reshape(6, 1):', data.reshape(6, 1))
    print('data.reshape(6, 1).ravel():', data.reshape(6, 1).ravel())
    print('data.reshape(6, 1).flatten():', data.reshape(6, 1).flatten())
    print('data.reshape(6, 1).flatten(order="F"):', data.reshape(6, 1).flatten(order="F"))
    print('data.reshape(6, 1).ravel(order="F"):', data.reshape(6, 1).ravel(order="F"))
    print('data.reshape(-1, 1):', data.reshape(-1, 1))
    print('data.reshape(1, -1):', data.reshape(1, -1))
    print('data.reshape(-1):', data.reshape(-1))
    print('data.reshape(3, -1):', data.reshape(3, -1))
    print('data.reshape(-1, 3):', data.reshape(-1, 3))
    print('data.reshape(-1, 1):', data.reshape(-1, 1))
    print('data.reshape(1, -1):', data.reshape(1, -1))
    print('data.reshape(-1):', data.reshape(-1))
    print('data.reshape(3, -1):', data.reshape(3, -1))
    print('data.reshape(-1, 3):', data.reshape(-1, 3))
    print('data.reshape(-1, 1):', data.reshape(-1, 1))

def use_create_ndarry():
    # syntax
    # Create a 1D array
    data1 = [6, 7.5, 8, 0, 1]
    array_1d = np.array(data1)
    print("1D Array:", array_1d)
    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    arr2 = np.array(data2)
    print("2D Array:", arr2)
    print("arr2.ndim:", arr2.ndim)
    print("arr2.shape:", arr2.shape)

    arr3=np.zeros((3, 6))
    print("arr3:", arr3)
    arr4=np.empty((2, 3, 2))
    print("arr4:", arr4)
    arr5=np.arange(15)
    print("arr5:", arr5)
    arr6=np.ones((3, 3))
    print("arr6:", arr6)
    arr7=np.eye(3)
    print("arr7:", arr7)
    arr8=np.identity(3)
    print("arr8:", arr8)
    arr9=np.full((2, 2), 35)
    print("arr9:", arr9)

def use_ndarray_data_types():
    arr1 = np.array([1, 2, 3], dtype=np.float64)
    print("arr1:", arr1)
    print("arr1.dtype:", arr1.dtype)
    arr2 = np.array([1, 2, 3], dtype=np.int32)
    print("arr2:", arr2)
    print("arr2.dtype:", arr2.dtype)


if __name__ == "__main__":
    use_numpy_array()
    numpy_multi_diamentional_array()
    use_create_ndarry()
    use_ndarray_data_types()




