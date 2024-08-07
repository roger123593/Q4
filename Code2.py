def is_magic_square(matrix):
    N = len(matrix)
    if N == 0:
        return "It is NOT a magic square!"

    # 計算目標和
    target_sum = N * (N ** 2 + 1) // 2

    row_sums = [0] * N   # 存每一行的和
    col_sums = [0] * N   # 存每一列的和
    main_diag_sum = 0    # 存主對角線的和
    anti_diag_sum = 0    # 存副對角線的和
    numbers_set = set()  # 存所有出現過的數字

    # 開始對矩陣的數字做判斷
    for i in range(N):
        for j in range(N):
            num = matrix[i][j]
            if num < 1 or num > N ** 2:
                return "It is NOT a magic square!"
            numbers_set.add(num)
            row_sums[i] += num
            col_sums[j] += num
            if i == j:
                main_diag_sum += num
            if i == N - 1 - j:
                anti_diag_sum += num

    # 檢查是否包含所有1到N^2的數字
    expected_numbers = set(range(1, N ** 2 + 1))
    if numbers_set != expected_numbers:
        return "It is NOT a magic square!"

    # 檢查行列的和是否等於目標和
    if any(s != target_sum for s in row_sums) or any(s != target_sum for s in col_sums):
        return "It is NOT a magic square!"

    # 檢查對角線
    if main_diag_sum != target_sum or anti_diag_sum != target_sum:
        return "It is NOT a magic square!"

    return "It is a magic square!"


# 測試

# 3x3 魔方陣
input_array_1 = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

# 3x3 非魔方陣
input_array_2 = [
    [4, 9, 2],
    [3, 5, 6],
    [8, 1, 7]
]

# 4x4 魔方陣
input_array_3 = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
]

# 4x4 非魔方陣
input_array_4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(is_magic_square(input_array_1))
print(is_magic_square(input_array_2))
print(is_magic_square(input_array_3))
print(is_magic_square(input_array_4))
