*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}


Kontroluj
    [Arguments]  ${ButtonSpolky}  ${StrankaSpolky}  ${ButtonFara}  ${StrankaFara}  ${ButtonWeb}  ${StrankaWeb}

    Element Should Be Visible  ${ButtonSpolky}

    Click Element  ${ButtonSpolky}

    Location Should Contain  ${StrankaSpolky}

    Element Should Be Visible  ${ButtonFara}

    Click Element  ${ButtonFara}

    Location Should Contain  ${StrankaFara}

    Element Should Be Visible  ${ButtonWeb}

    ${OldWindows}=                 Get Window Handles
    Click Element                  ${ButtonWeb}
    Wait Until Keyword Succeeds   10x    1s    Window Handle Should Change    ${OldWindows}

    ${AllWindows}=                 Get Window Handles
    ${NewWindow}=                  Get New Window Handle    ${OldWindows}    ${AllWindows}
    Switch Window                  ${NewWindow}

    Location Should Contain        ${StrankaWeb}

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
