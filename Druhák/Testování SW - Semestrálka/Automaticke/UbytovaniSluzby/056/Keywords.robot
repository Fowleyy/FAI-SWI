*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Kontroluj
    [Arguments]  ${ButtonSluzby}  ${StrankaSluzby}  ${ButtonRest1}  ${StrankaRest1}  ${ButtonRest2}  ${StrankaRest2}  ${ButtonRest3}  ${StrankaRest3}

    Element Should Be Visible  ${ButtonSluzby}

    Click Element  ${ButtonSluzby}

    Location Should Contain  ${StrankaSluzby}

    Element Should Be Visible  ${ButtonRest1}

    Click Element  ${ButtonRest1}

    Location Should Contain  ${StrankaRest1}

    Element Should Be Visible  ${ButtonRest2}

    Click Element  ${ButtonRest2}

    Location Should Contain  ${StrankaRest2}

    Element Should Be Visible  ${ButtonRest3}

    ${OldWindows}=                 Get Window Handles
    Click Element                  ${ButtonRest3}
    Wait Until Keyword Succeeds   10x    1s    Window Handle Should Change    ${OldWindows}

    ${AllWindows}=                 Get Window Handles
    ${NewWindow}=                  Get New Window Handle    ${OldWindows}    ${AllWindows}
    Switch Window                  ${NewWindow}

    Location Should Contain        ${StrankaRest3}

    Close Browser    # ← zavře celé okno prohlížeče po dokončení

Window Handle Should Change
    [Arguments]  ${OldWindows}
    ${CurrentWindows}=    Get Window Handles
    ${old_len}=           Get Length    ${OldWindows}
    ${new_len}=           Get Length    ${CurrentWindows}
    Should Be True        ${new_len} > ${old_len}

Get New Window Handle
    [Arguments]  ${OldHandles}  ${NewHandles}
    FOR    ${handle}    IN    @{NewHandles}
        Run Keyword If    '${handle}' not in ${OldHandles}    Return From Keyword    ${handle}
    END