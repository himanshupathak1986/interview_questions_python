# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

import numpy as np

def rotate_matrix(matrix):
    rotated_matrix_k_1 = np.rot90(matrix, k=-1)
    print("K1 rotated matrix: \n {}".format(rotated_matrix_k_1))
    
    rotated_matrix_k_2 = np.rot90(matrix, k=2)
    print("K2 rotated matrix: \n {}".format(rotated_matrix_k_2))


if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [8,9,10]]
    np_matrxi = np.array(matrix)
    print(np_matrxi)
    rotate_matrix(matrix)