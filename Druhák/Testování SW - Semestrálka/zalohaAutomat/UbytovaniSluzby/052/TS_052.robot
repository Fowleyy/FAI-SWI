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
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Sluzby}

Ověření dostupnosti sekce „Penziony a chaty“
    Zaloguj a Zkontroluj  ${Button_Sluzby}  ${URL_Finish1}  ${Button_Penziony}  ${URL_Finish2}  ${Button_Penzion}  ${URL_Finish3}

Post-conditions
    Close Browser

