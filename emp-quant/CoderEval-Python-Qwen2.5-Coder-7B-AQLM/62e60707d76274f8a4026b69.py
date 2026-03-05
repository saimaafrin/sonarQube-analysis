def point_type(name, fields, srid_map):
    """
    Dynamically Generating Point Class
    """
    class Point:
        def __init__(self, *args, **kwargs):
            for field in fields:
                setattr(self, field, kwargs.get(field, None))
            self.srid = kwargs.get('srid', None)

        def __repr__(self):
            return f"{name}({', '.join(f'{field}={getattr(self, field)}' for field in fields)})"

    return Point