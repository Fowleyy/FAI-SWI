*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Zaloguj a Zkontroluj
    [Arguments]  ${ButtonFoto}  ${StrankaFoto}  ${ButtonFoto2}  ${StrankaFoto2}  ${ButtonFoto3}  ${StrankaFoto3}  ${ButtonFoto4}  ${StrankaFoto4}

    Element Should Be Visible  ${ButtonFoto}

    Click Element  ${ButtonFoto}

    Location Should Contain  ${StrankaFoto}

    Element Should Be Visible  ${ButtonFoto2}

    Click Element  ${ButtonFoto2}

    Location Should Contain  ${StrankaFoto2}

    Element Should Be Visible  ${ButtonFoto3}

    Click Element  ${ButtonFoto3}

    Location Should Contain  ${StrankaFoto3}

    Element Should Be Visible  ${ButtonFoto4}

    Click Element  ${ButtonFoto4}

    Location Should Contain  ${StrankaFoto4}


