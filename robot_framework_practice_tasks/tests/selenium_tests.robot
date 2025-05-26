*** Settings ***
Resource    ../keywords/selenium.resource
Variables    ../variables/selenium.py

*** Test Cases ***
Test Login Correct Messages
    FOR    ${single_user}    IN    @{USERNAME_DATA_SHORT}
        ${username}    ${expected}=    Evaluate    list(${single_user})
        
        IF    '${expected}' == 'success'
            Navigate To Saucedemo
            Login User    ${username}
            Validate Navigation To Products Page
            
        ELSE IF    '${expected}' == 'error'
            Navigate To Saucedemo
            Login User    ${username}
            Validate That Error Message Appears
        END

        Close Browser
    END
    [Teardown]