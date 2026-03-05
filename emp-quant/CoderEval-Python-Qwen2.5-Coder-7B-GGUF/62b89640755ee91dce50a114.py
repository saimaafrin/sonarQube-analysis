import sys

def tzname_in_python2(namefunc):
    if sys.version_info[0] == 2:
        return lambda *args, **kwargs: [n.encode('utf-8') if isinstance(n, unicode) else n for n in namefunc(*args, **kwargs)]
    else:
        return namefunc