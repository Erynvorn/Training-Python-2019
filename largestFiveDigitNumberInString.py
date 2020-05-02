def solution(digits):
    max = 0
    for i in range(len(digits)-4):
        if max  <= int(digits[i:i+5]):
            max = int(digits[i:i+5])
    return max
