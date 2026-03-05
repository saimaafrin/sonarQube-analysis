import re

class InventoryValidator:
    def __init__(self, spec_version):
        self.spec_version = spec_version

    def validate(self, inventory, extract_spec_version=False):
        if not isinstance(inventory, dict):
            raise ValueError("Inventory must be a dictionary")

        if extract_spec_version:
            type_value = inventory.get('type')
            if type_value and re.match(r'^v\d+\.\d+$', type_value):
                self.spec_version = type_value
            else:
                raise ValueError(f"Invalid type value: {type_value}")

        # Additional validation logic based on self.spec_version
        if self.spec_version == 'v1.0':
            # Validation rules for version 1.0
            pass
        elif self.spec_version == 'v2.0':
            # Validation rules for version 2.0
            pass
        else:
            raise ValueError(f"Unsupported specification version: {self.spec_version}")