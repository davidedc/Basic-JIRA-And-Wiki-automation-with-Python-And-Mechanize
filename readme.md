If one wants to export data from JIRA, the best way is get database exports from the backend.

It might be occasionally needed to do basic automation for which there is no API or way to tweak the back-end, by accessing directly the web UI interface. Also this might be handy for some quick automation hacks.

(Note that there is always a risk to automatically perform unintended operations, so use your best judgement!

This solution consists in using Python + a library called Mechanize (originally a PERL library) used for web testing and for screen scraping where APIs or backend access is not available.

Python is already installed on OSX. For Windows installation there are several tutorials online.

To install Mechanize:
* install EasyInstall (look up on google)
* then, from command line  ```easy_install mechanize```

Then take a look and use the scripts in this repo (replace your configuration first). Then run them in command line doing:
```python [name of script].py```

One of these example scripts logs you in JIRA and prints the landing page, one runs a search, and one puts a dependency analisys in a wiki (confluence) page of your choice, here is how the final report looks like in this case:
