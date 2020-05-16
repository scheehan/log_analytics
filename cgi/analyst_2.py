#!/usr/bin/python3

import pandas as pd
from pandas.compat import StringIO
import os
from pathlib import Path
import subprocess
import re

filepath = '/var/www/wou/tmp/'

with open("/var/www/wou/data/filelist.txt", "r") as file:
   for last_line in file:
      pass
   file.close()

lastfilename = last_line

rc = subprocess.call('/var/www/wou/cgi/get_info.sh')

with open("/var/www/wou/data/client_info.txt", "r") as file:
   for last_access_line in file:
      pass
   file.close()

#r1 = re.findall(r"^[0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}\s", last_access_line)

command_output = os.popen('tail -n1 /var/www/wou/data/client_info.log')
#r1 = re.findall(r"^[0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}.[0-9]{2,3}\s", command_output.read())
r2 = re.findall(r" [lLwW].{4,11}", command_output.read())

file_to_open = filepath + lastfilename.rstrip()

f = open(file_to_open, 'r')
datainfo = f.readlines(3)

lines = list(f)
f.close()

df = pd.read_csv(file_to_open, names=['Time','Severity','Text'], engine='python')
df.to_html('../output.html', justify='center')

print("Content-Type: text/html\n")
print("<html>\n")
print("""\

<head>
  <meta charset="utf-8">
  <title>Data Analytic Output</title>
  <meta name="description" content="Basic Data output">
  <meta name="author" content="vasikadedomena">
  <link rel="stylesheet" href="../css/styles.css">
</head>
""")
print("<body>\n")
print("<p>You are using a {} system</p>".format(r2))
print("\n")
print("<p>Returns of your data filename: {}</p>".format(lastfilename))
print("""\

<object data="/tmp/{}" type="text/plain" width="500" style="height: 150px"></object>

""".format(lastfilename))

print("""\

<div class="box-1">
<iframe src="https://www.vasikadedomena.site/output.html" style="border: none; width: 600px; height: 300px;" ></iframe>
</div>

<div class="box-2">
        <button onclick="window.location.href='https://www.vasikadedomena.site';">Back To Main Page</button>
        
</div>

</body>
</html>
""")
