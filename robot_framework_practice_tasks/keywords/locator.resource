*** Settings ***
Resource    common.resource
Resource    ../variables/locator.resource

*** Keywords ***
Navigate To EPAM
    [Documentation]    Opens the EPAM webpage. Deals with cookies notice as well
    Open Webpage    ${URL}
    Click On Button If Present    ${COOKIE_BUTTON_TEXT}
    
Go To Careers Page
    [Documentation]    Clicks on careers link
    Click Element By Link Text    ${CAREERS}
    
Set Job Preferences    
    [Documentation]    Sets the job preferences remote, location, and enters a keyword on input field
    [Arguments]    ${keyword}
    Input Keyword To Text Field    ${FIELD_ID}    ${keyword}
    Click Element By Class    ${LOCATION_ARROW_CLASS}
    Click Element By Title    ${LOCATION_TITLE}
    Click Label With For Attribute    ${REMOTE_FOR}
    
Search Jobs
    [Documentation]    Clicks on the find button of the careers page
    Click Button By Text    ${FIND_BUTTON_TEXT}
    
Open Latest Search Result
    [Documentation]    Scrolls down to search results and clicks on the top result
    Scroll To By Class    ${RESULTS_TITLE_CLASS}
    Click Element By Link Text    ${APPLY_BUTTON_TEXT}

Click Magnifier Glass
    [Documentation]    Clicks on the magnifier glass on the top right corner of the page
    Click Element By Class    ${MAGNIFIER_CLASS}
    
Search For Posts Related To
    [Documentation]    Inputs keyword into the search field and clicks on find button
    [Arguments]    ${keyword}
    Input Keyword To Text Field    ${SEARCH_FIELD_ID}    ${keyword}
    Click Element By Class    ${FIND_BUTTON_CLASS}