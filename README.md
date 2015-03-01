tal-rss-scraper
===============

Scraping This American Life and creating RSS feed

RHEL6 system requirements:
```
sudo yum install -y libxml-devel libxslt-devel libiffi-dev python-virtualenv python-pip 
```

Ubuntu 14.04 system requirements:
```
sudo apt-get install -y python-pip libxslt1-dev libffi-dev libxml2-dev libssl-dev
pip install virtualenv
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

Setup header and footers:
```
cp header.xml{.example,}
cp footer.xml{.example,}
```

To-Do
-----
- Remove duplicates (i.e., repeats)
- ~~Filter out when mp3 does not exist~~
