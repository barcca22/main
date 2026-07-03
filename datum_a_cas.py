from datetime import datetime, timedelta
print(datetime.now())
apollo_start = datetime(1969, 7, 16, 13, 32)
print(apollo_start.strftime("%m/%d/%Y"))

import humanize
solar_orbiter_start = datetime(2020, 2, 10, 5, 3)
solar_orbiter_start.weekday
print(solar_orbiter_start.strftime("%A"))
uplynulo = datetime.now() - solar_orbiter_start
print(uplynulo)
print(humanize.precisedelta(uplynulo))

objednavka = datetime(2024, 11, 13, 19, 47)
prevzeti = timedelta(minutes=30, seconds=35)
priprava = timedelta(minutes=30)
doprava = timedelta(minutes=25, seconds=30)
dodani = objednavka + prevzeti + priprava + doprava
print(dodani)