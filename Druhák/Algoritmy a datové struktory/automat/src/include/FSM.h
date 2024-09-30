/*!
 * \file       FSM.h
 * \author     Horak, Jurena
 * \date       2019.6
 * \brief      Header file defining functions for functions.c file
 * ******************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

#ifndef _FSM_H_
#define _FSM_H_
/*! \defgroup FSM Finite State Machine
 *  \brief    Module that implements the Mealy machine to remove the comments
 * from the C sources
 *  \{
 */
/*Private includes: ---------------------------------------------------------*/
#include <stdio.h>

/*Private defines: ----------------------------------------------------------*/
/*!
 * \brief Mealys state machine - reads input per single character and transition
 * to the new state based on the value of the character. Using this approach it
 * removes comments in the C sources.
 *
 * \param[in] input   Pointer to input stream. The stream shall be opened for
 * reading.
 * \param[in,out] output  Pointer to the output stream. It is expected that
 * the file is opened for writting.
 */
void FSM_RemoveNotes(FILE* input, FILE* output);

/*! \} */
#endif
