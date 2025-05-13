*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}



Kontroluj
    [Arguments]  ${ButtonSpolky}  ${StrankaSpolky}  ${ButtonSkaut}  ${StrankaSkaut}

    Element Should Be Visible  ${ButtonSpolky}

    Click Element  ${ButtonSpolky}

    Location Should Contain  ${StrankaSpolky}

    Element Should Be Visible  ${ButtonSkaut}

    Click Element  ${ButtonSkaut}

    Location Should Contain  ${StrankaSkaut}