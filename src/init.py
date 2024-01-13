import cryptology.discretization

dr = cryptology.discretization.DiscretizationRandom(65, 122) 
rawResult = dr.get_discretized_random() 
password = ''
for text in rawResult:
    password += chr(text)

print(password)