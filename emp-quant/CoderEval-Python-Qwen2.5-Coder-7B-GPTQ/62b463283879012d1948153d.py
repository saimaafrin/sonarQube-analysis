for xpath in pubdate_xpaths:
    result = node.xpath(xpath)
    if result:
        return result[0]
return None