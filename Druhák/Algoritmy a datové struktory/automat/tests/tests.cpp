/*!
 * \file       tests.cpp
 * \author     Jurena
 * \date       7. 2. 2022
 * \brief      Unit tests for FSM module.
 * ******************************************
 * \attention
 * &copy; Copyright (c) 2022 FAI UTB. All rights reserved.
 *
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 */

/*Private includes: ---------------------------------------------------------*/
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>

#include "gtest/gtest.h"

extern "C" {
#include "FSM.h"
}

static const std::string cTestFiles = "test_files/";

class FSMFixture
    : public testing::TestWithParam<std::tuple<std::string, std::string>> {};

static std::string ReadFile(std::string fn) {
  std::ifstream in{fn};
  std::string output;

  if (in) {
    std::ostringstream ss;
    ss << in.rdbuf();
    output = ss.str();
    in.close();
  }

  return output;
}

TEST_P(FSMFixture, RemoveComments) {
  auto [inputName, expectedName] = GetParam();
  std::string outputName = cTestFiles + "output.c";
  FILE *inputFile = fopen(inputName.insert(0, cTestFiles).c_str(), "r");
  FILE *outputFile = fopen(outputName.c_str(), "w");

  std::string expectedFile = ReadFile(expectedName.insert(0, cTestFiles));

  // Run tested function and save processed file into output
  FSM_RemoveNotes(inputFile, outputFile);

  fclose(outputFile);
  fclose(inputFile);

  std::string output = ReadFile(outputName);

  // Compare output file with expectedOutput file
  ASSERT_EQ(expectedFile, output);
}

INSTANTIATE_TEST_SUITE_P(
    RemoveComments, FSMFixture,
    testing::Values(
        std::make_tuple("input_singleOneLiner.c", "output_singleOneLiner.c"),
        std::make_tuple("input_singleMultiline.c", "output_singleMultiline.c"),
        std::make_tuple("input_commentInString.c", "input_commentInString.c"),
        std::make_tuple("input_mclInString.c", "input_mclInString.c"),
        std::make_tuple("input_escapedQuote.c", "input_escapedQuote.c"),
        std::make_tuple("input_escapedApos.c", "input_escapedApos.c"),
        std::make_tuple("input_division.c", "input_division.c"),
        std::make_tuple("input_doxygen.c", "output_doxygen.c"),
        std::make_tuple("input_allTypes.c", "output_allTypes.c")));
