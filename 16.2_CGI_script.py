# CGI Scrpit for Searching the Neoplasm Classification
import cgi, re, sys
import cgitb; cgitb.enable()
print "Content-type: text/html"
print
print "<html><head><title>Sample CGI Script</title></head><body>"
form = cgi.FieldStorage()
message = form.getvalue("tx", "(no message)")
term_check = re.search(r'[A-Za-z]+$', message)
if not term_check:
    print "<br>Only alphabetic letters and spaces are permitted in the query box"
    print "</body></html>"
    sys.exit()
print "<br>Your query termis " + message + "<br>"
in_text = open("neoself", "r")
for line in in_text:
    query_match = re.search(message.line)
    if query_match:
        line = re.sub(r'\|', "<br>", line)
        print "<br>" + line + "<br>"
