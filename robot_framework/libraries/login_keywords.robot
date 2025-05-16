*** Settings ***
Library    SeleniumLibrary
Library    String

*** Keywords ***
Open Browser To Login Page
    [Documentation]    Opens a browser and navigates to the demoblaze page url
    Open Browser    https://www.demoblaze.com/    Chrome
    Maximize Browser Window

Click Login Button
    [Documentation]    Clicks on the login link of the website
    Click Element    id:login2
    Wait Until Element Is Visible    id:loginusername    timeout=5

Enter Credentials And Submit
    [Documentation]    Inputs the username and password into the proper text fields and clicks login button
    [Arguments]    ${username}    ${password}
    Input Text    id:loginusername    ${username}
    Input Text    id:loginpassword    ${password}
    Click Button    xpath=//button[@onclick='logIn()']
    Wait Until Page Contains Element    id:logout2    timeout=10
    Sleep    1s

Validate Successful Login
    [Documentation]    Checks that the login was successful
    [Arguments]    ${username}
    Element Should Be Visible    id:logout2
    Element Should Contain       id:nameofuser    Welcome ${username}
    Sleep    1s

Click Monitor Category
    [Documentation]    Navigates to the monitor category page
    Click Element    link:Monitors
    Sleep    1s
    
Add Most Expensive Monitor To Cart
    [Documentation]    Navigates to the page of the most expensive monitor and adds it to the cart
    Wait Until Element Is Visible    xpath://div[@class='card-block']
    ${monitor_links}=    Get Webelements    xpath://h4[@class='card-title']//a
    ${prices}=    Get Webelements    xpath://div[@class='card-block']//h5
    ${highest_price}=    Set Variable    0
    ${expensive_monitor}=    Set Variable

    FOR    ${ix}    ${monitor}    IN ENUMERATE    @{monitor_links}
        ${price_text}=    Get Text    ${prices}[${ix}]
        ${monitor_price}=    Price Text To Integer    ${price_text}
        
        IF    ${monitor_price} > ${highest_price}
            ${highest_price}=    Set Variable    ${monitor_price}
            ${monitor_link}=    Set Variable    ${monitor}
        END
    END

    ${monitor_name}=    Get Text    ${monitor_link}
    Click Element    ${monitor_link}

    Wait Until Element Is Visible    class:name
    ${page_title}=    Get Text    class:name
    Should Be Equal    ${monitor_name}    ${page_title}
    ${add_link}=    Get Webelement    xpath://a[contains(@class, 'btn-success')]
    Click Element    xpath://a[contains(@class, 'btn-success')]
    
    Return From Keyword    ${monitor_name}

Check Cart
    [Documentation]  Navigates to cart page and checks if the monitor was added successfully.
    [Arguments]    ${monitor_name}
    Click Element    id:cartur
    Wait Until Element Is Visible    class:success
    ${cart_item_name}=    Get Text    xpath=//tr[@class='success']/td[2]
    
    Should Be Equal    ${cart_item_name}    ${monitor_name}

    Wait Until Element Is Visible    xpath://a[contains(text(), 'Delete')]
    Click Element    xpath://a[contains(text(), 'Delete')]
    Sleep    1s

Price Text To Integer
    [Documentation]    Helper functions that takes a price in the format ex. $99 and returns an integer ex. 99
    [Arguments]    ${PriceText}
    ${price}=    Remove String    ${PriceText}    $
    ${price}=    Convert To Integer    ${price}
    Return From Keyword    ${price}