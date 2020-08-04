# Simple protobuf conan example

This example is created to show how easy it is to create protobuf project with conan as package manager, shown for Linux only. 


## Dependencies

* Install `g++` and `build-essential` with Linux package manager.
* To be able to use `conan` see [installation guide](https://docs.conan.io/en/latest/installation.html).


## How to compile

Issue the following command to setup the project
```bash
$ conan install . -if build
```
which will install all conan packages in local package repository.

Then issue the following command to build the project
```bash
$ conan build . -bf build
```
The executable is located in `build/bin` directory on Linux.

