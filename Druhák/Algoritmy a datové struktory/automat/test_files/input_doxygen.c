/*!
 * \file main.c
 *\brief This is a test file for Mealy machine removing comments
 */

#include <stdio.h>

/*!
 * \brief Doxygen comment
 */
int main( int argc, char **argv )
{
    /*! Local text variable */
	const char* text = "This is a /* comment */ inside 'text'";

    /*! Local text variable 2 */
	const char* text2 = "This is a // comment inside text";

	return 0;
}
