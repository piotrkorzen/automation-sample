#!/bin/bash
echo "Running Selenium Server..."
java -Dwebdriver.chrome.driver=./chromedriver.exe -jar ./selenium_grid/selenium-server-standalone-3.141.0.jar -role hub -hubConfig ./selenium_grid/conf.json & xvfb-run --server-args="-screen 0, 2560x2560x24" java -Dwebdriver.chrome.driver=./chromedriver.exe -jar ./selenium_grid/selenium-server-standalone-3.141.0.jar -role node -nodeConfig ./selenium_grid/node.json &