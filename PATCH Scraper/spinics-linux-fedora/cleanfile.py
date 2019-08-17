import glob, os, fileinput
os.chdir("topics")

for file in glob.glob("*.txt"):
    for line in fileinput.input(file, inplace=True):
        line = line.strip()
        print(line, end="\n")
                        

