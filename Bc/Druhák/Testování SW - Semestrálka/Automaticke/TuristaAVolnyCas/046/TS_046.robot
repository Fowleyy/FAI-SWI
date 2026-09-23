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
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Turista}

Ověření dostupnosti sekce „Autovláček“
    Kontroluj  ${Button_Turista}  ${URL_Finish}  ${Button_Vlacek}  ${URL_Finish2}

Post-conditions
    Close Browser

