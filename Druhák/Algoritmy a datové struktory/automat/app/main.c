/**
 * @file       main.c
 * @author     Horak, Jurena
 * @date       2019.6
 * @brief      Main file for task11/PME-Notes_Remover.
 * ******************************************
 * @par       COPYRIGHT NOTICE (c) 2019 TBU in Zlin. All rights reserved.
 */

/*Private includes: ---------------------------------------------------------*/
#include <assert.h>

#include "FSM.h"

struct Config {
  FILE* input;
  FILE* output;
};

static struct Config* handleCommandLine(int argc, char** argv,
                                        struct Config* cfg);

int main(int argc, char* argv[]) {
  struct Config cfg;
  if (handleCommandLine(argc, argv, &cfg) == NULL) {
    return -1;
  }

  FSM_RemoveNotes(cfg.input, cfg.output);

  fclose(cfg.input);
  fclose(cfg.output);

  return 0;
}

static struct Config* handleCommandLine(int argc, char** argv,
                                        struct Config* cfg) {
  if (!cfg || !argv || argc < 1) {
    return NULL;
  }

  cfg->input = stdin;
  cfg->output = stdout;

  if (argc > 1) {
    cfg->input = fopen(argv[1], "r");
  }

  if (argc > 2) {
    cfg->output = fopen(argv[2], "w");
  }

  if (cfg->input == NULL || cfg->output == NULL) {
    return NULL;
  }

  return cfg;
}