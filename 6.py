def outer_function(x):
     def inner_function(factor):
          return x*factor
     result = inner_function(2)
     return result
print(outer_function(3))
