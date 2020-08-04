from conans import ConanFile, CMake, tools


class ConanRecipe(ConanFile):
    name = "ProtobufTest"
    version = "0.0.1"
    url = ""
    settings = "os", "compiler", "build_type", "arch"
    requires = "protobuf/3.11.4"

    generators = "cmake"
    scm = {
        "type": "git",
        "url": url,
        "revision": "auto"
    }

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    # def package(self):
    #     cmake = CMake(self)
    #     cmake.configure()
    #     cmake.install()
