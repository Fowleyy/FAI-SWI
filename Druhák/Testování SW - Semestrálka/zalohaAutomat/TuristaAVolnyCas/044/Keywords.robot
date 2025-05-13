*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Zaloguj a Zkontroluj
    [Arguments]  ${ButtonTurista}  ${StrankaTurista}  ${ButtonTipy}  ${StrankaTipy}

    Element Should Be Visible  ${ButtonTurista}

    Click Element  ${ButtonTurista}

    Location Should Contain  ${StrankaTurista}

    Element Should Be Visible  ${ButtonTipy}

    Click Element  ${ButtonTipy}

    Location Should Contain  ${StrankaTipy}

