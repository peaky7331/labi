# Формируется матрица F следующим образом: скопировать в нее А и  если в Е сумма чисел, больших К в нечетных столбцах больше, чем произведение чисел по периметру, 
# то поменять местами С и Е симметрично, иначе С и В поменять местами несимметрично. При этом матрица А не меняется. 
# После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*A-1 – K * F-1, 
# иначе вычисляется выражение (AТ +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А.  Выводятся по мере формирования А, F и все матричные операции последовательно.

import numpy as np

N = int(input("Введите  N: "))
K = int(input("Введите K: "))

A = np.random.randint(-10, 10, (N, N))

size = N // 2
B = A[:size, :size]
C = A[:size, size:]
D = A[size:, size:]
E = A[size:, :size]

F = np.copy(A)

sum_perimeter_C = np.sum(C[0, :]) + np.sum(C[:, 0]) + np.sum(C[-1, :]) + np.sum(C[:, -1]) - C[0, 0] - C[0, -1] - C[-1, 0] - C[-1, -1]
prod_diagonal_C = np.prod(np.diag(C))

if sum_perimeter_C > prod_diagonal_C:
    F[:size, :size], F[:size, size:] = C, B  
else:
    F[:size, :size], F[size:, :size] = E, B  

det_A = np.linalg.det(A)
sum_diag_F = np.sum(np.diag(F))

if det_A > sum_diag_F:
    result = np.linalg.inv(A) * np.transpose(A) - K * np.linalg.inv(F)
else:
    G = np.tril(A) 
    result = (np.transpose(A) + G - np.transpose(F)) * K

print("Матрица A:")
print(A)
print("\nМатрица F:")
print(F)
print("\nРезультат:")
print(result)
