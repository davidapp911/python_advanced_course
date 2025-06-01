*** Settings ***
Resource    common.resource
Resource    ../variables/selenium.resource

*** Keywords ***
Navigate To Saucedemo
    [Documentation]    Opens a web browser and navigates to https://www.saucedemo.com
    Open Webpage    ${URL}

Login User
    [Documentation]    Enters username information to login
    [Arguments]    ${username}=standard_user    ${password}=secret_sauce
    Input Keyword To Text Field    ${USERNAME_FIELD_ID}    ${username}
    Input Keyword To Text Field    ${PASSWORD_FIELD_ID}    ${password}
    Click Element By Id    ${LOGIN_BUTTON_ID}
    Sleep    1s

Validate Navigation To Products Page
    [Documentation]    Validates whether the title of the page after login is the correct one
    Wait Until Page Contains Element       id:${PRODUCTS_HEAD_ID}
    ${title}=    Get Text    class:${PRODUCTS_PAGE_TITLE_CLASS}
    Should Be Equal    ${title}    Products
    
Validate That Error Message Appears
    [Documentation]    Validates that error message appears for login error
    ${message}=    Get Text    css:[data-test=${ERROR_DATA_TEST}]
    Should Contain    ${message}    ${ERROR_TEXT}
    
Add Items To Cart
    [Documentation]    Add n amount of different items to the cart
    [Arguments]    ${number_of_items}=1

    @{button_list}=    Get Buttons List    ${CART_BUTTON_TEXT}

#    FOR    ${ix}    IN RANGE    ${number_of_items}
#        ${button}=    Evaluate    ${button_list}[${ix}]
#        Click Element    ${button}
#        Sleep    1s
#    END
#
#    Sleep    2s