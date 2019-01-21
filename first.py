# Credit: Daw-St

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
from matplotlib.ticker import ScalarFormatter

n_groups = 16

transakcje = (5118367761, 1119358927, 1105527604, 699416868, 1381418977, 4251634084, 12792490030, 433587433, 478948346, 837135117, 4509834595, 1908237968, 364407537, 999181049, 3047271481, 1829763532)

naklady = (15260504000, 5318139000, 3832779000, 3617002000, 9221590000, 10668705000, 3403627000, 6509559000, 5531315000, 2515834000, 8560815000, 19968869000, 2037214000, 2980042000, 14906350000 , 4121804000)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = ax.bar(index, transakcje, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label='Suma transakcji na rynku mieszkan')

rects2 = ax.bar(index + bar_width, naklady, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='Nakady finansowe na inwestycje przedsiębiorstw')

ax.set_xlabel('Województwa')
ax.set_ylabel('Nakady finansowe w PLN')
ax.set_title('Wykres kolumnowy stosunku dwóch danych - Dawid Strytyski')
ax.set_xticks(index + bar_width / 2)
plt.yticks(np.arange(100000, 24999999999, 1000000000))
ax.set_xticklabels(('DOL', 'KUJ-POM', 'LUBEL', 'LUBU', 'LODZ', 'MALOP', 'MAZ', 'OP', 'PODKA', 'PODL', 'POMOR', 'SL', 'SWIET', 'WAR-MAZ', 'WLKP', 'ZACHPOM'))
ax.legend()

fig.tight_layout()
plt.show()