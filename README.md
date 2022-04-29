This framework follows the page object model approach

First please take the checkout of master branch then download the required dependencies.

There are few additional libraries which need to be downloaded.
Appium-Python-Client	2.2.0	2.2.0
allure-pytest	2.9.45	2.9.45
allure-python-commons	2.9.45	2.9.45
pip	22.0.4	22.0.4
pip-tools	6.1.0	6.6.0
pytest	6.2.4	7.1.2
pytest-order	1.0.1	1.0.1

I am running test cases using pytest.

Reporting : - for the reporting I am using allure. Allure report will have screenshot for failed test cases. 
Logger : For the logging purpose I am using custom logger
Screenshots : - I have written the code to attach screenshot to allure in case of failure, also capturing screenshot on app launch and few other places.


to run the project

Go to root directory of framework

run below command
 **python -m pytest --alluredir=/Orderbird/reports/allurereports -v -s EchoBoxTest.py**
 
 --alluredir - is the directory where allure report will be generated
 EchoBoxTest.py is the class name where test cases are available for EchoBox
 
 Once above command get executed then run 
 
** allure serve** 
 
 this will create allure report and launch it in browser.
 
 
 All the test cases are present under tests package. Classes for test cases are EchoBoxTest.py, ListDemoTest.py and LoginScreenTest.py
 
 Due to the time constraints I have written few cases only, also couldn't enhance the framework much.
 
 Please do let me know in case of you have any questions.
 
 Test cases are present under **Orderbird AG.xlsx** file which is available in root.
 
