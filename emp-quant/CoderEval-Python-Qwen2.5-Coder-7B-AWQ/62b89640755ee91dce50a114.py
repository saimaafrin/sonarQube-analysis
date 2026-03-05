import sys

if sys.version_info[0] == 2:
    def tzname_in_python2(namefunc):
        return lambda: [n.encode('utf-8') for n in namefunc()]
else:
    tzname_in_python2 = lambda namefunc: namefunc