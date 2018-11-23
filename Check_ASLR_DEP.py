#Check ASLR and DEP is enabled or not.

import argparse
import os
import pefile


class DllCharacteristics():
    def __init__(self):
        self.IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE = False
        self.IMAGE_DLLCHARACTERISTICS_WDM_DRIVER = False
        self.IMAGE_DLLCHARACTERISTICS_NO_BIND = False
        self.IMAGE_DLLCHARACTERISTICS_NO_SEH = False
        self.IMAGE_DLLCHARACTERISTICS_NO_ISOLATION = False
        self.IMAGE_DLLCHARACTERISTICS_NX_COMPAT = False
        self.IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY = False
        self.IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE = False


def get_dll_characteristics(path):
    foo = DllCharacteristics()

    pe = pefile.PE(path, fast_load=True)
    dll_characteristics = pe.OPTIONAL_HEADER.DllCharacteristics

    if dll_characteristics > 0:
        if dll_characteristics >= 32768:
            foo.IMAGE_DLLCHARACTERISTICS_TERMINAL_SERVER_AWARE = True
            dll_characteristics -= 32768

        if dll_characteristics >= 8192:
            foo.IMAGE_DLLCHARACTERISTICS_WDM_DRIVER = True
            dll_characteristics -= 8192

        if dll_characteristics == 2048 or dll_characteristics > 2080:
            foo.IMAGE_DLLCHARACTERISTICS_NO_BIND = True
            dll_characteristics -= 2048

        if dll_characteristics == 1024 or dll_characteristics > 1056:
            foo.IMAGE_DLLCHARACTERISTICS_NO_SEH = True
            dll_characteristics -= 1024

        if dll_characteristics == 512 or dll_characteristics > 544:
            foo.IMAGE_DLLCHARACTERISTICS_NO_ISOLATION = True
            dll_characteristics -= 512

        if dll_characteristics == 256 or dll_characteristics > 288:
            foo.IMAGE_DLLCHARACTERISTICS_NX_COMPAT = True
            dll_characteristics -= 256

        if dll_characteristics >= 128:
            foo.IMAGE_DLLCHARACTERISTICS_FORCE_INTEGRITY = True
            dll_characteristics -= 128

        if dll_characteristics == 64:
            foo.IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE = True
            dll_characteristics -= 64

    return foo


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='Directory to scan')
    args = parser.parse_args()

    dep_enabled = []
    dep_disabled = []

    aslr_enabled = []
    aslr_disabled = []

    for root, dirs, files in os.walk(args.dir):
        for f in files:
            bar = get_dll_characteristics(os.path.join("/home/manish/Music/BasicPython/CodeCraft/setup.exe","")

            if bar.IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE:
                aslr_enabled.append(f)
            else:
                aslr_disabled.append(f)

            if bar.IMAGE_DLLCHARACTERISTICS_NX_COMPAT:
                dep_enabled.append(f)
            else:
                dep_disabled.append(f)

    print("ASLR Enabled: ")
    print("==============")
    for i in aslr_enabled:
        print(i)
    print("")

    print("ASLR Disabled: ")
    print("===============")
    for i in aslr_disabled:
        print(i)
    print("")

    print("DEP Enabled: ")
    print("=============")
    for i in dep_enabled:
        print(i)
    print("")

    print("DEP Disabled: ")
    print("==============")
    for i in dep_disabled:
        print(i)
    print("")
