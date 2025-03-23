import glob
import re
ip_list=[]
for i in glob.glob('*.log'):
    with open(i) as j:
        list_j=j.readlines()
        for s in list_j:
            if "ip address" in s:
                ip_and_mask_str = " ".join(re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', s))
                if ip_and_mask_str:
                    ip_list.append(ip_and_mask_str)
for ip in list(set(ip_list)):
    print(ip)