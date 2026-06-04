# Készíts egy Python chat alkalmazást asyncio segítségével.
# Legyen külön egy kliens és egy sever modul.
# Tetszőleges üzenettel lehessen bontani a kapcsolatot.
# A chat üzeneteket a szerver és a kliens is a saját szemszögéből jelenítse meg.


import asyncio


async def serve(reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
    while True:
        try:
            req = await reader.readline()
        except ConnectionError:
            break

        print(f"Req: {req}")
        if req.rstrip(b"\n") == b"Marco!":
            writer.write(b"Polo!\n")
        elif req.rstrip(b"\n") == b"q":
            break
        else:
            writer.write(b"what?\n")

        await writer.drain()  # push the data out
    writer.close()
    await writer.wait_closed()


async def launch(host: str, port: int) -> None:
    server = await asyncio.start_server(serve, host, port)
    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:  # keep the server alive until cancelled
        await server.serve_forever()


if __name__ == "__main__":
    # `asyncio.run` handles loop creation/closure for us
    asyncio.run(launch("127.0.0.1", 8899))
