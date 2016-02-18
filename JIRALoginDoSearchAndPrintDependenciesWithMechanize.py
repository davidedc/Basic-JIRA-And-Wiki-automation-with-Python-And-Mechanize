# This script extracts all the dependencies in all the tickets of a particular search.
# Again, just replace the login, password and the url of the xml view of a search.

import sys
import re
 
from mechanize import ParseResponse, urlopen, urljoin
 
# build the login URL and get the page
uri = "https://YOUR JIRA URL"
response = urlopen(urljoin(uri, "login.jsp"))
 
# get the first form in the page and print it
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]
# print form
 
# fills the form
form["os_username"] = "YOUR USERNAME"
form["os_password"] = "YOUR PASSWORD"
 
# press click
request2 = form.click()
response2 = urlopen(request2)
 
# INSERT YOUR XML VIEW URL OF A SEARCH
response3 = urlopen(urljoin(uri, "sr/jira.issueviews:searchrequest-xml/10655/SearchRequest-10655.xml?tempMax=1000"))
 
txt=response3.read()
 
# This part of the regular expression prints the key ids
reB1='(<)'   # Any Single Character 1
reB2='(k)'  # Any Single Character 2
reB3='(e)'  # Any Single Character 3
reB4='(y)'  # Any Single Character 4
reB5='(\\s+)'   # White Space 1
reB6='(i)'  # Any Single Character 5
reB7='(d)'  # Any Single Character 6
reB8='(=)'  # Any Single Character 7
reB9='(".*?")'  # Double Quote String 1
reB10='(>)'  # Any Single Character 8
reB11='((?:[a-z][a-z]+))'   # Word 1
reB12='(-)' # Any Single Character 9
reB13='(\\d+)'  # Integer Number 1
reB14='(<)'  # Any Single Character 10
reB15='(\\/)'   # Any Single Character 11
reB16='(k)' # Any Single Character 12
reB17='(e)' # Any Single Character 13
reB18='(y)' # Any Single Character 14
reB19='(>)'  # Any Single Character 15
 
 
# This part of the regular expression prints the dependencies
re1='(<)'    # Any Single Character 1
re2='(issuekey)'# Word 1
re3='(\\s+)'    # White Space 1
re4='((?:[a-z][a-z]+))' # Word 2
re5='(=)'   # Any Single Character 2
re6='(".*?")'   # Double Quote String 1
re7='(>)'    # Any Single Character 3
re8='((?:[a-z][a-z]+))' # Word 3
re9='(-)'   # Any Single Character 4
re10='(\\d+)'   # Integer Number 1
re11='(<)'   # Any Single Character 5
re12='(\\/)'    # Any Single Character 6
re13='((?:[a-z][a-z]+))'    # Word 4
re14='(>)'   # Any Single Character 7
 
rg = re.compile(reB1+reB2+reB3+reB4+reB5+reB6+reB7+reB8+reB9+reB10+reB11+reB12+reB13+reB14+reB15+reB16+reB17+reB18+reB19 + '|'+re1+re2+re3+re4+re5+re6+re7+re8+re9+re10+re11+re12+re13+re14,re.IGNORECASE)
 
 
# Prints all the matches - together with the position in the xml file
for m in re.finditer(rg, txt):
 print '%02d-%02d: %s' % (m.start(), m.end(), m.group(0))