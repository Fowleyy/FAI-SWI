*** Settings ***
Library  SeleniumLibrary  run_on_failure=Nothing
Resource  Browsers.robot
Resource  URLs.robot
Resource  Buttons.robot
Resource  Values.robot
Resource  Inputs.robot
Resource  Keywords.robot

*** Test Cases ***
Pre-conditions
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Sys}

Ověření kontroly proti nezadání jména
    Zaloguj a Zkontroluj  ${Button_Sys}  ${URL_Sys}  ${Button_Reg}  ${URL_Reg}  ${Input_email}  ${Input_heslo}  ${Input_hesloVerify}  ${Input_jmeno}  ${Input_prijmeni}  ${Input_tel}  ${Value_NevalidniEmail}  ${Value_Validniheslo}  ${Value_ValidnihesloVer}  ${Value_Validnijmeno}  ${Value_Validniprijmeni}  ${Value_ValidniTelefon}  ${Button_FinalReg}  ${SpatneUdaje}

Post-conditions
    Close Browser

