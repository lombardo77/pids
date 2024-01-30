import psutil
from termcolor import colored


def print_pids(filter="all"):
    p = psutil.pids()
    proc = None
    id_label = colored("pid", "yellow")
    id = ""

    status_label = colored("status", "yellow")
    status = ""

    name_label = colored("name", "yellow")
    name = ""

    users = colored("user", "yellow")
    user = ""

    percent_label = colored("MEM%", "yellow")
    percent = ""
    for i in p:
        proc = psutil.Process(i)
        percent = colored(str(proc.memory_percent())[:4], "green")

        if filter == "r" and proc.status() != "running":
            continue
        if filter == "s" and proc.status() != "sleeping":
            continue
        #set colors
        #cut the name length to ensure readability
        if len(proc.name()) > 7:
            name = colored(proc.name()[:6], "blue")
        else:
            name = colored(proc.name(), "blue")

        id = colored(str(i), "blue")
        if len(proc.username()) > 7:
            user = colored(proc.username()[:7], "green")
        else:
            user = colored(proc.username()[:7], "green")
        if proc.status() == "running":
            status = colored(proc.status(), "green")
        elif proc.status() == "sleeping":
            status = colored(proc.status(), "magenta")
        else:
            status = colored(proc.status(), "red")

        print(f"{id_label}: {id}   \t{status_label}: {status}   \t{name_label}: {name} \t {users}: {user} \t    {percent_label}: {percent} %")

print_pids()
while True:
    stream = input("enter command: ")
    if stream  == "kill":
        print("enter pid: ", end="")
        psutil.Process(int(input())).terminate()
        print_pids()
    elif stream == "r":
        print_pids("r")
    elif stream == "s":
        print_pids("s")
    elif stream == "a":
        print_pids()


