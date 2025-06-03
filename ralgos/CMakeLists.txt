cmake_minimum_required(VERSION 3.14)
project(ralgos)

find_package(pybind11 REQUIRED)

# Create the module from source
pybind11_add_module(ralgos_cpp src/kwise.cpp src/bindings.cpp)

# 🔧 Tell CMake to put the output shared object (.so) into the ralgos/ folder
set_target_properties(ralgos_cpp PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/ralgos
)

