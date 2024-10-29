def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the original matrix
    return [[num ** 2 for num in row] for row in matrix]