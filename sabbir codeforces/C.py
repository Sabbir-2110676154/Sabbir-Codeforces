def contest():
    n = int(input())
    s = input()
    zeros = s.count('0')
    ones = n - zeros
    result = []
    left_zeros = 0
    left_ones = 0
    for i in range(n):
        if s[i] == '0':
            left_zeros += 1
        if s[i] == '1':
            left_ones += 1
        
        right_zeros = zeros - left_zeros
        right_ones = ones - left_ones
        left = (i + 2) // 2
        right = (n - i) // 2

        if left_zeros >= left and right_ones >= right:
            result.append(1)
        else:
            result.append(0)
    
    middle = n / 2
    distances = []
    for i in range(len(result)):
        if result[i] == 1:
            temp = middle - (i + 1)
            distances.append((abs(temp), i + 1))
    
    flag = 0
    mini = (n + 1) // 2
    if ones >= mini:
        flag = 1
    
    if flag == 1:
        distances.append((middle, 0))
    
    distances.sort()
    print(distances[0][1])

T = int(input())
for _ in range(T):
    contest()