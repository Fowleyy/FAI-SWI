*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Kontroluj
    [Arguments]  ${ButtonSluzby}  ${StrankaSluzby}  ${ButtonUbyt1}  ${StrankaUbyt1}  ${ButtonUbyt2}  ${StrankaUbyt2}

    Element Should Be Visible  ${ButtonSluzby}

    Click Element  ${ButtonSluzby}

    Location Should Contain  ${StrankaSluzby}

    Element Should Be Visible  ${ButtonUbyt1}

    Click Element  ${ButtonUbyt1}

    Location Should Contain  ${StrankaUbyt1}

    Element Should Be Visible  ${ButtonUbyt2}

    Click Element  ${ButtonUbyt2}

    Location Should Contain  ${StrankaUbyt2}

