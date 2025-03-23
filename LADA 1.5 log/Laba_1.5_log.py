import glob

for i in glob.glob('*.log'):
    with open(i) as j:
        list_j=j.readlines()
        for s in list_j:
            if "ip address" in s:

                print(s)