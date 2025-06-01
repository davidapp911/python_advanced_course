*** Settings ***
Library    SeleniumLibrary
Library    String

*** Keywords ***
Open Webpage
    [Documentation]    Opens a browser and navigates to the given url
    [Arguments]    ${url}
    Open Browser    ${url}    Chrome
    Maximize Browser Window

Click On Button If Present
    [Documentation]    Clicks on button when present
    [Arguments]    ${button_text}
    ${is_present}=    Run Keyword And Return Status    Element Should Be Visible    xpath://button[text()="${button_text}"]
    IF    ${is_present}
        Click Element    xpath://button[text()="${button_text}"]
    ELSE
        No Operation
    END
    
Click Element By Link Text
    [Documentation]    Clicks on Webelement that contains a given text
    [Arguments]    ${link_text}
    Wait Until Element Is Visible    link:${link_text}
    Click Element    link:${link_text}
    
Input Keyword To Text Field
    [Documentation]    Send a given input keyword to text field by id
    [Arguments]    ${field_id}    ${keyword}
    Wait Until Element Is Visible    id:${field_id}
    Input Text    id:${field_id}    ${keyword}

Click Element By Class
    [Documentation]    Clicks on Webelement that contains a given class
    [Arguments]    ${classname}
    Wait Until Element Is Visible    class:${classname}
    Click Element    class:${classname}
    
Click Element By Title
    [Documentation]    Clicks on Webelement that contains a given title
    [Arguments]    ${title}
    Wait Until Element Is Visible    //li[@title='${title}']
    Click Element    //li[@title='${title}']
    
Click Element By Id
    [Documentation]    Clicks on Webelement that contains a given id
    [Arguments]    ${id}
    Wait Until Element Is Visible    id:${id}
    Click Element    id:${id}

Click Label With For Attribute
    [Documentation]    Clicks on a label Webelement that contains a given for attribute
    [Arguments]    ${for}
    Wait Until Element Is Visible    css=label[for='${for}']
    Click Element    css=label[for='${for}']
    
Click Button By Text
    [Documentation]    Clicks on a button that contains a given text
    [Arguments]    ${text}
    Click Element    xpath://button[contains(text(), '${text}')]
    
Scroll To By Class
    [Documentation]    Scrolls screen to the element with the given class
    [Arguments]    ${class}
    Wait Until Element Is Enabled    class:${class}
    Scroll Element Into View    class:${class}
    
Validate Keyword In Page Body
    [Documentation]    Search for the presence of a given keyword anywhere in the page
    [Arguments]    ${keyword}
    Wait Until Element Is Visible    xpath://body
    Sleep    1s
    ${body_text}=    Get Text        xpath=//body
    
    Should Match Regexp    ${body_text}    (?i).*${keyword}.*

Get Buttons List
    [Documentation]    Returns a list of buttons with a given text
    [Arguments]    ${text}
    @{button_list}=    Get Webelements    xpath://button[contains(text(), '${text}')]
    Return From Keyword    @{button_list}