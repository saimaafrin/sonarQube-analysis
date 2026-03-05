def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if prior.version != self.version - 1:
		self.error("Prior version is not one less than current version")
	if prior.inventory_type != self.inventory_type:
		self.error("Prior inventory type is not the same as current inventory type")
	if prior.inventory_type == "single":
		if prior.single_inventory_type != self.single_inventory_type:
			self.error("Prior single inventory type is not the same as current single inventory type")
		if prior.single_inventory_type == "item":
			if prior.item_id != self.item_id:
				self.error("Prior item id is not the same as current item id")
			if prior.item_id == self.item_id:
				if prior.item_quantity != self.item_quantity:
					self.error("Prior item quantity is not the same as current item quantity")
				if prior.item_quantity == self.item_quantity:
					if prior.item_price != self.item_price:
						self.error("Prior item price is not the same as current item price")
					if prior.item_price == self.item_price:
						if prior.item_description != self.item_description:
							self.error("Prior item description is not the same as current item description")
						if prior.item_description == self.item_description:
							if prior.item_image != self.item_image:
								self.error("Prior item image is not the same as current item image")
							if prior.item_image == self.item_image:
								if prior.item_category != self.item_category:
									self.error("Prior item category is not the same as current item category")