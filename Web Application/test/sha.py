import hashlib 
  
# initializing string 
str = "Enter_Secret_message_here"
  

result = hashlib.sha256(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA256 is : ") 
print(result.hexdigest()) 
  
print ("\r") 

result = hashlib.sha384(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA384 is : ") 
print(result.hexdigest()) 
  
print ("\r") 

result = hashlib.sha224(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA224 is : ") 
print(result.hexdigest()) 
  
print ("\r") 
  

result = hashlib.sha512(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA512 is : ") 
print(result.hexdigest()) 
  
print ("\r") 
  

result = hashlib.sha1(str.encode()) 
  
# printing the equivalent hexadecimal value. 
print("The hexadecimal equivalent of SHA1 is : ") 
print(result.hexdigest()) 
