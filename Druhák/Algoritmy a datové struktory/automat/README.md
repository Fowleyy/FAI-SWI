#  Zpracování textů - konečný automat
Naprogramujte **konečný Mealyho automat**, který ze vstupního souboru v jazyce C/C++ odstraní poznámky (tzn. vše mezi znaky `/* */` nebo `// \n`).

## Příklad vstupního souboru a odpovídající výstup

### Vstup
```c
/* This is a test file for Mealy machine removing comments */

#include <stdio.h>

/*! 
 * \brief Doxygen comment
 */
int main( int argc, char **argv )
{
	// One-line comment
	
	const char* text = "This is a /* comment */ inside 'text'";
	const char* text2 = "This is a // comment inside text"; // comment after text
	const char* text3 = "This is a \" inside text with odd number ' "; /* multiline comment
	after text */
	
	char ch = '"';
	char ch2 = '\''; // comment after character
	char ch3 = '\\'; /* multi-line comment
	after character */
	
	double val = 10 / 2;
	
	return 0;
}
```

### Výstup

```c


#include <stdio.h>


int main( int argc, char **argv )
{
	
	
	const char* text = "This is a /* comment */ inside 'text'";
	const char* text2 = "This is a // comment inside text"; 
	const char* text3 = "This is a \" inside text with odd number ' "; 
	
	char ch = '"';
	char ch2 = '\''; 
	char ch3 = '\\'; 
	
	double val = 10 / 2;
	
	return 0;
}

```

## Spuštění programu

Program může být spuštěn s variabilním počtem argumentů. Obecné volání vypadá následovně: `./FSM_CommentRemover [input.c] [output.c]`

V předchozím příkladu jsou oba argumenty nepovinné a pokud nejsou uvedeny, tak je použit standardní vstup a výstup (stdin a stdout). Pokud je uveden pouze jeden argument, bude použit jako vstupní soubor, ve kterém budou poznámky odstraněny, a výstup bude zapsán na standardní výstup. Jestliže budou zadány argumenty dva, tak je druhý z nich použit jako výstupní soubor, kam je zapsán zpracovaný soubor. Pokud je argumentů více než dva, tak je zbytek ignorován.

## Návratová hodnota

Program vrací na svém výstupu hodnotu **0** pokud nedojde k chybě, hodnotu **-1** při detekci chyby.

## Testovací soubory

V adresáři **test_files** najdete sadu vstupních souborů a jejich výstupů.

---
#  Text processing - finite machine
Program **finite Mealy machine**, which removes the notes (i.e. everything between `/* */` or `// \n`) from the C / C++ input file.

## Example of input and coresponding output 

See [czech version](#příklad-vstupního-souboru-a-odpovídající-výstup)

## Running the program

The program can be run with a variable number of arguments. A general call looks like this: `./FSM_CommentRemover [input.c] [output.c]`

In the previous example, both arguments are optional, and if they are not specified, the standard input and output (stdin and stdout) are used. If only one argument is given, it will be used as the input file in which the notes will be removed, and the output will be written to standard output. If two arguments are given, the second one is used as the output file where the processed file is written. If there are more than two arguments, the rest are ignored.

## Exit status

The program returns **0** on its output if no error occurs, **-1** if an error is detected.

## Test files

In the **test_files** directory you will find a set of input files and their outputs.
