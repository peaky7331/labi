#Формируется матрица F следующим образом: Скопировать в нее матрицу А и если сумма чисел, больших К в нечетных столбцах в области 3 больше, 
# чем произведение чисел по периметру в области 2, то поменять симметрично области 1 и 2 местами, иначе 3 и 4 поменять местами несимметрично. 
# При этом матрица А не меняется. После чего вычисляется выражение: ((К*A)*F+ K* F T . Выводятся по мере формирования А, F и все матричные операции последовательно.

def create_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def print_matrix(matrix, name):
    print(f"Матрица {name}:")
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

def copy_matrix(matrix):
    return [row[:] for row in matrix]

def sum_greater_than_k(matrix, k, indices):
    total = 0
    for (i, j) in indices:
        if matrix[i][j] > k:
            total += matrix[i][j]
    return total

def prod_perimeter(matrix, indices):
    perimeter_elements = [matrix[i][j] for (i, j) in indices]
    product = 1
    for elem in perimeter_elements:
        product *= elem
    return product

def swap_symmetric(matrix, indices1, indices2):
    for (i1, j1), (i2, j2) in zip(indices1, indices2):
        matrix[i1][j1], matrix[i2][j2] = matrix[i2][j2], matrix[i1][j1]

def swap_asymmetric(matrix, indices3, indices4):
    for (i3, j3), (i4, j4) in zip(indices3, indices4):
        matrix[i3][j3], matrix[i4][j4] = matrix[i4][j4], matrix[i3][j3]

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

def calculate_expression(a, f, k):
    result = []
    f_transpose = transpose_matrix(f)
    for i in range(len(a)):
        result_row = []
        for j in range(len(a[i])):
            result_value = (k * a[i][j]) * f[i][j] + k * f_transpose[i][j]
            result_row.append(result_value)
        result.append(result_row)
    return result

def main():
    K = int(input("Введите значение K: "))
    N = int(input("Введите размерность матрицы N: "))


    A = create_matrix_from_file('kekw.txt')
    print_matrix(A, 'A')

    
    F = copy_matrix(A)

    
    indices1 = [(i, j) for i in range(N//2) for j in range(N//2)]
    indices2 = [(i, j) for i in range(N//2) for j in range(N//2, N)]
    indices3 = [(i, j) for i in range(N//2, N) for j in range(N//2)]
    indices4 = [(i, j) for i in range(N//2, N) for j in range(N//2, N)]

    
    sum_area3 = sum_greater_than_k(F, K, indices3)
    prod_area2 = prod_perimeter(F, indices2)

    
    if sum_area3 > prod_area2:
        swap_symmetric(F, indices1, indices2)
    else:
        swap_asymmetric(F, indices3, indices4)

    print_matrix(F, 'F')

    
    result = calculate_expression(A, F, K)
    print_matrix(result, 'Результат')

if __name__ == "__main__":
    main()
