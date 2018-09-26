def rangoli(n):
    width = n * 4 - 3
    letters = 'abcdefghijklmnopqrstuvwxyz'
    limit1 = n
    limit2 = 1
    
    while limit1 > 0:       
        content = letters[limit1 - 1:n][::-1] + letters[limit1:n]
        strLine = '-'.join(content)
        print(strLine.center(width, '-'))  
        limit1 -= 1
        
    while limit2 < n:        
        content = letters[limit2:n][::-1] + letters[limit2 + 1:n]
        strLine = '-'.join(content)
        print(strLine.center(width, '-'))  
        limit2 += 1