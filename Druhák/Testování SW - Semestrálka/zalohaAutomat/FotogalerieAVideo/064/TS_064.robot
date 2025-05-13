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
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Foto}

Ověření funkčnosti zobrazení konkrétního videa
    Zaloguj a Zkontroluj  ${Button_Foto}  ${URL_Finish}  ${Button_Foto2}  ${URL_Finish2}  ${Button_Foto3}  ${URL_Finish3}

Post-conditions
    Close Browser

