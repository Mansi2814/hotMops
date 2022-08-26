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

tollFree = {"Andhra Pradesh": ['1800-180-5678'],
            "Assam": ['0361-2232532'],
            "Bihar": ['1800 345 6284'],
            "Chhattisgarh": ['1800-233-0008'],
            "Goa": ['08322420069', '08322420070'],
            "Gujarat": ['079-23229162', '079-23225624', '079-23222547'],
            "Haryana": ['1800-180-5678'],
            "Himachal Pradesh": ['1800-180-8009'],
            "Jammu and Kashmir": ['1800-180-5678'],
            "Jharkhand": ['1800-3456-502'],
            "Karnataka": ['1916'],
            "Kerala": ['1916'],
            "Madhya Pradesh": ['14420'],
            "Maharashtra": ['022-22025354', '22835247'],
            "Manipur": ['+91-385241168'],
            "Mizoram": ['(0389)-2322244'],
            "Odisha": ['+91-674-2571341', '2571185'],
            "Punjab": ['14420'],
            "Sikkim": ['1800-345-3286'],
            "Telangana": ['040-23225397'],
            "Uttarakhand": ['18001804100'],
            "Uttar Pradesh": ['1800-313-0522 '],
            "West Bengal": ['033-2324-2137'],
            "Chandigarh": ['0172-278720'],
            "Delhi": ['1916,1800117118'],
            "Puducherry": ['1031']
            }
