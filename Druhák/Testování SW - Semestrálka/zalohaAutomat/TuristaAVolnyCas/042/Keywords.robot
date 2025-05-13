*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Zaloguj a Zkontroluj
    [Arguments]  ${ButtonTurista}  ${StrankaTurista}  ${ButtonDuha}  ${StrankaDuha}  ${ButtonCenik}  ${StrankaCenik}

    Element Should Be Visible  ${ButtonTurista}

    Click Element  ${ButtonTurista}

    Location Should Contain  ${StrankaTurista}

    Element Should Be Visible  ${ButtonDuha}

    Click Element  ${ButtonDuha}

    Location Should Contain  ${StrankaDuha}

    Element Should Be Visible  ${ButtonCenik}

    ${OldWindows}=                 Get Window Handles
    Click Element                  ${ButtonCenik}
    Wait Until Keyword Succeeds   10x    1s    Window Handle Should Change    ${OldWindows}

    ${AllWindows}=                 Get Window Handles
    ${NewWindow}=                  Get New Window Handle    ${OldWindows}    ${AllWindows}
    Switch Window                  ${NewWindow}

    Location Should Contain        ${StrankaCenik}

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