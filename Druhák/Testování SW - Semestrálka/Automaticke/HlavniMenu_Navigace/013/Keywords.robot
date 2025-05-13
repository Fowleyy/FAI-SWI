*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}

Kontroluj
    [Arguments]  ${ButtonTurista}  ${StrankaTurista}

    Element Should Be Visible  ${ButtonTurista}

    Click Element  ${ButtonTurista}

    Location Should Contain  ${StrankaTurista}


