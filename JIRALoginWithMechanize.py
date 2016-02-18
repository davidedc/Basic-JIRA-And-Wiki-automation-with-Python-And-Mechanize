# This script logs you in JIRA and prints the landing page.

import sys
from mechanize import ParseResponse, urlopen, urljoin
 
 
# build the login URL and get the page
uri = "https://YOUR JIRA URL"
response = urlopen(urljoin(uri, "login.jsp"))
 
 
# get the first form in the page and print it
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]
print form
 
 
# fills the form
form["os_username"] = "YOUR LOGIN"
form["os_password"] = "YOUR PASSWORD"
 
 
# press click and print response
print urlopen(form.click()).read()