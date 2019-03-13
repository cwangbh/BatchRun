import os
from subprocess import Popen, PIPE
import pandas as pd

#read into the excel simulation table
parameters = pd.read_csv("Simulation plan.xlsx")
for i in len()

#generate a xml file for each line in the table


#generate all input files, save in folder Input
pathOfInput = '/media/gcf/3TB-ONE/MPM/NairnMPM/input/Python LXML Input/Input/'
for f in os.listdir(pathOfInput):
	print(f)
	Popen(['/media/gcf/3TB-ONE/MPM/NairnMPM/input/NairnMPM','-np','8',pathOfInput+f],stdin = PIPE)


