cmake_minimum_required(VERSION 3.14)
project(ralgos)

find_package(pybind11 REQUIRED)

set(SOURCES
    src/generators/kuniform.cpp
    src/generators/uuniform.cpp
    src/generators/normal.cpp
    src/generators/uniform.cpp
    src/generators/bernoulli.cpp
    src/generators/kbernoulli.cpp
    src/generators/margulis.cpp

    src/expanders/margulis.cpp

    src/bindings.cpp
)

# Create the module from source
pybind11_add_module(ralgos_cpp ${SOURCES})

# put the output shared object (.so) into the ralgos/ 
set_target_properties(ralgos_cpp PROPERTIES
    LIBRARY_OUTPUT_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/ralgos
)

