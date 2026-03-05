def validate(self, inventory, extract_spec_version=False):
    if extract_spec_version:
        if 'type' in inventory:
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

    # Additional validation logic for the inventory
    if 'items' not in inventory:
        raise ValueError("Inventory must contain 'items' key")
    if not isinstance(inventory['items'], list):
        raise ValueError("Items must be a list")

    for item in inventory['items']:
        if 'name' not in item or 'quantity' not in item:
            raise ValueError("Each item must have 'name' and 'quantity' keys")
        if not isinstance(item['quantity'], int) or item['quantity'] < 0:
            raise ValueError("Quantity must be a non-negative integer")