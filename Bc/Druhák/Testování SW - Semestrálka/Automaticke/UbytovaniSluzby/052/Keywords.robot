*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Kontroluj
    [Arguments]  ${ButtonSluzby}  ${StrankaSluzby}  ${ButtonPenziony}  ${StrankaPenziony}  ${ButtonPenzion}  ${StrankaPenzion}

    Element Should Be Visible  ${ButtonSluzby}

    Click Element  ${ButtonSluzby}

    Location Should Contain  ${StrankaSluzby}

    Element Should Be Visible  ${ButtonPenziony}

    Click Element  ${ButtonPenziony}

    Location Should Contain  ${StrankaPenziony}

    Element Should Be Visible  ${ButtonPenzion}

    Click Element  ${ButtonPenzion}

    Location Should Contain  ${StrankaPenzion}

