tal-rss-scraper
===============

Scraping This American Life and creating RSS feed

System requirements (RHEL6 based distro):
```
yum install -y libxml-devel libxslt-devel libiffi-dev python-virtualenv python-pip 
```

Create virtualenv:
```
virtualenv --no-site-packages tal-rss-scraper
```

Install requirements:
```
. bin/activate
pip install -r requirements.txt
```

To-Do
-----
- Remove duplicates (i.e., repeats)
- Filter out when mp3 does not exist
