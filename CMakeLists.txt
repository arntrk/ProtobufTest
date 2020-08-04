cmake_minimum_required(VERSION 3.15)
project(ProtobufTest CXX)

set(CMAKE_EXPORT_COMPILE_COMMANDS On)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED On)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

# add the source files including .proto
add_executable(${PROJECT_NAME}
  Person.proto
  ProtobufTest.cpp
)

# use protobuf generate on project proto files
protobuf_generate(TARGET ${PROJECT_NAME})

# add needed dependecy
target_link_libraries(${PROJECT_NAME}
  PUBLIC CONAN_PKG::protobuf
)
 
# include for generated headers
target_include_directories(${PROJECT_NAME}
  PUBLIC ${CMAKE_CURRENT_BINARY_DIR}
)
