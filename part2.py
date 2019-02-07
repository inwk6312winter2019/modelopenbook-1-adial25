with open('running-config.cfg') as f:
 newText=f.read().replace('192', '10')
 newText=f.read().replace('172', '10')
 newText=f.read().replace('255.255.0.0','255.0.0.0')
 newText=f.read().replace('255.255.255.0','255.0.0.0')
with open('running-config.cfg', "w") as f:
 f.write(newText)
