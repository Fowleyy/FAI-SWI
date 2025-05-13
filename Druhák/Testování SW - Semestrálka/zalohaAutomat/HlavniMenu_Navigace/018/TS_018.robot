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
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Zprava}

Ověření funkčnosti odkazu na „Úřední desku“ z úvodní stránky
    Zaloguj a Zkontroluj  ${Button_Zprava}  ${URL_Finish1}  ${Button_PDF}  ${URL_Finish2}

Post-conditions
    Close Browser
