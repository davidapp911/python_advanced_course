*** Settings ***
Resource    common.resource
Resource    ../variables/locator.resource

*** Keywords ***
Navigate To EPAM
    [Documentation]    Opens the EPAM webpage. Deals with cookies notice as well
    Open Webpage    ${url}
    Click On Button If Present    ${cookie_button_text}
    
Go To Careers Page
    [Documentation]    Clicks on careers link
    Click Element By Link Text    ${careers}
    
Set Job Preferences    
    [Documentation]    Sets the job preferences remote, location, and enters a keyword on input field
    [Arguments]    ${keyword}
    Input Keyword To Text Field    ${field_id}    ${keyword}
    Click Element By Class    ${location_arrow_class}
    Click Element By Title    ${location_title}
    Click Label With For Attribute    ${remote_for}
    
Search Jobs
    [Documentation]    Clicks on the find button of the careers page
    Click Button By Text    ${find_button_text}
    
Open Latest Search Result
    [Documentation]    Scrolls down to search results and clicks on the top result
    Scroll To By Class    ${results_title_class}
    Click Element By Link Text    ${apply_button_text}

Click Magnifier Glass
    [Documentation]    Clicks on the magnifier glass on the top right corner of the page
    Click Element By Class    ${magnifier_class}
    
Search For Posts Related To
    [Documentation]    Inputs keyword into the search field and clicks on find button
    [Arguments]    ${keyword}
    Input Keyword To Text Field    ${search_field_id}    ${keyword}
    Click Element By Class    ${find_button_class}