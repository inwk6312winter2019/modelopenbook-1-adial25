#Task 3
final3 = open("running-config.cfg")

transit_access_in = []
fw_management_access_in = []
global_access = []

for line in final3:
  line = line.strip()
  if("transit_access_in" in line):
    transit_access_in.append(line)
  elif("fw-management_access_in" in line):
    fw_management_access_in.append(line)
  elif("global_access" in line):
    global_access.append(line)


print(transit_access_in)
print(fw_management_access_in)
print(global_access)
