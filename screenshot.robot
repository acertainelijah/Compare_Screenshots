*** Settings ***

Documentation  This is some information about the Suite
Library  Selenium2Library
Library  TestPythonLib

Test Setup  Screenshot
Test Teardown  Close test browser

*** Variables ***
${WEBSITE}  https://www.google.com/
${BROWSER}  chrome

*** Test Cases ***
Simple Test
    Screenshot
    Close test browser

*** Keywords ***
Screenshot
    [Documentation]  This opens browser and takes a screenshot
    [Tags]  1234
    Open Browser  ${WEBSITE} ${BROWSER}

Close test browser
    [Documentation]  This closes browser
    [Tags]  4321
    Close Browser

