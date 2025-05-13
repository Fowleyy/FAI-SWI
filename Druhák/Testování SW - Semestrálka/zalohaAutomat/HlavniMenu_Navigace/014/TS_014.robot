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
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Ubytovani}

Ověření funkčnosti odkazu na sekci "Ubytování a služby"
    Zaloguj a Zkontroluj  ${Button_Ubytovani}  ${URL_Finish}

Post-conditions
    Close Browser

