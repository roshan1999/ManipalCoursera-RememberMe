import hashlib 
  
# initializing string 
str = "Secret_msg_here"
  
result = hashlib.md5(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of hash is : ", end ="") 
print(result.hexdigest()) 
