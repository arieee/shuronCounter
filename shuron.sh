#!/bin/sh

cd $HOME/Dropbox/shuron
python shuronExplorer.py >>/home/ari/www/arieee.net/public_html/shuron/data
python shuronJsoner.py >/home/ari/www/arieee.net/public_html/shuron/shuron.json
