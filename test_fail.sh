conan create ./build-tools
conan install --profile:build default_build . # also fails: conan install --profile:build default_build --profile:host default_host .
cmake .
