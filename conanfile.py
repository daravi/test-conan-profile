from conans import ConanFile, CMake, tools


class TestprofilesConan(ConanFile):
    name = "test-profiles"
    version = "1.0.0"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Testprofiles here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = "cmake"

    def build_requirements(self):
        self.build_requires("build-tools/1.0.0")
