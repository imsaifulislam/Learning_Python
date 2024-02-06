""" def clean_string(text):
    remove_chars = ":,;.-"
    # clean_string = "".join(char for char in text if char not in remove_chars)
    
    clean_string = ""
    for char in text:
        if char not in remove_chars:
            clean_string +=char
            
    return clean_string

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

output = clean_string(s)
print(output) """


# ========== Clean Text In String ===============

""" def cleanString(text):
    remove_string = ":,;-."
    
    clean_text = ""
    
    for char in text:
        if char not in remove_string:
            clean_text += char
    
    return clean_text

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = cleanString(s)
print(output) """

# ==============================================


""" def final_string(text):
  
  remove_string = ":,;.-"
#  => Select Remove String
  
  clean_string = "" 
#  => store String In This Variable
  
  for char in text: # -> loop run iN Text(s)
      if char not in remove_string: #-> যেগুলো remove_string,char এর মধ্যে পাবেনা 
          clean_string += char #-> সেগুলো clean_string এ জমা হবে
          
  return clean_string
    

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = final_string(s)
print(output) """







def final_string(text):
  
  remove_str = ":;,-."
  
  clean_str = ""
  
  for char in text:
    if char not in remove_str:
      clean_str += char
  
  return clean_str
    

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output_str = final_string(s)
print(output_str)