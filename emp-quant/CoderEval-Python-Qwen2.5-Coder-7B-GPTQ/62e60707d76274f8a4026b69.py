class Point:
    def __init__(self, name, fields, srid_map):
        self.name = name
        self.fields = fields
        self.srid_map = srid_map

    def get_srid(self):
        return self.srid_map.get(self.name, None)