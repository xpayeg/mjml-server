#input file
fin = open("app.yaml.temp", "rt")
#output file to write the result to
fout = open("app.yaml", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	fout.write(line.replace('$BRANCH_NAME', '123'))
#close input and output files
fin.close()
fout.close()