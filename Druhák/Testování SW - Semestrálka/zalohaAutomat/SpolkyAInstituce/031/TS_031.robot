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

Ověření dostupnosti sekce „Místní knihovna“
    Zaloguj a Zkontroluj  ${Button_Spolky}  ${URL_Finish}  ${Button_Knihovna}  ${URL_Finish2}  ${Button_Katalog}  ${URL_Finish3}

Post-conditions
    Close Browser

