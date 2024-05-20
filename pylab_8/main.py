import osmium
class PharmacyCounterHandler(osmium.SimpleHandler):
    def __init__(self):
        super().__init__()
        self.pharmacy_names = []
        self.kol_opening = 0

    def node(self, n):
        if 'amenity' in n.tags and n.tags['amenity'] == 'pharmacy':
            if 'name' in n.tags:
                self.pharmacy_names.append([n.id, n.tags['name']])
            else:
                self.pharmacy_names.append([n.id, ''])
            if "opening_hours" in n.tags and n.tags['opening_hours'] == '24/7':
                self.kol_opening += 1

    def way(self, w):
        if 'amenity' in w.tags and w.tags['amenity'] == 'pharmacy':
            if 'name' in w.tags:
                self.pharmacy_names.append([w.id, w.tags['name']])
            else:
                self.pharmacy_names.append([w.id, ''])
            if "opening_hours" in w.tags and w.tags['opening_hours'] == 'pharmacy':
                self.kol_opening += 1

    def relation(self, r):
        if 'amenity' in r.tags and r.tags['amenity'] == 'pharmacy':
            if 'name' in r.tags:
                self.pharmacy_names.append([r.id, r.tags['name']])
            else:
                self.pharmacy_names.append([r.id, ''])
            if "opening_hours" in r.tags and r.tags['opening_hours'] == 'pharmacy':
                self.kol_opening += 1


if __name__ == '__main__':
    osmfile = "9.osm"
    handler = PharmacyCounterHandler()
    handler.apply_file(osmfile)
    pharmacy_list = list(handler.pharmacy_names)
    kol = handler.kol_opening
    print("Список имен аптек 9.osm:")
    pharmacy_list.sort()
    for pharmacy in pharmacy_list:
        print(pharmacy)
    print('Кол-во аптек:', len(pharmacy_list))
    print('Кол-во круглосуточных аптек:', kol)
    print('\n')
    osmfile = "9-2.osm"
    handler = PharmacyCounterHandler()
    handler.apply_file(osmfile)
    pharmacy_list = list(handler.pharmacy_names)
    kol = handler.kol_opening
    print("Список имен аптек 9-2.osm:")
    pharmacy_list.sort()
    for pharmacy in pharmacy_list:
        print(pharmacy)
    print('Кол-во аптек:', len(pharmacy_list))
    print('Кол-во круглосуточных аптек:', kol)
