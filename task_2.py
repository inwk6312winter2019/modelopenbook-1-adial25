#Task 2

import re
final1 = open("running-config.cfg")
finalout1 = open("running-config-copy.cfg","w")
ip_pattern = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

for line in final1: 
  line = line.replace('192','10')
  line = line.replace('172','10')
  line = line.replace('255.255.0.0','255.0.0.0')
  line = line.replace('255.255.255.0','255.0.0.0')
  finalout1.write(line)
'''
  words = line.split()
  for word in words:
    if(ip_pattern.match(word)):
      if(('192' in word) or ('172' in word)):
        c = word.split('.')
        c[0] = '10'
        word = '.'.join(c)
        line.replace("192*",word)
        line.replace("172*",word)
      elif('255' in word):
        word = '255.0.0.0'
        line.replace("255*",word)
'''
