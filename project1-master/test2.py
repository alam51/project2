import os
os.system('pwd')
os.system('cd ~')
stream = os.popen('ls -la')
output = stream.readlines()
a = 4
print(output)