def namesAndDescriptions(self, all=False):
    """
    Returns the name and description of the current class attribute.
    """
    if all:
        return self._get_all_names_and_descriptions()
    else:
        return self._get_current_name_and_description()