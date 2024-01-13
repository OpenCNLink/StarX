import cryptology.discretization

dr = cryptology.discretization.DiscretizationRandom(65, 122) 
result = dr.get_discretized_random() 
print(result)