#zip()

# Python3 code to demonstrate 
# conversion of lists to dictionary
# using zip()
  
# initializing lists
test_keys = ["Rash", "Kil", "Varsha"]
test_values = [1, 4, 5]
  
# Printing original keys-value lists
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))
  
# using zip()
# to convert lists to dictionary
res = dict(zip(test_keys, test_values))
  
# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))