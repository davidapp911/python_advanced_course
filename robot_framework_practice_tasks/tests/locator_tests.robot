*** Settings ***
Library    SeleniumLibrary
Resource    ../libraries/common.resource
Resource    ../variables/locator_variables.resource

*** Test Cases ***
Job Search Based on Keywords
    Open Webpage    ${url}
    Click On Button If Present    ${cookie_button_text}
    Click Element By Link Text    ${careers}
    Input Keyword To Text Field    ${field_id}    ${coding_language}
    Click Element By Class    ${location_arrow_class}
    Click Element By Title    ${location_title}
    Click Label With For Attribute    ${remote_for}
    Click Button By Text    ${find_button_text}
    Scroll To By Class    ${results_title_class}
    Click Element By Link Text    ${apply_button_text}
    Search For Keyword In Body    ${coding_language}
    [Teardown]    Close Browser

Global Search Validation
    FOR    ${search_term}    IN    @{search_list}
        Open Webpage    https://www.epam.com
        Click On Button If Present    ${cookie_button_text}
        Click Element By Class    ${magnifier_class}
        Input Keyword To Text Field    ${search_field_id}    ${search_term}
        Click Element By Class    ${find_button_class}
        Search For Keyword In Body    ${search_term}
        Close Browser
    END
    [Teardown]
    
Debug Search Term
    Log To Console    ${test_var}