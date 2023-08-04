import re # regular exp library

email = input('What\'s your email?: ').strip()

if re.search(r'^(\w|\s|\.)+@(\w\.)?\w+\.(com|edu|gov|net|in)$', email, re.IGNORECASE): # [^@] --> means allow anything except @ || \w ---> represents any word character(alpha numeric, underscore) || \s --> represents white space characters (space,tab) || ? means 0 or 1 repetitions
  print('valid')
else:
  print('Invalid')
# username, domain = email.split('@') # Returns two parts of the email

# if (username) and domain.endswith('.edu'): 
#   print('Valid')
# else:
#   print('Invalid')
  
# if '@' in email and '.' in email:
#   print('Valid')
# else:
#   print('InValid')

