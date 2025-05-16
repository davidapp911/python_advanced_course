*** Settings ***
Library    SeleniumLibrary
Resource   ../libraries/login_keywords.robot

*** Variables ***
${USERNAME}    someuser2
${PASSWORD}    afkpc123

*** Test Cases ***
Login With Valid User
    Open Browser To Login Page
    Click Login Button
    Enter Credentials And Submit    ${USERNAME}    ${PASSWORD}
    Validate Successful Login    ${USERNAME}
    Close Browser
    
Add Monitor To Cart
    Open Browser To Login Page
    Click Login Button
    Enter Credentials And Submit    ${USERNAME}    ${PASSWORD}
    Click Monitor Category
    Add Expensive Monitor
