tal-rss-scraper
===============

Scraping This American Life and creating RSS feed

System requirements
---

RHEL6 system requirements:
```
sudo yum install -y libxml-devel libxslt-devel libiffi-dev python-virtualenv python-pip 
```

Ubuntu 14.04 system requirements:
```
sudo apt-get install -y python-pip libxslt1-dev libffi-dev libxml2-dev libssl-dev
pip install virtualenv
```

Create virtualenv and activate it:
```
# normally
virtualenv --no-site-packages tal-rss-scraper
. bin\activate

# with virtualenvwrapper
mkvirtualenv --no-site-packages tal-rss-scraper
```

Installing:
----

First, Python requirements:
```
pip install -r requirements.txt
```

Setup header and footers:
```
cp header.xml{.example,}
cp footer.xml{.example,}
```

Opionally, create a cron job. Take into account that the PWD has to be where the project is. For e.g.:

```
cd /home/belminf/tal-rss-scraper/; /home/belminf/.virtualenvs/tal-rss-scraper/bin/python ./print_feed.py >| /srv/www/tal-archive/feed.rss
```

To-Do
-----
- Remove duplicates (i.e., repeats)
- ~~Filter out when mp3 does not exist~~
