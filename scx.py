import os
import sys
from configparser import ConfigParser
import platform
from rich.console import Console
import requests as req

console = Console()
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
        Console().print("[black on bright_green]## OS Info:")
        print(f"CPU Arhitecture: ",platform.machine())
        print(f"Device Network Name: ",platform.node())
        print(f"Device's Platform: ",platform.platform())
        print(f"CPU Name: ",platform.processor())
        print(f"Device Platform Version: ",platform.release())

        if sys.platform == "win32":
            print()
            console.print("[bright_yellow]# Windows Detected!")
            scx.WindowsGetInfo()

        elif sys.platform == "darwin":
            print()
            console.print("[bright_yellow]# MacOS Detected!")

    def fetch(args): 
        if args == ("ip"):
            url: str = "https://checkip.amazonaws.com"
            request = req.get(url)
            ip: str = request.text
            console.print("[bold][black on bright_yellow]IP:[/] ", ip)

        elif args == ("file"):
            print("Please input path")
            path = input("fetch>file>")
            with open(path, "r") as file:
                print(file.readlines)

        elif args == (""): ...

        