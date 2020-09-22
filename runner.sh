#!/bin/bash
pip install virtualenv
virtualenv venv
source venv/bin/activate
curl -o allure-2.6.0.tgz -Ls https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.6.0/allure-2.6.0.tgz
sudo tar -zxvf allure-2.6.0.tgz -C /opt/
sudo ln -s /opt/allure-2.6.0/bin/allure /usr/bin/allure
allure --version
pip install -r ./requirements.txt
behave -f allure_behave.formatter:AllureFormatter -o ./report/ ./features/*.feature
allure serve ./report/
