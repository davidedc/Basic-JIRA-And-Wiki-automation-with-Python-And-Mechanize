# This script aggregates all of the above: fetches JIRA tickets from a search,
# then filters the tickets into a report, then performs some cosmetic changes to the
# report, then puts the report in a wiki page.
# some code taken from http://www.mattryall.net/blog/2008/06/confluence-python
 
import sys, string, xmlrpclib, re
 
if len(sys.argv) < 3:
   exit("Usage: " + sys.argv[0] + " spacekey pagetitle");
 
input = "".join(sys.stdin.readlines()).rstrip();
spacekey = sys.argv[1];
pagetitle = sys.argv[2];
 
server = xmlrpclib.ServerProxy('https://wiki.shazamteam.net/rpc/xmlrpc');
token = server.confluence1.login('YOUR LOGIN', 'YOUR PASSWORD');
page = server.confluence1.getPage(token, spacekey, pagetitle);
print page
 
if page is None:
   exit("Could not find page " + spacekey + ":" + pagetitle);
 
content = input
 
page['content'] = content;
server.confluence1.storePage(token, page);
This script aggregates all of the above: fetches JIRA tickets from a search, then filters the tickets into a report, then performs some cosmetic changes to the report, then puts the report in a wiki page
puttingContentInAWikiPage.py
import sys, string, xmlrpclib, re, time, datetime
from mechanize import ParseResponse, urlopen, urljoin
 
theLogin = "YOUR JIRA + WIKI LOGIN"
thePassword = "YOUR JIRA + WIKI PASSWORD"
 
 
# build the login URL and get the page
uri = "https://YOUR JIRA URL"
response = urlopen(urljoin(uri, "login.jsp"))
 
# get the first form in the page and print it
forms = ParseResponse(response, backwards_compat=False)
form = forms[0]
# print form
 
# fills the form
form["os_username"] = theLogin
form["os_password"] = thePassword
 
# press click
request2 = form.click()
response2 = urlopen(request2)
 
response3 = urlopen(urljoin(uri, "sr/jira.issueviews:searchrequest-xml/10655/SearchRequest-10655.xml?tempMax=1000"))
 
# print response3.read()
 
# txt='<issuekey id="28020">APS-2862</issuekey>'
txt=response3.read()
 
#########################################################
# filter the xml output of the search so to highlight
# the dependencies. Lots of regexes here.
#########################################################
 
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
 
report = "*Notes:*\n\n"
report = report + "* the unindented tickets are the blocked ones,"
report = report + "the indented tickets are the blocking ones\n\n"
report = report + "* only tickets from the following search are being shown:\n"
report = report + 'issuetype in (Bug, Phone, "SIM Card", "Software Deployment Request", "Handset Builds Deployment Request", Epic, Story, "Store Link Request", "New Feature", "Service Issue", Task, "Change Request", Issue, Port, Solution, "Solution Risk", "Solution Issue", "Technical task", "Solution Milestone") AND resolution = Unresolved AND status in (Open, Reopened, "In Progress", "Work Blocked", "In Testing", "Awaiting Testing",Submitted, Qualifying, Scoping, Defining, Delivering, Supporting, Assigned) AND created >= 2011-03-25'
report = report + "\n\n_Report automatically generated on: " + str(datetime.datetime.now()) + "_\n\n----\n"
 
for m in re.finditer(rg, txt):
 report = report + '\-&nbsp;' + m.group(0) + '\n'
 
#########################################################
# now some cosmetic changes to the report
#########################################################
 
rg2 = re.compile(reB1+reB2+reB3+reB4+reB5+reB6+reB7+reB8+reB9+reB10,re.IGNORECASE)
report = rg2.sub("", report)
 
rg3 = re.compile("(<\\/key>)|(<\\/issuekey>)",re.IGNORECASE)
report = rg3.sub("", report)
 
rg4 = re.compile(re1+re2+re3+re4+re5+re6+re7,re.IGNORECASE)
report = rg4.sub("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;", report)
 
 
#########################################################
# now save the report as a wiki page
#########################################################
 
spacekey = "ENGINEERING";
pagetitle = "JIRA Issues - dependency report";
 
server = xmlrpclib.ServerProxy('https://wiki.shazamteam.net/rpc/xmlrpc');
token = server.confluence1.login(theLogin, thePassword);
page = server.confluence1.getPage(token, spacekey, pagetitle);
# print page
 
if page is None:
   exit("Could not find page " + spacekey + ":" + pagetitle);
 
page['content'] = report;
server.confluence1.storePage(token, page);