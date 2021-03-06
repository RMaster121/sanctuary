from multiprocessing import Process

import click

import chatroom
import servchat


@click.command()
@click.option(
    "-s",
    "--servport",
    "servport",
    help="Set the port value for Chatroom [0-65536]",
    required=True,
)
@click.option(
    "-c",
    "--chatport",
    "chatport",
    help="Set the port value for WebSockets [0-65536]",
    required=True,
)
@click.option(
    "-6",
    "--ipprotv6",
    "netprotc",
    flag_value="ipprotv6",
    help="Start the server on an IPv6 address",
    required=True,
)
@click.option(
    "-4",
    "--ipprotv4",
    "netprotc",
    flag_value="ipprotv4",
    help="Start the server on an IPv4 address",
    required=True,
)
@click.version_option(
    version="22072020", prog_name="Sanctuary by AstroSonic"
)
def main(chatport, netprotc, servport):
    # Additional Thread
    server_thread = Process(target=chatroom.mainfunc, args=(chatport, netprotc))
    server_thread.start()

    # Main Thread
    servchat.mainfunc(servport, chatport, netprotc)

    server_thread.terminate()


if __name__ == "__main__":
    main()
