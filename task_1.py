#Task 1

def list_ifname_ip(fin):
  dict = {}
  keys = []
  array = []
  for line in fin:
    line = line.strip()
    words = line.split()
    for i in range(len(words)-1):
      if("nameif" == words[i]):
        keys.append(words[i+1])
      elif("." in words[i]):
        array.append((words[i],words[i+1]))
  for i in range(len(keys)):
    dict.update({keys[i] : array[i]})
  return dict

final = open("running-config.cfg")
directory = list_ifname_ip(final)
print(directory)
