class Point:
    def __init__(self, name, fields, srid_map):
        self.name = name
        self.fields = fields
        self.srid_map = srid_map

    def get_name(self):
        return self.name

    def get_fields(self):
        return self.fields

    def get_srid_map(self):
        return self.srid_map