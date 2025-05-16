*** Settings ***
Library    SeleniumLibrary
Library    String

*** Keywords ***
Open Browser To Login Page
    Open Browser    https://www.demoblaze.com/    Chrome
    Maximize Browser Window

Click Login Button
    Click Element    id=login2
    Wait Until Element Is Visible    id:loginusername    timeout=5

Enter Credentials And Submit
    [Arguments]    ${username}    ${password}
    Input Text    id=loginusername    ${username}
    Input Text    id=loginpassword    ${password}
    Click Button    xpath=//button[@onclick='logIn()']
    Wait Until Page Contains Element    id=logout2    timeout=10
    Sleep    2s

Validate Successful Login
    [Arguments]    ${username}
    Element Should Be Visible    id=logout2
    Element Should Contain       id=nameofuser    Welcome ${username}
    Sleep    2s

Click Monitor Category
    Click Element    link=Monitors
    Sleep    2s
    
Add Expensive Monitor
    Wait Until Element Is Visible    xpath://div[@class='card-block']
    ${monitors}=    Get Webelements    xpath://div[@class='card-block']
    ${highest_price}=    Set Variable    0

    FOR    ${ix}    ${monitor}    IN ENUMERATE    @{monitors}
        ${price}=    Get Text    ${monitor}    xpath://h5
        ${price}=    Remove String    ${price}    $
        Log To Console    ${price}

    END