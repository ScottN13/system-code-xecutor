import os
import sys
from configparser import ConfigParser
import platform
from termcolor import cprint, colored

ver = "1.0"

class scx:
    def about():
        print(f"scx-py version ",ver,)
        print(f"created by ValkTheBoxman")

    def WindowsGetInfo():
        print("Windows Version :",platform.version())
        print("Type of Windows Platform :",platform.win32_edition())
        print("Is Windows Ver IoT?: ",platform.win32_is_iot())

    def getOsInfo():
        print()
        cprint("## OS Info:", "black", "on_light_green")
        print(f"CPU Arhitecture: ",platform.machine())
        print(f"Device Network Name: ",platform.node())
        print(f"Device's Platform: ",platform.platform())
        print(f"CPU Name: ",platform.processor())
        print(f"Device Platform Version: ",platform.release())

        if sys.platform == "win32":
            print()
            cprint("# Windows Detected!", "yellow")
            scx.WindowsGetInfo()

        elif sys.platform == "darwin":
            print()
            cprint("# MacOS Detected!", "yellow")

        