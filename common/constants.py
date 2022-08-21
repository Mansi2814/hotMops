from indian_cities.dj_city import cities
states = []
for i in cities:
    states.append((i[0], i[0]))
STATE_CHOICES = states
STATE_CITY = {}
ALL_CITIES = []
for state in cities:
    selected_city = {}
    for i in state[1]:
        ALL_CITIES.append(i)
        selected_city[i[0]] = i[1]
    STATE_CITY[state[0]] = selected_city
# print(STATE_CITY)
PRIVATE = "pvt"
PUBLIC = "public"
ACCESS_CHOICES = [(PRIVATE, "Private"), (PUBLIC, "Public")]