a#write a function called linearSearchproduct that takes the list of products a

def linearsearchproduct(productlist,targetproduct):
  indices=[]

  for index,product in enumerate(productlist):
    if product==targetproduct:
      indices.append(index)
  return indices


#Example usage:
products=["Shoes","boot","loofer","Shoes","Sandal","Shoes"]
target="Shoes"
target1="apple"
result=linearsearchproduct(products,target)
result1=linearsearchproduct(products,target1)
print(result)
print(result1)     
    

