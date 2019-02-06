*** Settings ***
Library         Selenium2Library
Library         Screencap.Screencap
Library         Screencap.Compare
#Library         tinker
#Library         /Users/marchese/Development/M2020/RobotTests/tinker.py
Test Setup      Open Google
Test Teardown   Close All Browsers

*** Test Cases ***
Take a Screenshot
    Take a Screencap

*** Variables ***
${URL}              https://www.google.com
${BROWSER}          chrome
# ${PATH}             /Users/marchese/Development/M2020/RobotsTest_gitbackup/
${PATH}             /Users/marchese/Development/M2020/RobotTests/
${SCREENSHOT_NAME}  test_screenshot.png
# How should the screenshot be passed in? Should I keep the Path and Screenshot name as 2 seperate arguments
#   or just combine into 1?
${BASE_IMAGE}   base_google_screenshot.png

*** Keywords ***
Open Google
    Open Browser        ${URL}  ${BROWSER}
    Set Window Size     1280  1024

Take a Screencap
    # take screencap      base  screenshot
    # take screencap      base_google_screenshot.png  youtube_screenshot.png
    take screencap      hplogo  ${SCREENSHOT_NAME}  ${PATH}
    compare_images      ${BASE_IMAGE}  ${PATH}/${SCREENSHOT_NAME}
