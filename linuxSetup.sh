#!/usr/bin/bash

# Get the webdriver for firefox (geckodriver)
wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz 

# extract
tar -xvf geckodriver-v0.26.0-linux64.tar.gz

# Move
sudo mv ./geckodriver /usr/bin
