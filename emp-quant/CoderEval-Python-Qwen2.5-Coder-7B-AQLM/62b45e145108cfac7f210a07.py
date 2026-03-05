def validate(self, inventory, extract_spec_version=False):
    if extract_spec_version:
        if 'type' in inventory and inventory['type'] in ['v1', 'v2']:
            spec_version = inventory['type']
        else:
            spec_version = self.spec_version
    else:
        spec_version = self.spec_version

    # Add validation logic based on the spec_version
    if spec_version == 'v1':
        # Validation logic for version 1
        pass
    elif spec_version == 'v2':
        # Validation logic for version 2
        pass
    else:
        raise ValueError("Invalid specification version")

    # Additional validation logic
    if 'item' not in inventory or not isinstance(inventory['item'], str):
        raise ValueError("Invalid item value")

    if 'quantity' not in inventory or not isinstance(inventory['quantity'], int) or inventory['quantity'] < 0:
        raise ValueError("Invalid quantity value")

    # Return True if all validations pass
    return True