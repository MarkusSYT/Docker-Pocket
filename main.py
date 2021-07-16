import typer
import os

logo = """
 _____             _             _____           _        _  
|  __ \\           | |           |  __ \\         | |      | |  
| |  | | ___   ___| | _____ _ __| |__) |__   ___| | _____| |_ 
| |  | |/ _ \\ / __| |/ / _ \\ '__|  ___/ _ \\ / __| |/ / _ \\ __|
| |__| | (_) | (__|   <  __/ |  | |  | (_) | (__|   <  __/ |_ 
|_____/ \\___/ \\___|_|\\_\\___|_|  |_|   \\___/ \\___|_|\\_\\___|\\__|"""

choices: str = """
1.      list local images
2.      list local containers
3.      list running containers
4.      download image
5.      remove image
6.      remove container
7.      container shell
8.      create container
9.      start container
10.     stop container
11.     quit
"""


def main():
    typer.echo(typer.style(logo, fg=typer.colors.BLUE))
    typer.echo(typer.style("         by MarkusS (https://github.com/MarkusSYT)", fg=typer.colors.GREEN))
    typer.echo(typer.style("         by Tert0   (https://github.com/Tert0)", fg=typer.colors.GREEN))
    typer.echo(typer.style(choices, fg=typer.colors.CYAN))
    choice = typer.prompt(">", prompt_suffix=" ")
    command = ""
    if choice == "1":
        command = "docker images"
    elif choice == "2":
        command = "docker ps -a"
    elif choice == "3":
        command = "docker ps"
    elif choice == "4":
        image = typer.prompt("Whats the image name?")
        command = f"docker pull {image}"
    elif choice == "5":
        image = typer.prompt("Whats the image name?")
        command = f"docker rmi {image}"
    elif choice == "6":
        container = typer.prompt("Whats the container name?")
        command = f"docker rm {container}"
    elif choice == "7":
        container = typer.prompt("Whats the container name?")
        shell = typer.prompt("What Shell do you want to use?", default="/bin/bash")
        command = f"docker exec -it {container} {shell}"
    elif choice == "8":
        image = typer.prompt("Whats the image name?")
        container = typer.prompt("Whats the container name?")
        typer.echo("How to expose Ports: HOST_PORT_1:CONTAINER_PORT_1;HOST_PORT_2:CONTAINER_PORT_2")
        ports = typer.prompt("Expose Ports").split(";")
        ports_str = ""
        if len(ports) > 0:
            ports_str = f"-p {' -p '.join(ports)}"
        command = f"docker run -d {ports_str} --name {container} {image}"
    elif choice == "9":
        container = typer.prompt("Whats the container name?")
        command = f"docker start {container}"
    elif choice == "10":
        container = typer.prompt("Whats the container name?")
        command = f"docker stop {container}"
    elif choice == "11":
        return 0
    if command != "":
        typer.echo(typer.style(f"Executing command '{command}'", fg=typer.colors.BRIGHT_GREEN))
        os.system(command)

    else:
        typer.echo(typer.style(f"The Choice '{choice}' is not supported", fg=typer.colors.RED))
    if typer.confirm(typer.style("Do you want to continue?", fg=typer.colors.BRIGHT_RED), prompt_suffix="",
                     default=True):
        main()


if __name__ == "__main__":
    typer.run(main)
