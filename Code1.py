def count_pair(target, numbers):
    seen = set() #記錄遍歷過的數字
    count = 0 #符合條件的數量
    for num in numbers:
        complement = target - num #所需的配對數字
        if complement in seen:
            count += 1
        seen.add(num) #將當前數字加到set中

    return count


print(count_pair(9, [3, 4, 7, 2, 5, 18]))  # Output: 2
print(count_pair(13, [4, 11, 2, 7, 9, 6]))  # Output: 3
print(count_pair(4, [5, 7, 1, 19]))  # Output: 0