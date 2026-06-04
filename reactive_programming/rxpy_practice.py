# Készíts Python alkalmazást, ami az RxPy modul használatával valósít meg egy egyszerű tőzsdei vevő jelző rendszert.
# Készíts ebből egy observable forrást. A forrás küldjön instrukciókat a feliratkozottaknak (observer függvény)
# de csak akkor ha a részvény árfolyam éppen 100 USD felett van.

import rx
import rx.operators as ops

stocks = [
    {"TCKR": "APPL", "PRICE": 200},
    {"TCKR": "GOOG", "PRICE": 90},
    {"TCKR": "TSLA", "PRICE": 120},
    {"TCKR": "MSFT", "PRICE": 150},
    {"TCKR": "INTL", "PRICE": 70},
]

observable = rx.from_iterable(stocks).pipe(
    ops.filter(lambda stock: stock.get("PRICE", 0) > 100)
)

# Az observer függvényed és így a programod is ilyen kimenetet kell adjon:

# Received Instruction to buy APPL
# Received Instruction to buy TSLA
# Received Instruction to buy MSFT

# All Buy Instructions have been received

observable.subscribe(
    on_next=lambda event: print(
        f"Received Instruction to buy {event.get('TCKR', 'uknown')}"
    )
)
observable.subscribe(
    on_completed=lambda: print("All Buy Instructions have been received")
)

observable.run()
