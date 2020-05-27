#!/usr/bin/python3

import pandas as pd
from pandas.compat import StringIO
import os
from pathlib import Path
import subprocess
import re
import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt

# identify folder path
filepath = '/var/www/wou/tmp/'

# identify upload target filename
with open("/var/www/wou/data/filelist.txt", "r") as file:
   for last_line in file:
      pass
   file.close()

# assign uploaded target filename as variable
lastfilename = last_line

# open apache client_info file to get client info
command_output = os.popen('tail -n1 /var/www/wou/data/client_info.log')

r2 = re.findall(r" [lLwW][iI][nN].{4,11} ", command_output.read())

# merge folder path with filename
file_to_open = filepath + lastfilename.rstrip()

# open the target file
f = open(file_to_open, 'r')
datainfo = f.readlines(3)

lines = list(f)
f.close()

df = pd.read_csv(file_to_open, names=['Time','Severity','Text'], engine='python')

# export as html 
df.to_html('../output.html', justify='center')

# generate pie chart and calculate percentage based on severity column
df.Severity.value_counts().plot.pie(y='Severities', figsize=(7, 7),autopct='%1.1f%%', startangle=90)
plt.savefig('../images/chart_output.png')

# generate HTML page
print("Content-Type: text/html\n")
print("<html>\n")
print("""\

<head>
  <meta charset="utf-8">
  <title>Data Analytic Output</title>
  <meta name="description" content="Basic Data output">
  <meta name="author" content="vasikadedomena">
  <link rel="stylesheet" href="../css/styles.css" />
</head>
""")
print("<body>\n")
print("<p>You are using a {} system</p>".format(r2))
print("\n")
print("<p>Returns of your data filename: {}</p>".format(lastfilename))
print("""\

<object data="/tmp/{}" type="text/plain" width="800" style="height: 300px"></object>

""".format(lastfilename))

print("""\

<div class="box-1">
<iframe src="https://www.vasikadedomena.site/output.html" style="border: none; width: 600px; height: 300px;" ></ifram$
</div>

<div class="image-box-1">
<img src='../images/chart_output.png'>
</div>

<div class="box-2">
        <button onclick="window.location.href='https://www.vasikadedomena.site';">Back To Main Page</button>
        
</div>

</body>
</html>
""")
