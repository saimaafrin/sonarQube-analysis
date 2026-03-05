def validate(self, inventory, extract_spec_version=False):
    if extract_spec_version:
        spec_version = inventory.get('type')
        if not spec_version or spec_version not in ['v1', 'v2']:
            spec_version = self.spec_version
    else:
        spec_version = self.spec_version

    # Add validation logic based on the spec_version
    if spec_version == 'v1':
        # Validation for version v1
        pass
    elif spec_version == 'v2':
        # Validation for version v2
        pass
    else:
        raise ValueError("Invalid specification version")

    return True