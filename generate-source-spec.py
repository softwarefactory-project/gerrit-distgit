#!/bin/env python
# Tiny script to generate source spec from mock build log

import sys

try:
    buildlog = open(sys.argv[1]).readlines()
except IndexError:
    print "usage: %s build.log" % sys.argv[0]
    exit(1)

deps = {}
for line in buildlog:
    if "curl" not in line:
        continue
    line = line.replace("'", "").replace("]", "").replace(",", "")
    line = line.split()
    try:
        deps[line[8]] = line[7]
    except:
        print line
        raise

deps_list = sorted(deps.keys())
idx = 100
for dep in deps_list:
    print "Source%3d:     %s" % (idx, dep)
    idx += 1

print
for dep in deps_list:
    if "-sources" in dep:
        continue
    d = dep[dep.rfind("/")+1:dep.find(".jar")]
    print "Provides:      bundled(%s)" % d

print
print "%setup"
idx = 100
for dep in deps_list:
    print "mv %%{SOURCE%d} %s" % (idx, deps[dep])
    idx += 1
