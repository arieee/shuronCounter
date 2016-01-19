# Usage
## prepare VPS or some server to host web and run script to count shuron word

## make M2 to put each shuron in specific share folder of dropbox

## synchronize dropbox folder in the server
ex. see dropbox.py

http://qiita.com/yudoufu/items/163f9c9b6b9fa2f4bf9e

## put script and html in the right place of the server
see also 

https://github.com/arieee/shuronCounterWeb

## set crontab to count shuron word

ex. add following sentence


```
0 0,6,12,18 * * * /home/ari/Dropbox/shuron/shuron.sh
```

Good luck!!!!!!!!!