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
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Spolky}

Ověření funkčnosti odkazu na sekci "Spolky a instituce"
    Kontroluj  ${Button_Spolky}  ${URL_Finish}

Post-conditions
    Close Browser

