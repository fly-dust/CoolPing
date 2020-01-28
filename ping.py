import time
import subprocess
import platform
import csv

# 初始化日志文件
with open("pinglog.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Time", "Ping"])


def get_int_after(s, f): # A function for searching value
    S = s.upper()
    F = f.upper()
    par = S.partition(F)
    int_str = ""
    for c in par[2]:
        if c in ("-", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            int_str += c
        else:
            if c == ":" or c == "=" or c == " ":
                if int_str == "":
                    continue
            break
    try:
        return int(int_str)
    except: #Timeout
        return 0

def ping(pinghost):
    if(platform.system()=='Windows'): #For windows
        cmd = "ping -n 1 "+ pinghost
        cmd_result = subprocess.getoutput(cmd)
        result = get_int_after(cmd_result,"时间=")
        return result
    if(platform.system()=='Linux'): #For linux
        cmd = "ping "+ pinghost + " -c1 -W 1"
        cmd_result = subprocess.getoutput(cmd)
        result = cmd_result.split()
        result = result[-2].split("/")[0]
        if result.isalpha(): #Avoid timeout
            result = 0
        return float(result)

while True:
    print("loop running")
    host = 'baidu.com'
    x = int(time.time()) * 1000
    y = ping(host)

    with open("pinglog.csv", "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([str(x), str(y)])

    time.sleep(5)




