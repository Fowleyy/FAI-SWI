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
    Otevri Prohlizec Jdi na URL a Zkontroluj  ${Browser_Chrome}  ${URL_MainPage}  ${Button_Novinka}

Ověření, že sekce „Aktuální zprávy“ na úvodní stránce zobrazuje nejnovější informace
    Kontroluj  ${Button_Novinka}  ${URL_Finish1}  ${Button_Foto}  ${URL_Finish2}

Post-conditions
    Close Browser

