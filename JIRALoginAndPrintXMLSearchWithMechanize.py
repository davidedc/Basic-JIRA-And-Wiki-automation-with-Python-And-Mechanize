# This script launches any search and outputs the results in xml.
# To use it, just replace login / password, and point it to the url of a search.
# So for example the login in this script is the xml output for new android issues.
# One can redirect the output of the script to a file for further processing.

import sys
 
from mechanize import ParseResponse, urlopen, urljoin
 
# build the login URL and get the page
 
uri = "https://YOUR JIRA URL"
 
response = urlopen(urljoin(uri, "login.jsp"))
 
# get the first form in the page and print it
 
forms = ParseResponse(response, backwards_compat=False)
 
form = forms[0]
 
# fills the form
 
form["os_username"] = "INSERT YOUR USERNAME HERE"
 
form["os_password"] = "INSERT YOUR PASSWORD HERE"
 
# press click
 
request2 = form.click()
 
response2 = urlopen(request2)
 
# now get the search result CHANGE YOUR OWN SEARCH HERE
 
response3 = urlopen(urljoin(uri, "[sr/jira.issueviews:searchrequest-xml/10578/SearchRequest-10578.xml?tempMax=1000|https://jira.shazamteam.net/sr/jira.issueviews:searchrequest-xml/10578/SearchRequest-10578.xml?tempMax=1000]"))
 
print response3.read()