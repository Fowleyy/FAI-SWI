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

Ověření dostupnosti sekce „Ubytování v soukromí“
    Kontroluj  ${Button_Sluzby}  ${URL_Finish1}  ${Button_Ubyt1}  ${URL_Finish2}  ${Button_Ubyt2}  ${URL_Finish3}

Post-conditions
    Close Browser

