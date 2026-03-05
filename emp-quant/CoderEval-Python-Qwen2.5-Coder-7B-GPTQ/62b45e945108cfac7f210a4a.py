def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
    """
    Validate storage root hierarchy.

Returns:
    num_objects - number of objects checked
    good_objects - number of objects checked that were found to be valid
    """
    num_objects = 0
    good_objects = 0

    for obj in self.storage_root.iterate():
        num_objects += 1
        if validate_objects and not obj.validate():
            if show_warnings:
                print(f"Warning: Object {obj.id} is invalid.")
        elif check_digests and not obj.check_digest():
            if show_warnings:
                print(f"Warning: Digest mismatch for object {obj.id}.")
        else:
            good_objects += 1

    return num_objects, good_objects