import os
import tkinter as tk
import urllib3, json
from subprocess import check_output
import subprocess
import subprocess
url = "http://localhost:8080/CallCenterAstronet/srv/astronet/ip"
http = urllib3.PoolManager()
r = http.request('GET', url)
ip = r.data.decode("utf-8")
ping = "ping " + ip
p = subprocess.Popen(ping, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
root = tk.Tk()
S = tk.Scrollbar(root)
T = tk.Text(root, height=30, width=50)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

for line in p.stdout.readlines():
    T.insert(tk.END, line.decode("utf-8"))
tk.mainloop()