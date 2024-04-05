import asyncio
import os
import sys
from datetime import datetime
from hashlib import sha256, sha512, md5, sha3_224

from line_profiler import profile
from rich.console import Console

console = Console()
LOOP_PASSES = int(os.environ.get("LOOP_PASSES", 1_000))
try:
    FILENAME = os.environ["FILENAME"]
except KeyError:
    console.print("[bold red]Missed FILENAME env variable[/]")
    sys.exit(1)


@profile  # type: ignore
def hash_it(binary: bytes) -> str:
    hashed_256 = sha256(binary)
    sha512(binary)
    md5(binary)
    sha3_224(binary)
    return hashed_256.hexdigest()


@profile  # type: ignore
async def ahash_it(binary: bytes) -> str:
    hashed_256_coro = asyncio.to_thread(sha256, binary)
    hashed_512_coro = asyncio.to_thread(sha512, binary)
    hashed_md5_coro = asyncio.to_thread(md5, binary)
    hashed_sha3_coro = asyncio.to_thread(sha3_224, binary)

    hashes = await asyncio.gather(
        hashed_256_coro,
        hashed_512_coro,
        hashed_md5_coro,
        hashed_sha3_coro,
    )
    hashed = hashes[0].hexdigest()
    return hashed


def sync_main(binary: bytes) -> list[str]:
    console.print(f"[{datetime.utcnow()}] sync_main called")
    sync_hashes = []
    for i in range(LOOP_PASSES):
        sync_hashes.append(hash_it(binary))
    console.print(f"[{datetime.utcnow()}] sync_main finished")
    return sync_hashes


async def async_main(binary: bytes) -> list[str]:
    console.print(f"[{datetime.utcnow()}] async_main called")
    result = []
    tasks = []
    for i in range(LOOP_PASSES):
        tasks.append(asyncio.create_task(ahash_it(binary)))
        if len(tasks) == 8:
            result.extend([h for h in await asyncio.gather(*tasks)])
            tasks = []
    result.extend([h for h in await asyncio.gather(*tasks)])

    console.print(f"[{datetime.utcnow()}] async_main finished")
    return result


@profile  # type: ignore
def main() -> None:
    console.print(f"{LOOP_PASSES=}")
    console.print(f"{FILENAME=}")
    with open(FILENAME, "r") as file:
        book = file.readlines()
    binary = "".join(book).encode("utf8")
    sync_hashes = sync_main(binary)
    async_hashes = asyncio.run(async_main(binary))
    console.print(f"{sync_hashes[:2]= }")
    console.print(f"{async_hashes[:2]=}")
    try:
        assert sync_hashes == async_hashes
    except Exception:
        console.print_exception()
        sys.exit(1)


if __name__ == "__main__":
    main()
