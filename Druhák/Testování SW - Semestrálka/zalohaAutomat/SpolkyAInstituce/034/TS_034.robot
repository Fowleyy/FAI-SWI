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

Ověření dostupnosti sekce „Kulturní komise“
    Zaloguj a Zkontroluj  ${Button_Spolky}  ${URL_Finish}  ${Button_Skaut}  ${URL_Finish2}

Post-conditions
    Close Browser

