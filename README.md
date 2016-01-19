# Usage
1. prepare VPS or some server to host web and run script to count shuron word

2. synchronize dropbox in the server
see dropbox.py
http://qiita.com/yudoufu/items/163f9c9b6b9fa2f4bf9e

3. put script and html in the right place of the server
see also https://github.com/arieee/shuronCounterWeb

3. set crontab to count shuron word

ex. add following sentence


```
0 0,6,12,18 * * * /home/ari/Dropbox/shuron/shuron.sh
```

Good luck!!!!!!!!!