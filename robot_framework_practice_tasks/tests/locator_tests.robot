*** Settings ***
Library    SeleniumLibrary
Resource    ../keywords/locator.resource

*** Test Cases ***
Job Search Based on Keywords
    FOR    ${keyword}    IN    @{career_terms}
        Navigate To EPAM
        Go To Careers Page
        Set Job Preferences    ${keyword}
        Search Jobs
        Open Latest Search Result
        Validate Keyword In Page Body    ${keyword}
        Close Browser
    END
    [Teardown]    

Global Search Validation
    FOR    ${keyword}    IN    @{search_terms}
        Navigate To EPAM
        Click Magnifier Glass
        Search For Posts Related To    ${keyword}
        Validate Keyword In Page Body    ${keyword}
        Close Browser
    END
    [Teardown]