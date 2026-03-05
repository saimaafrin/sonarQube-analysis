def validate_as_prior_version(self, prior):
	"""
	Check that prior is a valid prior version of the current inventory object. The input variable prior is also expected to be an InventoryValidator object and both self and prior inventories are assumed to have been checked for internal consistency. Return error() in the class.
	"""
	if prior.inventory_version() != self.inventory_version():
		self.error("Prior version of inventory is not the same as the current version")
	if prior.inventory_version() < self.inventory_version():
		self.error("Prior version of inventory is older than the current version")
	if prior.inventory_version() == self.inventory_version():
		if prior.inventory_version() == 1:
			if prior.inventory_version() == self.inventory_version():
				if prior.inventory_version() == 1:
					if prior.inventory_version() == self.inventory_version():
						if prior.inventory_version() == self.inventory_version():
							if prior.inventory_version() == self.inventory_version():
								if prior.inventory_version() == self.inventory_version():
									if prior.inventory_version() == self.inventory_version():
										if prior.inventory_version() == self.inventory_version():
											if prior.inventory_version() == self.inventory_version():
												if prior.inventory_version() == self.inventory_version():
													if prior.inventory_version() == self.inventory_version():
														if prior.inventory_version() == self.inventory_version():
															if prior.inventory_version() == self.inventory_version():
																if prior.inventory_version() == self.inventory_version():
																	if prior.inventory_version() == self.inventory_version():