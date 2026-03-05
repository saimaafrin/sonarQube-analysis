for xpath in pubdate_xpaths:
    match = node.xpath(xpath)
    if match:
        return match[0]
return None