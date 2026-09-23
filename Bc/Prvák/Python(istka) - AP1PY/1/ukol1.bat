@ECHO OFF
CLS
REM Vyčištění obrazovky a zablokování vypisování samotných příkazů


REM Pozdravení uživatele a vypsání aktuálního času
ECHO Vitej v mem programu uzivateli

timeout /t 2 >nul
ECHO.

ECHO Aktualni cas je: %TIME%

timeout /t 2 >nul
ECHO.

REM Vytvoření složky MujProgram
ECHO Vytvarim slozku: MujProgram
MKDIR MujProgram

timeout /t 2 >nul
ECHO.

REM Vytvoření složky MujProgram/src
ECHO Vytvarim slozku: MujProgram/src
MKDIR MujProgram\src

timeout /t 2 >nul
ECHO.

REM Vytvoření složky MujProgram/info
ECHO Vytvarim slozku: MujProgram/info
MKDIR MujProgram\info

timeout /t 2 >nul
ECHO.

REM Kontrola, zda byl skript spuštěn s parametrem
IF "%1"=="" (
  REM Pokud nebyl parametr zadán, zeptej se uživatele na jméno složky
  SET /P folder_name="Zadej nazev slozky pro vytvoreni: "
) ELSE (
  REM Pokud byl parametr zadán, použijte jej jako jméno složky
  SET "folder_name=%1"
)


REM Vytvoření složky s zadaným názvem a kontrola úspěšnosti
MKDIR "MujProgram\%folder_name%"
IF ERRORLEVEL 1 (
  ECHO Vytvoření slozky selhalo.
) ELSE (
  ECHO Slozka "%folder_name%" byla uspesne vytvorena.
)

timeout /t 2 >nul
ECHO.

REM Test spojeni se serverem utb.cz a uložení výstupu
ECHO Testuju spojeni se serverem utb.cz
PING utb.cz > "MujProgram\info\ping.log"
ECHO Ukladam log do: MujProgram\info\ping.log

timeout /t 2 >nul
ECHO.

REM Vytvoření souboru s adresářovou strukturou
ECHO Zapisuju adresarovou strukturu adresare MujProgram
DIR /S /B "MujProgram" > "MujProgram\info\dir.log"
ECHO Soubor ulozen do slozky MujProgram\info\dir.log

timeout /t 2 >nul
ECHO.

REM Ukončení skriptu s nulovým kódem
ECHO Ukoncuju program

timeout /t 2 >nul

EXIT /B 0