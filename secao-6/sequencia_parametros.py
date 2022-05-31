def soma_todos(*nums):
    soma = 0
    
    for num in nums:
        soma += num
        
    return soma

s = soma_todos(5,3,4,2,1,42,23,13)

print(s)

