#!/usr/bin/env python
#
#  Copyright 2012, 2013 Nick Galbreath
#  nickg@client9.com
#  BSD License -- see COPYING.txt for details
#

"""
Converts a libinjection JSON data file to a C header (.h) file
"""

def toc(obj):
    """ main routine """

    print """
import libinjection
def lookup(state, stype, keyword):
    #print "GOt {0} {1}".format(stype, keyword)
    keyword = keyword.upper()
    if stype == libinjection.LOOKUP_FINGERPRINT:
        keyword = "0" + keyword
        ch = words.get(keyword, chr(0))
        if ch == 'X' and libinjection.sqli_not_whitelist(state):
            return 'X'
        else:
            return chr(0)
    return words.get(keyword, chr(0))
"""

    words = {}
    keywords = obj['keywords']

    for k,v in keywords.iteritems():
        words[str(k)] = str(v)

    for  fp in list(obj[u'fingerprints']):
        fp = '0' + fp.upper()
        words[str(fp)] = 'X';

    print 'words = {'
    for k in sorted(words.keys()):
        print "'{0}': '{1}',".format(k, words[k])
    print '}'
    return 0

if __name__ == '__main__':
    import sys
    import json
    sys.exit(toc(json.load(sys.stdin)))

