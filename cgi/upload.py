#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
import webbrowser

form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']

# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('/var/www/wou/tmp/' + fn, 'wb').write(fileitem.file.read())

   ap_file = open('/var/www/wou/data/filelist.txt', 'a')
   ap_file.write(fn + "\n")
   ap_file.close()

   message = 'The file "' + fn + '" was uploaded successfully'

elif not (fn == ('.txt') or ('.log') or ('.csv')):
   message = 'uploaded file type is not supported'

else:
   message = 'No file was uploaded'

with open("/var/log/apache2/access.log", "r") as file:
   for last_access_line in file:
      pass
   file.close()


   
print """\
Content-Type: text/html\n
<html>
<body>



   <p>%s</p>

   <div>
	<form action="analyst.py" method="post">
		<input type="submit" value="Proceed analyst" />
 	</form>
  </div>

<button onclick="window.location.href='https://www.vasikadedomena.site';">Back To Main Page</button>

</body>
</html>
""" % (message,)