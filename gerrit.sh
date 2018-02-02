#!/bin/sh

exec /usr/bin/java -Xmx${GERRIT_HEAP_LIMIT} \
     -Djava.security.egd=file:///dev/urandom \
     -jar /usr/lib64/gerrit/release.war \
     daemon -d /var/lib/gerrit/ --console-log
