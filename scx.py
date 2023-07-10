import os
import sys
from configparser import ConfigParser
import platform
from rich.console import Console
import requests as req
from timeit import default_timer as timer
import subprocess

# Variables and misc.
console = Console()
config = ConfigParser(delimiters="=", comment_prefixes="#")
config.read("data/main.ini")
ver = str(config["MAIN"]["version"])
branch = str(config["MAIN"]["branch"])

class scx:
    
    def __init__(self):
        self.version = ver
        self.branch = branch
        self.os = sys.platform()
        self.nr = ...
        console.print(f"[bright_green]# SCX Succesful!","\n[bright_yellow]Welcome to system-code-xecutor!")

    def log(str):
        print("log started")
        with open(f"data/logs/log{scx.nr}", "a"):
            ...


    def about():
        print(f"scx-py version ",ver,branch,"\ncreated by @ScottN13")

    def WindowsGetInfo():
        print("Windows Version :",platform.version())
        print("Type of Windows Platform :",platform.win32_edition())
        print("Is Windows Ver IoT?: ",platform.win32_is_iot())

    def getOsInfo():
        start = timer()
        print()
        Console().print("[black on bright_green]## OS Info:")
        print("CPU Arhitecture: ",platform.machine())
        print("Device Network Name: ",platform.node())
        print("Device's Platform: ",platform.platform())
        print("CPU Name: ",platform.processor())
        print("Device Platform Version: ",platform.release())
        end = timer()
        Console().print(f"[black on bright_green]# Success! in {end-start}")

        if sys.platform == "win32":
            print()
            console.print("\n[bright_yellow]# Windows Detected!")
            scx.WindowsGetInfo()

        elif sys.platform == "darwin":
            print()
            console.print("[bright_yellow]# MacOS Detected!")

    def fetch(args): 
        start = timer()
        if args == ("ip"):
            url: str = "https://checkip.amazonaws.com"
            request = req.get(url)
            ip: str = request.text
            console.print("[bold][black on bright_yellow]IP:[/] ", ip)
            end = timer()
            Console().print(f"[black on bright_green]# Success! in {end-start}")

        elif args == ("file"):
            print("Please input path")
            path = input("fetch>file>")
            with open(path, "r") as file:
                print(file.readlines)

        elif args == ("webscrape"): ...

    def script(perm, path, type):
        if perm == "root":
            ...
        elif perm == "usr":
            ...

    def shell(): ...

    def command(cmd):
        start = timer()
        subprocess.run(cmd)
        end = timer()
        Console().print(f"[black on bright_green]# Task ended in {end - start}")       