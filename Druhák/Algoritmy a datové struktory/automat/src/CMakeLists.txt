set(SOURCES FSM.c)

set(HEADERS "include/FSM.h")

set(LIBNAME "io_functions")

add_library(${LIBNAME} ${SOURCES} ${HEADERS})

target_include_directories(${LIBNAME} PUBLIC include)
