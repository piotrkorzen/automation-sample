#!/bin/bash

VISIBLE=1

echo "Running Selenium Server..."
if [ $VISIBLE == 0 ]; then
    java -Dwebdriver.chrome.driver=./chromedriver.exe.exe -jar ./selenium_grid/selenium-server-standalone-3.141.0.jar -role hub -hubConfig ./selenium_grid/conf.json & xvfb-run --server-args="-screen 0, 2560x2560x24" java -Dwebdriver.chrome.driver=./chromedriver.exe.exe -jar ./selenium_grid/selenium-server-standalone-3.141.0.jar -role node -nodeConfig ./selenium_grid/node.json
else
      java -Dwebdriver.chrome.driver=./chromedriver.exe.exe -jar ./selenium_grid/selenium-server-standalone-3.141.0.jar -role hub -hubConfig ./selenium_grid/conf.json & java -Dwebdriver.chrome.driver=./chromedriver.exe.exe -jar ./selenium_grid/selenium-server-standalone-3.141.0.jar -role node -nodeConfig ./selenium_grid/node.json
fi
