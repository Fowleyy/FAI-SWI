*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Zaloguj a Zkontroluj
    [Arguments]  ${ButtonSluzby}  ${StrankaSluzby}  ${ButtonHotely}  ${StrankaHotely}  ${ButtonHotel}  ${StrankaHotel}

    Element Should Be Visible  ${ButtonSluzby}

    Click Element  ${ButtonSluzby}

    Location Should Contain  ${StrankaSluzby}

    Element Should Be Visible  ${ButtonHotely}

    Click Element  ${ButtonHotely}

    Location Should Contain  ${StrankaHotely}

    Element Should Be Visible  ${ButtonHotel}

    Click Element  ${ButtonHotel}

    Location Should Contain  ${StrankaHotel}

