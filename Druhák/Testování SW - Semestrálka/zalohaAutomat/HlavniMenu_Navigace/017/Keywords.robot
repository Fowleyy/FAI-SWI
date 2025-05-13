*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Zaloguj a Zkontroluj
    [Arguments]  ${ButtonNovinka}  ${StrankaNovinka}  ${ButtonFoto}  ${StrankaFoto}

    Element Should Be Visible  ${ButtonNovinka}

    Click Element  ${ButtonNovinka}

    Location Should Contain  ${StrankaNovinka}

    Element Should Be Visible  ${ButtonFoto}

    Click Element  ${ButtonFoto}

    Location Should Contain  ${StrankaFoto}
