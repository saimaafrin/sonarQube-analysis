def validate_as_prior_version(self, prior):
    if not isinstance(prior, InventoryValidator):
        return self.error("Invalid prior version: not an InventoryValidator object")
    
    if self.inventory_id != prior.inventory_id:
        return self.error("Invalid prior version: inventory IDs do not match")
    
    if self.version_number >= prior.version_number:
        return self.error("Invalid prior version: current version is not earlier than the prior version")
    
    return None