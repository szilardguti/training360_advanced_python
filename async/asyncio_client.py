# Készíts egy Python chat alkalmazást asyncio segítségével.
# Legyen külön egy kliens és egy sever modul.
# Tetszőleges üzenettel lehessen bontani a kapcsolatot.
# A chat üzeneteket a szerver és a kliens is a saját szemszögéből jelenítse meg.


import asyncio


async def client(host: str, port: int):
    reader, writer = await asyncio.open_connection(host, port)

    async def send(msg: str):
        print(f"Client: {msg}")
        writer.write((msg + "\n").encode())
        await writer.drain()
        resp = await reader.readline()
        print("Server:", resp.decode().rstrip())

    await send("Marco!")
    await send("Hello")
    await send("q")  # tell server to close
    writer.close()
    await writer.wait_closed()


if __name__ == "__main__":
    asyncio.run(client("127.0.0.1", 8899))
