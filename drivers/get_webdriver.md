#### get chrome webdrivers

##### chrome driver version
ChromeDriver 101.0.4951.41

##### download webdriver

```
https://chromedriver.chromium.org/downloads

mac: https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_mac64.zip
linux: https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip
windows: https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_win32.zip
```


#### replace its binary with perl

```
perl -pi -e 's/cdc_/dog_/g' /path-to-driver
```
