*** Settings ***

Library  Selenium2Library
Library  TestingBot

Test Setup  Open test browser
Test Teardown  Close test browser


*** Variables ***

${CREDENTIALS  key:secret}


*** Test Cases ***

Simple Test 
	Go to  https://www.google.com
	Page should contain  Google


*** Keywords ***

Open test browser
	Open browser  about:  firefox
	...  remote_url=http://${CREDENTIALS}@hub.testingbot.com/wd/hub}
	...  desired capabilities=browserName:${BROWSER},version:${VERSION},platform:${PLATFORM}

Close test browser
	...  Report TestingBot status
	...  ${SUITE_NAME} | ${TEST_NAME}
	...  ${TEST_STATUS}  ${CREDENTIALS}
	Close all browsers 
