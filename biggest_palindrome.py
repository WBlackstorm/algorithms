def biggest_palindrome(digits):
    begin = int('1' + ('0' * (digits - 1)))
    end = int('9'*digits)
    biggest = 0
    
    for i in range(end, begin, -1):
        for j in range(end,begin, -1):
            n = i * j
            if (str(n) == str(n)[::-1]) and (n > biggest):
                biggest = n                

    return biggest