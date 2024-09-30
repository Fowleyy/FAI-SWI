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
