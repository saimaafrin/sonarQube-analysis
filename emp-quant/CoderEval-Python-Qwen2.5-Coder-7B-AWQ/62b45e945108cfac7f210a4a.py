import os

class StorageRoot:
    def __init__(self, path):
        self.path = path

    def validate_hierarchy(self, validate_objects=True, check_digests=True, show_warnings=False):
        """
        Validate storage root hierarchy.

        Returns:
            num_objects - number of objects checked
            good_objects - number of objects checked that were found to be valid
        """
        num_objects = 0
        good_objects = 0

        for root, _, files in os.walk(self.path):
            for file in files:
                num_objects += 1
                if validate_objects:
                    # Simulate object validation
                    if self._is_valid_object(os.path.join(root, file)):
                        good_objects += 1
                    elif show_warnings:
                        print(f"Warning: Invalid object {os.path.join(root, file)}")
                if check_digests:
                    # Simulate digest check
                    if not self._check_digest(os.path.join(root, file)):
                        if show_warnings:
                            print(f"Warning: Digest mismatch for {os.path.join(root, file)}")

        return num_objects, good_objects

    def _is_valid_object(self, path):
        # Placeholder for actual object validation logic
        return True

    def _check_digest(self, path):
        # Placeholder for actual digest check logic
        return True