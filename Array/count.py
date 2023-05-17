def count_splits_two_pointers(s):
    n = len(s)
    count = 0
    x_count_left = 0
    y_count_left = 0
    x_count_right = s.count('x')
    y_count_right = s.count('y')
    for i in range(1, n):
        if s[i-1] == 'x':
            x_count_left += 1
            x_count_right -= 1
        else:
            y_count_left += 1
            y_count_right -= 1
        if x_count_left == y_count_left and x_count_right == y_count_right:
            count += 1
    return count
    
def count_splits_two_pointers(s):
    n = len(s)
    count = 0
    x_count_left = 0
    y_count_left = 0
    x_count_right = s.count('x')
    y_count_right = s.count('y')
    for i in range(1, n):
        if s[i-1] == 'x':
            x_count_left += 1
            x_count_right -= 1
        else:
            y_count_left += 1
            y_count_right -= 1
        if x_count_left == y_count_right and y_count_left == x_count_right:
            count += 1
    return count

def count_splits(s):
    n = len(s)
    count = 0
    for i in range(1, n):
        left = s[:i]
        right = s[i:]
        x_count_left = left.count('x')
        y_count_left = left.count('y')
        x_count_right = right.count('x')
        y_count_right = right.count('y')
        if x_count_left == y_count_right or y_count_left == x_count_right:
            count += 1
    return count
print(count_splits("xaby"))