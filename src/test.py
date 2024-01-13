import cryptology.discretization

dr = cryptology.discretization.DiscretizationRandom(1, 4) 
result = dr.get_discretized_random() 
print(result)