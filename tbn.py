import os
import sys

os.system('sudo mv protobuf /home/vsa01/Desktop/tensorflow1/models/research')
os.system('mv os_research.py /home/vsa01/Desktop/tensorflow1/models/research')

os.chdir('/home/vsa01/Desktop/Train_node/training')
os.system('python3 mv.py')

os.chdir('/home/vsa01/Desktop/tensorflow1/models/research')
os.system('os_research.py')




