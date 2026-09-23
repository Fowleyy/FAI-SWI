*** Keywords ***
Otevri Prohlizec Jdi na URL a Zkontroluj
    [Arguments]    ${Browser}    ${URL}    ${KontrolovanyElement}
    ${service}=    Evaluate    sys.modules['selenium.webdriver.chrome.service'].Service('C:/Users/Daniel/Desktop/testování/chromedriver.exe')    sys
    ${driver}=     Create WebDriver    Chrome    service=${service}
    Go To          ${URL}
    Maximize Browser Window
    Wait Until Element Is Visible    ${KontrolovanyElement}

Kontroluj
    [Arguments]  ${Button_Sys}  ${StrankaSys}  ${Button_Reg}  ${StrankaReg}
    ...  ${Input_email}  ${Input_heslo}  ${Input_hesloVerify}  ${Input_jmeno}
    ...  ${Input_prijmemi}  ${Input_tel}  ${Value_NevalidniEmail}  ${Value_Validniheslo}  ${Value_ValidnihesloVer}
    ...  ${Value_Validnijmeno}  ${Value_Validniprijmeni}  ${Value_ValidniTelefon}  ${Button_FinalReg}  ${SpatneUdaje}

    Element Should Be Visible  ${Button_Sys}

    ${OldWindows}=                 Get Window Handles
    Click Element                  ${Button_Sys}
    Wait Until Keyword Succeeds   10x    1s    Window Handle Should Change    ${OldWindows}

    ${AllWindows}=                 Get Window Handles
    ${NewWindow}=                  Get New Window Handle    ${OldWindows}    ${AllWindows}
    Switch Window                  ${NewWindow}

    Sleep  3s

    Location Should Contain        ${StrankaSys}

    Element Should Be Visible  ${Button_Reg}

    Click Element  ${Button_Reg}

    Sleep  2s

    Location Should Contain  ${StrankaReg}

    Element Should Be Visible  ${Input_email}
    Element Should Be Visible  ${Input_heslo}
    Element Should Be Visible  ${Input_hesloVerify}
    Element Should Be Visible  ${Input_jmeno}
    Element Should Be Visible  ${Input_prijmeni}
    Element Should Be Visible  ${Input_tel}

    Input Text  ${Input_email}  ${Value_NevalidniEmail}
    Input Text  ${Input_heslo}  ${Value_Validniheslo}
    Input Text  ${Input_hesloVerify}  ${Value_ValidnihesloVer}
    Input Text  ${Input_jmeno}  ${Value_Validnijmeno}
    Input Text  ${Input_prijmeni}  ${Value_Validniprijmeni}
    Input Text  ${Input_tel}  ${Value_ValidniTelefon}

    Element Should Be Visible  ${Button_FinalReg}

    Click Element  ${Button_FinalReg}

    Wait Until Element Is Visible  ${SpatneUdaje}


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



