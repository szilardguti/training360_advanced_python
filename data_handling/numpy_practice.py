# Készíts egy Python programot ami kiszámítja nagyon sok tétel áfa tartalmát.
# Oldd meg NumPy tömbök segítségével és egyetlen egy műveletben. (Tipp, generálj random nettó árakat a programodhoz)
# Áfa (Áru Forgalmi Adó), melynek kulcsa legyen 27%. Az Áfa tartalom meghatározására a képlet:
# netto_ar * afa_kulcs

import numpy as np

net_prices = np.random.rand(1, 100_000_0)
tax_perc = np.full((1, 100_000_0), 0.27)

tax_amount = net_prices * tax_perc

# Bonusz feladat: össze tudod kapcsolni egy numpy array-be a nettó ár és az áfa tartalom oszlopokat? (tipp np.column_stack)
stacked = np.vstack((net_prices, tax_amount))
print(stacked)

# Adott az alábbi 2D Numpy tömb:
# Használd a slicing operátort és válaszd ki a kék, zöld és piros Numpy rész tömböket.

base_matrix = np.arange(1, 31).reshape(-1, 5)
print(base_matrix)

blue_part = base_matrix[2:4, 0:2]
print(blue_part)

green_part = base_matrix[[0, 1, 2, 3], [1, 2, 3, 4]]
print(green_part)

red_part = base_matrix[[0, 4, 5], 3:]
print(red_part)
