# Problem: get an url input from the user and figure out the username
# Tolerant of the protocol(http, www), any query parameter symbols in url, strip of anything the user writes that is not an url
import re

url = input('URL: ').strip()

matches = re.search(r'^(?:https://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$', url, re.IGNORECASE) # (?:...)  --> this syntax tells re to not record that particular group wrapped. In this case (https://) & (www\.)
if matches:
  print(f'Username:',matches.group(1))  
# username = re.sub(r'^(htpps?://)?(www\.)?twitter\.com/', '', url)
# username = url.replace('https://twitter.com/','')

