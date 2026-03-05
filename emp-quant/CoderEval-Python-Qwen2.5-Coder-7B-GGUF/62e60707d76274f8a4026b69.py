def point_type(name, fields, srid_map):
    """
    Dynamically Generating Point Class
    """
    class Point:
        def __init__(self, *args, **kwargs):
            for field in fields:
                if field in kwargs:
                    setattr(self, field, kwargs[field])
                else:
                    setattr(self, field, None)
            if 'srid' in kwargs:
                self.srid = kwargs['srid']
            else:
                self.srid = None

        def __repr__(self):
            return f"{name}({', '.join(f'{field}={getattr(self, field)}' for field in fields if getattr(self, field) is not None)})"

    return Point