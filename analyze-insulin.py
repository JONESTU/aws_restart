import re
import sys

sequence = open('/home/ec2-user/environment/preproinsulin-seq.txt').read()

preproinsulinSeq = re.sub(pattern=r'[^a-z]', repl='', string=sequence)
print("Preproinsulin: ", preproinsulinSeq, "\nCharacters: ", len(preproinsulinSeq), "\nWriting file...\n")
preproinsulinFile = open("preproinsulin-seq-clean.txt", "x")
preproinsulinFile = open("preproinsulin-seq-clean.txt", "w")
preproinsulinFile.write(preproinsulinSeq)
preproinsulinFile.close()

lsinsulinSeq = preproinsulinSeq[:24]
print("Lsinsulin: ", lsinsulinSeq, "\nCharacters: ", len(lsinsulinSeq), "\nWriting file...\n")
lsinsulinFile = open("lsinsulin-seq-clean.txt", "x")
lsinsulinFile = open("lsinsulin-seq-clean.txt", "w")
lsinsulinFile.write(lsinsulinSeq)
lsinsulinFile.close()

binsulinSeq = preproinsulinSeq[24:54]
print("Binsulin: ", binsulinSeq, "\nCharacters: ", len(binsulinSeq), "\nWriting file...\n")
binsulinFile = open("binsulin-seq-clean.txt", "x")
binsulinFile = open("binsulin-seq-clean.txt", "w")
binsulinFile.write(binsulinSeq)
binsulinFile.close()

cinsulinSeq = preproinsulinSeq[54:89]
print("Cinsulin: ", cinsulinSeq, "\nCharacters: ", len(cinsulinSeq), "\nWriting file...\n")
cinsulinFile = open("cinsulin-seq-clean.txt", "x")
cinsulinFile = open("cinsulin-seq-clean.txt", "w")
cinsulinFile.write(cinsulinSeq)
cinsulinFile.close()

ainsulinSeq = preproinsulinSeq[89:110]
print("Ainsulin: ", ainsulinSeq, "\nCharacters: ", len(ainsulinSeq), "\nWriting file...\n")
ainsulinFile = open("ainsulin-seq-clean.txt", "x")
ainsulinFile = open("ainsulin-seq-clean.txt", "w")
ainsulinFile.write(ainsulinSeq)
ainsulinFile.close()

sys.exit()