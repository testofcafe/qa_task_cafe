# Automation test with appium framework - BDD

This is the test automation framework using Appium, Python and Behave framework with wrapper model.
And I have used Android test app (Fasthub) for writing test scenarios.


## Prerequisites

install emulator and connect to adb (debug mode)

install pycharm 

install behave

install other required packages


--------------------------------------------------

## To run

Please watch this video on aparat :
https://aparat.com/v/RwSFY

```git clone https://github.com/testofcafe/qa_task_cafe.git```

``` cd qa_task_cafe```

add execute permission to ```runner.sh``` file

```chmod +x ./runner.sh```

```./runner.sh```


--------------------------------------------------

### Explain directory of the automation
```
├── app
│   └── Fasthub.apk
├── core
│   ├── appium_wrapper.py
│   ├── config.py
│   ├── deviceInfo.yaml
│   ├── __init__.py
│   ├── session_handler.py
│   └── utils.py
├── features
│   ├── authentication.feature
│   ├── create_new_issue.feature
│   ├── edit_exist_issue.feature
│   ├── environment.py
│   ├── __init__.py
│   └── steps
│       ├── basic_authentication.py
│       ├── __init__.py
│       ├── issue.py
│       └── search.py
├── README.md
├── report
├── requirements.txt
└── runner.sh

```

#### App
contain apk file **(FastHub version 4.7.3)** 
#### core
* ```./core/appium_wrapper.py```: to simplify the implementation process. Singleton class and create only one instance
 before start scenario and after that remove instance
* ```./core/config.py```: to control appium server and init configs
* ```./core/deviceInfo.yaml```: device information (Used android emulator version 9.0 in tests)
* ```./core/session_handler.py```: to close session after each scenario
* ```./core/utils.py```: some helper contain socket checker (appium socket 4723) and time calculator decorator

#### features
* ```./features/*.feature``` There are scenario files (BDD) write with behave framework (Gherkin files)
* ```/features/steps/*.py``` implantation of feature files(scenarios) 
* ```/features/environment.py``` setUp and tearDown steps (before and after scenario/feature) configs
#### report
* final report in html format


# Note: 

cafebazaar/Hop repository archived and read-only, so when scenarios try to create an new issue get this error:

This repository has been archived by the owner. It is now read-only. 


for pass all test cases you can put ```testofcafe/qa_task_cafe``` instead of ```cafebazaar/Hop```


# Tools

| Tool                   | version |
|------------------------|---------|
| python                 | 3.8     |
| android emulator       | 9.0     |
| appium desktop (linux) | 1.15.1  |
| Appium-Python-Client   | 1.0.2   |
| selenium               | 3.141.0 |
| behave                 | 1.2.6   |
| allure-behave          | 2.8.18  |
| allure                 | 2.6.0   |


# Result test

![alt text](https://imgur.com/3CM9phx)

![alt text](https://pasteboard.co/JsARYbQ.png)
