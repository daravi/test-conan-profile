cmake_minimum_required(VERSION 3.12)

project(test-profiles)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

message("CONAN_BUILD-TOOLS_ROOT: '${CONAN_BUILD-TOOLS_ROOT}'")

