import sys

if sys.version_info[0] == 2:
    def tzname_in_python2(namefunc):
        return lambda *args, **kwargs: namefunc(*args, **kwargs).encode('utf-8')
else:
    def tzname_in_python2(namefunc):
        return namefunc