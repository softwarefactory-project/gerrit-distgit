Name:          gerrit
Version:       2.11.10
Release:       3%{?dist}
Summary:       Code review system

License:       APACHE-2
URL:           https://www.gerritcodereview.com
Source0:       https://gerrit.googlesource.com/gerrit/+archive/11a891ddf8a01fef5f487a35950a60e7f5f738cb.tar.gz
Source1:       gerrit.service

# Plugins
Source10:      https://gerrit.googlesource.com/plugins/commit-message-length-validator/+archive/76b9115b830cab453c12dd9014f5130c7b7f2ce5.tar.gz
Source11:      https://gerrit.googlesource.com/plugins/download-commands/+archive/63e7cf5f24045ede2ee9e5a220e594716b2b6ce4.tar.gz
Source12:      https://gerrit.googlesource.com/plugins/replication/+archive/85685f618eecf41bc0bc3a65bc1c849b96bca4e8.tar.gz
Source13:      https://gerrit.googlesource.com/plugins/reviewnotes/+archive/f6403a1ed35e908a4828fdc9168ed752fa178c69.tar.gz
Source14:      https://gerrit.googlesource.com/plugins/singleusergroup/+archive/691c9c9c4fa6c0a533ee8386e991a41224c87243.tar.gz
Source15:      https://gerrit.googlesource.com/plugins/avatars-gravatar/+archive/94061de368332af13218f82605a41e9fc8d4c7c9.tar.gz
Source16:      https://gerrit.googlesource.com/plugins/delete-project/+archive/9eb4988bc9c6ddf4a939497b1018b77d0c92104c.tar.gz
Source17:      https://gerrit.googlesource.com/plugins/reviewers-by-blame/+archive/c679c0c9f85378a723261c9f603ad3d9c05b93b4.tar.gz

# Build req
Source100:     http://gerrit-maven.storage.googleapis.com/com/google/gerrit/gwtorm/1.14-14-gf54f1f1/gwtorm-1.14-14-gf54f1f1-sources.jar
Source101:     http://gerrit-maven.storage.googleapis.com/com/google/gerrit/gwtorm/1.14-14-gf54f1f1/gwtorm-1.14-14-gf54f1f1.jar
Source102:     http://gerrit-maven.storage.googleapis.com/com/googlecode/prolog-cafe/PrologCafe/1.3/PrologCafe-1.3-sources.jar
Source103:     http://gerrit-maven.storage.googleapis.com/com/googlecode/prolog-cafe/PrologCafe/1.3/PrologCafe-1.3.jar
Source104:     http://gerrit-maven.storage.googleapis.com/gwtjsonrpc/gwtjsonrpc/1.7-2-g272ca32/gwtjsonrpc-1.7-2-g272ca32-sources.jar
Source105:     http://gerrit-maven.storage.googleapis.com/gwtjsonrpc/gwtjsonrpc/1.7-2-g272ca32/gwtjsonrpc-1.7-2-g272ca32.jar
Source106:     http://repo1.maven.org/maven2/antlr/antlr/2.7.7/antlr-2.7.7.jar
Source107:     http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0-sources.jar
Source108:     http://repo1.maven.org/maven2/aopalliance/aopalliance/1.0/aopalliance-1.0.jar
Source109:     http://repo1.maven.org/maven2/args4j/args4j/2.0.26/args4j-2.0.26-sources.jar
Source110:     http://repo1.maven.org/maven2/args4j/args4j/2.0.26/args4j-2.0.26.jar
Source111:     http://repo1.maven.org/maven2/com/github/parboiled1/grappa/1.0.4/grappa-1.0.4-sources.jar
Source112:     http://repo1.maven.org/maven2/com/github/parboiled1/grappa/1.0.4/grappa-1.0.4.jar
Source113:     http://repo1.maven.org/maven2/com/google/auto/value/auto-value/1.0/auto-value-1.0-sources.jar
Source114:     http://repo1.maven.org/maven2/com/google/auto/value/auto-value/1.0/auto-value-1.0.jar
Source115:     http://repo1.maven.org/maven2/com/google/code/gson/gson/2.1/gson-2.1-sources.jar
Source116:     http://repo1.maven.org/maven2/com/google/code/gson/gson/2.1/gson-2.1.jar
Source117:     http://repo1.maven.org/maven2/com/google/guava/guava/18.0/guava-18.0-sources.jar
Source118:     http://repo1.maven.org/maven2/com/google/guava/guava/18.0/guava-18.0.jar
Source119:     http://repo1.maven.org/maven2/com/google/gwt/gwt-dev/2.7.0/gwt-dev-2.7.0.jar
Source120:     http://repo1.maven.org/maven2/com/google/gwt/gwt-user/2.7.0/gwt-user-2.7.0.jar
Source121:     http://repo1.maven.org/maven2/com/google/inject/extensions/guice-assistedinject/4.0/guice-assistedinject-4.0-sources.jar
Source122:     http://repo1.maven.org/maven2/com/google/inject/extensions/guice-assistedinject/4.0/guice-assistedinject-4.0.jar
Source123:     http://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0-sources.jar
Source124:     http://repo1.maven.org/maven2/com/google/inject/extensions/guice-servlet/4.0/guice-servlet-4.0.jar
Source125:     http://repo1.maven.org/maven2/com/google/inject/guice/4.0/guice-4.0-sources.jar
Source126:     http://repo1.maven.org/maven2/com/google/inject/guice/4.0/guice-4.0.jar
Source127:     http://repo1.maven.org/maven2/com/google/javascript/closure-compiler-externs/v20141120/closure-compiler-externs-v20141120-sources.jar
Source128:     http://repo1.maven.org/maven2/com/google/javascript/closure-compiler-externs/v20141120/closure-compiler-externs-v20141120.jar
Source129:     http://repo1.maven.org/maven2/com/google/javascript/closure-compiler/v20141120/closure-compiler-v20141120-sources.jar
Source130:     http://repo1.maven.org/maven2/com/google/javascript/closure-compiler/v20141120/closure-compiler-v20141120.jar
Source131:     http://repo1.maven.org/maven2/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0-sources.jar
Source132:     http://repo1.maven.org/maven2/com/google/protobuf/protobuf-java/2.5.0/protobuf-java-2.5.0.jar
Source133:     http://repo1.maven.org/maven2/com/googlecode/javaewah/JavaEWAH/0.7.9/JavaEWAH-0.7.9-sources.jar
Source134:     http://repo1.maven.org/maven2/com/googlecode/javaewah/JavaEWAH/0.7.9/JavaEWAH-0.7.9.jar
Source135:     http://repo1.maven.org/maven2/com/googlecode/juniversalchardet/juniversalchardet/1.0.3/juniversalchardet-1.0.3-sources.jar
Source136:     http://repo1.maven.org/maven2/com/googlecode/juniversalchardet/juniversalchardet/1.0.3/juniversalchardet-1.0.3.jar
Source137:     http://repo1.maven.org/maven2/com/h2database/h2/1.3.174/h2-1.3.174-sources.jar
Source138:     http://repo1.maven.org/maven2/com/h2database/h2/1.3.174/h2-1.3.174.jar
Source139:     http://repo1.maven.org/maven2/com/jcraft/jsch/0.1.54/jsch-0.1.54-sources.jar
Source140:     http://repo1.maven.org/maven2/com/jcraft/jsch/0.1.54/jsch-0.1.54.jar
Source141:     http://repo1.maven.org/maven2/commons-codec/commons-codec/1.4/commons-codec-1.4-sources.jar
Source142:     http://repo1.maven.org/maven2/commons-codec/commons-codec/1.4/commons-codec-1.4.jar
Source143:     http://repo1.maven.org/maven2/commons-collections/commons-collections/3.2.2/commons-collections-3.2.2.jar
Source144:     http://repo1.maven.org/maven2/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4-sources.jar
Source145:     http://repo1.maven.org/maven2/commons-dbcp/commons-dbcp/1.4/commons-dbcp-1.4.jar
Source146:     http://repo1.maven.org/maven2/commons-io/commons-io/1.4/commons-io-1.4-sources.jar
Source147:     http://repo1.maven.org/maven2/commons-io/commons-io/1.4/commons-io-1.4.jar
Source148:     http://repo1.maven.org/maven2/commons-lang/commons-lang/2.5/commons-lang-2.5-sources.jar
Source149:     http://repo1.maven.org/maven2/commons-lang/commons-lang/2.5/commons-lang-2.5.jar
Source150:     http://repo1.maven.org/maven2/commons-net/commons-net/2.2/commons-net-2.2-sources.jar
Source151:     http://repo1.maven.org/maven2/commons-net/commons-net/2.2/commons-net-2.2.jar
Source152:     http://repo1.maven.org/maven2/commons-pool/commons-pool/1.5.5/commons-pool-1.5.5.jar
Source153:     http://repo1.maven.org/maven2/commons-validator/commons-validator/1.4.1/commons-validator-1.4.1-sources.jar
Source154:     http://repo1.maven.org/maven2/commons-validator/commons-validator/1.4.1/commons-validator-1.4.1.jar
Source155:     http://repo1.maven.org/maven2/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8-sources.jar
Source156:     http://repo1.maven.org/maven2/dk/brics/automaton/automaton/1.11-8/automaton-1.11-8.jar
Source157:     http://repo1.maven.org/maven2/eu/medsea/mimeutil/mime-util/2.1.3/mime-util-2.1.3.jar
Source158:     http://repo1.maven.org/maven2/javax/inject/javax.inject/1/javax.inject-1-sources.jar
Source159:     http://repo1.maven.org/maven2/javax/inject/javax.inject/1/javax.inject-1.jar
Source160:     http://repo1.maven.org/maven2/javax/validation/validation-api/1.0.0.GA/validation-api-1.0.0.GA-sources.jar
Source161:     http://repo1.maven.org/maven2/javax/validation/validation-api/1.0.0.GA/validation-api-1.0.0.GA.jar
Source162:     http://repo1.maven.org/maven2/joda-time/joda-time/2.3/joda-time-2.3-sources.jar
Source163:     http://repo1.maven.org/maven2/joda-time/joda-time/2.3/joda-time-2.3.jar
Source164:     http://repo1.maven.org/maven2/log4j/log4j/1.2.17/log4j-1.2.17-sources.jar
Source165:     http://repo1.maven.org/maven2/log4j/log4j/1.2.17/log4j-1.2.17.jar
Source166:     http://repo1.maven.org/maven2/me/qmx/jitescript/jitescript/0.4.0/jitescript-0.4.0-sources.jar
Source167:     http://repo1.maven.org/maven2/me/qmx/jitescript/jitescript/0.4.0/jitescript-0.4.0.jar
Source168:     http://repo1.maven.org/maven2/net/sourceforge/nekohtml/nekohtml/1.9.10/nekohtml-1.9.10.jar
Source169:     http://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2-sources.jar
Source170:     http://repo1.maven.org/maven2/org/antlr/antlr-runtime/3.5.2/antlr-runtime-3.5.2.jar
Source171:     http://repo1.maven.org/maven2/org/antlr/antlr/3.5.2/antlr-3.5.2-sources.jar
Source172:     http://repo1.maven.org/maven2/org/antlr/antlr/3.5.2/antlr-3.5.2.jar
Source173:     http://repo1.maven.org/maven2/org/antlr/stringtemplate/4.0.2/stringtemplate-4.0.2.jar
Source174:     http://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.7/commons-compress-1.7-sources.jar
Source175:     http://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.7/commons-compress-1.7.jar
Source176:     http://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.3.4/httpclient-4.3.4-sources.jar
Source177:     http://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.3.4/httpclient-4.3.4.jar
Source178:     http://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2-sources.jar
Source179:     http://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3.2/httpcore-4.3.2.jar
Source180:     http://repo1.maven.org/maven2/org/apache/httpcomponents/httpmime/4.3.4/httpmime-4.3.4-sources.jar
Source181:     http://repo1.maven.org/maven2/org/apache/httpcomponents/httpmime/4.3.4/httpmime-4.3.4.jar
Source182:     http://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-common/4.10.2/lucene-analyzers-common-4.10.2-sources.jar
Source183:     http://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-common/4.10.2/lucene-analyzers-common-4.10.2.jar
Source184:     http://repo1.maven.org/maven2/org/apache/lucene/lucene-core/4.10.2/lucene-core-4.10.2-sources.jar
Source185:     http://repo1.maven.org/maven2/org/apache/lucene/lucene-core/4.10.2/lucene-core-4.10.2.jar
Source186:     http://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/4.10.2/lucene-queryparser-4.10.2-sources.jar
Source187:     http://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/4.10.2/lucene-queryparser-4.10.2.jar
Source188:     http://repo1.maven.org/maven2/org/apache/mina/mina-core/2.0.8/mina-core-2.0.8-sources.jar
Source189:     http://repo1.maven.org/maven2/org/apache/mina/mina-core/2.0.8/mina-core-2.0.8.jar
Source190:     http://repo1.maven.org/maven2/org/apache/solr/solr-solrj/4.3.1/solr-solrj-4.3.1-sources.jar
Source191:     http://repo1.maven.org/maven2/org/apache/solr/solr-solrj/4.3.1/solr-solrj-4.3.1.jar
Source192:     http://repo1.maven.org/maven2/org/apache/sshd/sshd-core/0.14.0/sshd-core-0.14.0-sources.jar
Source193:     http://repo1.maven.org/maven2/org/apache/sshd/sshd-core/0.14.0/sshd-core-0.14.0.jar
Source194:     http://repo1.maven.org/maven2/org/apache/tomcat/tomcat-servlet-api/8.0.5/tomcat-servlet-api-8.0.5-sources.jar
Source195:     http://repo1.maven.org/maven2/org/apache/tomcat/tomcat-servlet-api/8.0.5/tomcat-servlet-api-8.0.5.jar
Source196:     http://repo1.maven.org/maven2/org/apache/velocity/velocity/1.7/velocity-1.7-sources.jar
Source197:     http://repo1.maven.org/maven2/org/apache/velocity/velocity/1.7/velocity-1.7.jar
Source198:     http://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.5/zookeeper-3.4.5-sources.jar
Source199:     http://repo1.maven.org/maven2/org/apache/zookeeper/zookeeper/3.4.5/zookeeper-3.4.5.jar
Source200:     http://repo1.maven.org/maven2/org/asciidoctor/asciidoctorj/1.5.0/asciidoctorj-1.5.0.jar
Source201:     http://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/1.51/bcpg-jdk15on-1.51-sources.jar
Source202:     http://repo1.maven.org/maven2/org/bouncycastle/bcpg-jdk15on/1.51/bcpg-jdk15on-1.51.jar
Source203:     http://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/1.51/bcpkix-jdk15on-1.51-sources.jar
Source204:     http://repo1.maven.org/maven2/org/bouncycastle/bcpkix-jdk15on/1.51/bcpkix-jdk15on-1.51.jar
Source205:     http://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51-sources.jar
Source206:     http://repo1.maven.org/maven2/org/bouncycastle/bcprov-jdk15on/1.51/bcprov-jdk15on-1.51.jar
Source207:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-continuation/9.2.9.v20150224/jetty-continuation-9.2.9.v20150224-sources.jar
Source208:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-continuation/9.2.9.v20150224/jetty-continuation-9.2.9.v20150224.jar
Source209:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-http/9.2.9.v20150224/jetty-http-9.2.9.v20150224-sources.jar
Source210:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-http/9.2.9.v20150224/jetty-http-9.2.9.v20150224.jar
Source211:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-io/9.2.9.v20150224/jetty-io-9.2.9.v20150224-sources.jar
Source212:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-io/9.2.9.v20150224/jetty-io-9.2.9.v20150224.jar
Source213:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-jmx/9.2.9.v20150224/jetty-jmx-9.2.9.v20150224-sources.jar
Source214:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-jmx/9.2.9.v20150224/jetty-jmx-9.2.9.v20150224.jar
Source215:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-security/9.2.9.v20150224/jetty-security-9.2.9.v20150224-sources.jar
Source216:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-security/9.2.9.v20150224/jetty-security-9.2.9.v20150224.jar
Source217:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-server/9.2.9.v20150224/jetty-server-9.2.9.v20150224-sources.jar
Source218:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-server/9.2.9.v20150224/jetty-server-9.2.9.v20150224.jar
Source219:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-servlet/9.2.9.v20150224/jetty-servlet-9.2.9.v20150224-sources.jar
Source220:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-servlet/9.2.9.v20150224/jetty-servlet-9.2.9.v20150224.jar
Source221:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-util/9.2.9.v20150224/jetty-util-9.2.9.v20150224-sources.jar
Source222:     http://repo1.maven.org/maven2/org/eclipse/jetty/jetty-util/9.2.9.v20150224/jetty-util-9.2.9.v20150224.jar
Source223:     http://repo1.maven.org/maven2/org/eclipse/jgit/org.eclipse.jgit.archive/4.0.1.201506240215-r/org.eclipse.jgit.archive-4.0.1.201506240215-r-sources.jar
Source224:     http://repo1.maven.org/maven2/org/eclipse/jgit/org.eclipse.jgit.archive/4.0.1.201506240215-r/org.eclipse.jgit.archive-4.0.1.201506240215-r.jar
Source225:     http://repo1.maven.org/maven2/org/eclipse/jgit/org.eclipse.jgit.http.server/4.0.1.201506240215-r/org.eclipse.jgit.http.server-4.0.1.201506240215-r-sources.jar
Source226:     http://repo1.maven.org/maven2/org/eclipse/jgit/org.eclipse.jgit.http.server/4.0.1.201506240215-r/org.eclipse.jgit.http.server-4.0.1.201506240215-r.jar
Source227:     http://repo1.maven.org/maven2/org/eclipse/jgit/org.eclipse.jgit/4.0.1.201506240215-r/org.eclipse.jgit-4.0.1.201506240215-r-sources.jar
Source228:     http://repo1.maven.org/maven2/org/eclipse/jgit/org.eclipse.jgit/4.0.1.201506240215-r/org.eclipse.jgit-4.0.1.201506240215-r.jar
Source229:     http://repo1.maven.org/maven2/org/joda/joda-convert/1.2/joda-convert-1.2-sources.jar
Source230:     http://repo1.maven.org/maven2/org/joda/joda-convert/1.2/joda-convert-1.2.jar
Source231:     http://repo1.maven.org/maven2/org/jruby/jruby-complete/1.7.4/jruby-complete-1.7.4.jar
Source232:     http://repo1.maven.org/maven2/org/noggit/noggit/0.5/noggit-0.5-sources.jar
Source233:     http://repo1.maven.org/maven2/org/noggit/noggit/0.5/noggit-0.5.jar
Source234:     http://repo1.maven.org/maven2/org/openid4java/openid4java/0.9.8/openid4java-0.9.8-sources.jar
Source235:     http://repo1.maven.org/maven2/org/openid4java/openid4java/0.9.8/openid4java-0.9.8.jar
Source236:     http://repo1.maven.org/maven2/org/ow2/asm/asm-analysis/5.0.3/asm-analysis-5.0.3-sources.jar
Source237:     http://repo1.maven.org/maven2/org/ow2/asm/asm-analysis/5.0.3/asm-analysis-5.0.3.jar
Source238:     http://repo1.maven.org/maven2/org/ow2/asm/asm-commons/5.0.3/asm-commons-5.0.3-sources.jar
Source239:     http://repo1.maven.org/maven2/org/ow2/asm/asm-commons/5.0.3/asm-commons-5.0.3.jar
Source240:     http://repo1.maven.org/maven2/org/ow2/asm/asm-tree/5.0.3/asm-tree-5.0.3-sources.jar
Source241:     http://repo1.maven.org/maven2/org/ow2/asm/asm-tree/5.0.3/asm-tree-5.0.3.jar
Source242:     http://repo1.maven.org/maven2/org/ow2/asm/asm-util/5.0.3/asm-util-5.0.3-sources.jar
Source243:     http://repo1.maven.org/maven2/org/ow2/asm/asm-util/5.0.3/asm-util-5.0.3.jar
Source244:     http://repo1.maven.org/maven2/org/ow2/asm/asm/5.0.3/asm-5.0.3-sources.jar
Source245:     http://repo1.maven.org/maven2/org/ow2/asm/asm/5.0.3/asm-5.0.3.jar
Source246:     http://repo1.maven.org/maven2/org/pegdown/pegdown/1.4.2/pegdown-1.4.2-sources.jar
Source247:     http://repo1.maven.org/maven2/org/pegdown/pegdown/1.4.2/pegdown-1.4.2.jar
Source248:     http://repo1.maven.org/maven2/org/slf4j/jcl-over-slf4j/1.7.7/jcl-over-slf4j-1.7.7-sources.jar
Source249:     http://repo1.maven.org/maven2/org/slf4j/jcl-over-slf4j/1.7.7/jcl-over-slf4j-1.7.7.jar
Source250:     http://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.7/slf4j-api-1.7.7-sources.jar
Source251:     http://repo1.maven.org/maven2/org/slf4j/slf4j-api/1.7.7/slf4j-api-1.7.7.jar
Source252:     http://repo1.maven.org/maven2/org/slf4j/slf4j-log4j12/1.7.7/slf4j-log4j12-1.7.7-sources.jar
Source253:     http://repo1.maven.org/maven2/org/slf4j/slf4j-log4j12/1.7.7/slf4j-log4j12-1.7.7.jar
Source254:     http://repo1.maven.org/maven2/org/tukaani/xz/1.4/xz-1.4.jar
Source255:     http://repo1.maven.org/maven2/org/webjars/codemirror/5.0/codemirror-5.0.jar
Source256:     http://repo1.maven.org/maven2/oro/oro/2.0.8/oro-2.0.8.jar
Source257:     http://repo1.maven.org/maven2/postgresql/postgresql/9.1-901-1.jdbc4/postgresql-9.1-901-1.jdbc4.jar
Source258:     http://repo1.maven.org/maven2/xerces/xercesImpl/2.8.1/xercesImpl-2.8.1.jar

BuildRequires: buck
BuildRequires: systemd
Requires:      java-1.8.0-openjdk
Requires:      mysql-connector-java
Requires:      wait4service

Provides:      bundled(gwtorm-1.14-14-gf54f1f1)
Provides:      bundled(PrologCafe-1.3)
Provides:      bundled(gwtjsonrpc-1.7-2-g272ca32)
Provides:      bundled(antlr-2.7.7)
Provides:      bundled(aopalliance-1.0)
Provides:      bundled(args4j-2.0.26)
Provides:      bundled(grappa-1.0.4)
Provides:      bundled(auto-value-1.0)
Provides:      bundled(gson-2.1)
Provides:      bundled(guava-18.0)
Provides:      bundled(gwt-dev-2.7.0)
Provides:      bundled(gwt-user-2.7.0)
Provides:      bundled(guice-assistedinject-4.0)
Provides:      bundled(guice-servlet-4.0)
Provides:      bundled(guice-4.0)
Provides:      bundled(closure-compiler-externs-v20141120)
Provides:      bundled(closure-compiler-v20141120)
Provides:      bundled(protobuf-java-2.5.0)
Provides:      bundled(JavaEWAH-0.7.9)
Provides:      bundled(juniversalchardet-1.0.3)
Provides:      bundled(h2-1.3.174)
Provides:      bundled(jsch-0.1.54)
Provides:      bundled(commons-codec-1.4)
Provides:      bundled(commons-collections-3.2.2)
Provides:      bundled(commons-dbcp-1.4)
Provides:      bundled(commons-io-1.4)
Provides:      bundled(commons-lang-2.5)
Provides:      bundled(commons-net-2.2)
Provides:      bundled(commons-pool-1.5.5)
Provides:      bundled(commons-validator-1.4.1)
Provides:      bundled(automaton-1.11-8)
Provides:      bundled(mime-util-2.1.3)
Provides:      bundled(javax.inject-1)
Provides:      bundled(validation-api-1.0.0.GA)
Provides:      bundled(joda-time-2.3)
Provides:      bundled(log4j-1.2.17)
Provides:      bundled(jitescript-0.4.0)
Provides:      bundled(nekohtml-1.9.10)
Provides:      bundled(antlr-runtime-3.5.2)
Provides:      bundled(antlr-3.5.2)
Provides:      bundled(stringtemplate-4.0.2)
Provides:      bundled(commons-compress-1.7)
Provides:      bundled(httpclient-4.3.4)
Provides:      bundled(httpcore-4.3.2)
Provides:      bundled(httpmime-4.3.4)
Provides:      bundled(lucene-analyzers-common-4.10.2)
Provides:      bundled(lucene-core-4.10.2)
Provides:      bundled(lucene-queryparser-4.10.2)
Provides:      bundled(mina-core-2.0.8)
Provides:      bundled(solr-solrj-4.3.1)
Provides:      bundled(sshd-core-0.14.0)
Provides:      bundled(tomcat-servlet-api-8.0.5)
Provides:      bundled(velocity-1.7)
Provides:      bundled(zookeeper-3.4.5)
Provides:      bundled(asciidoctorj-1.5.0)
Provides:      bundled(bcpg-jdk15on-1.51)
Provides:      bundled(bcpkix-jdk15on-1.51)
Provides:      bundled(bcprov-jdk15on-1.51)
Provides:      bundled(jetty-continuation-9.2.9.v20150224)
Provides:      bundled(jetty-http-9.2.9.v20150224)
Provides:      bundled(jetty-io-9.2.9.v20150224)
Provides:      bundled(jetty-jmx-9.2.9.v20150224)
Provides:      bundled(jetty-security-9.2.9.v20150224)
Provides:      bundled(jetty-server-9.2.9.v20150224)
Provides:      bundled(jetty-servlet-9.2.9.v20150224)
Provides:      bundled(jetty-util-9.2.9.v20150224)
Provides:      bundled(org.eclipse.jgit.archive-4.0.1.201506240215-r)
Provides:      bundled(org.eclipse.jgit.http.server-4.0.1.201506240215-r)
Provides:      bundled(org.eclipse.jgit-4.0.1.201506240215-r)
Provides:      bundled(joda-convert-1.2)
Provides:      bundled(jruby-complete-1.7.4)
Provides:      bundled(noggit-0.5)
Provides:      bundled(openid4java-0.9.8)
Provides:      bundled(asm-analysis-5.0.3)
Provides:      bundled(asm-commons-5.0.3)
Provides:      bundled(asm-tree-5.0.3)
Provides:      bundled(asm-util-5.0.3)
Provides:      bundled(asm-5.0.3)
Provides:      bundled(pegdown-1.4.2)
Provides:      bundled(jcl-over-slf4j-1.7.7)
Provides:      bundled(slf4j-api-1.7.7)
Provides:      bundled(slf4j-log4j12-1.7.7)
Provides:      bundled(xz-1.4)
Provides:      bundled(codemirror-5.0)
Provides:      bundled(oro-2.0.8)
Provides:      bundled(postgresql-9.1-901-1.jdbc4)
Provides:      bundled(xercesImpl-2.8.1)


%description
Gerrit provides web based code review and repository management for the Git version control system.

%package plugin-commit-message-length-validator
Requires:      gerrit
Summary:       Gerrit commit-message-length-validator plugin

%description plugin-commit-message-length-validator
Gerrit commit-message-length-validator plugin

%package plugin-download-commands
Requires:      gerrit
Summary:       Gerrit download-commands plugin

%description plugin-download-commands
Gerrit download-commands plugin

%package plugin-replication
Requires:      gerrit
Summary:       Gerrit replication plugin

%description plugin-replication
Gerrit replication plugin

%package plugin-reviewnotes
Requires:      gerrit
Summary:       Gerrit reviewnotes plugin

%description plugin-reviewnotes
Gerrit reviewnotes plugin

%package plugin-singleusergroup
Requires:      gerrit
Summary:       Gerrit singleusergroup plugin

%description plugin-singleusergroup
Gerrit singleusergroup plugin

%package plugin-avatars-gravatar
Requires:      gerrit
Summary:       Gerrit avatars-gravatar plugin

%description plugin-avatars-gravatar
Gerrit avatars-gravatar plugin

%package plugin-delete-project
Requires:      gerrit
Summary:       Gerrit delete-project plugin

%description plugin-delete-project
Gerrit delete-project plugin

%package plugin-reviewers-by-blame
Requires:      gerrit
Summary:       Gerrit reviewers-by-blame plugin

%description plugin-reviewers-by-blame
Gerrit reviewers-by-blame plugin

%prep
%setup -q -c gerrit-2.11.10
# Disable war copy to site_path
sed -i 's|if (copy) {|if (false) {|' gerrit-pgm/src/main/java/com/google/gerrit/pgm/init/InitContainer.java
# Disable gerrit.sh creation
sed -i 's|extract(site.gerrit_sh, getClass(), "gerrit.sh");||' gerrit-pgm/src/main/java/com/google/gerrit/pgm/init/SitePathInitializer.java
sed -i 's|chmod(0755, site.gerrit_sh);||' gerrit-pgm/src/main/java/com/google/gerrit/pgm/init/SitePathInitializer.java
# Bump JSCH lib due to https://github.com/blog/2507-weak-cryptographic-standards-removed
sed -i 's/com.jcraft:jsch:0.1.51/com.jcraft:jsch:0.1.54/' lib/BUCK
sed -i 's/6ceee2696b07cc320d0e1aaea82c7b40768aca0f/da3584329a263616e277e15462b387addd1b208d/' lib/BUCK

tar -xzf %{SOURCE10} -C plugins/commit-message-length-validator/
tar -xzf %{SOURCE11} -C plugins/download-commands/
tar -xzf %{SOURCE12} -C plugins/replication/
tar -xzf %{SOURCE13} -C plugins/reviewnotes/
tar -xzf %{SOURCE14} -C plugins/singleusergroup/
mkdir plugins/avatars-gravatar/ plugins/delete-project/ plugins/reviewers-by-blame/
tar -xzf %{SOURCE15} -C plugins/avatars-gravatar/
tar -xzf %{SOURCE16} -C plugins/delete-project/
tar -xzf %{SOURCE17} -C plugins/reviewers-by-blame/

mkdir -p /builddir/.gerritcodereview/buck-cache/
mv %{SOURCE100} /builddir/.gerritcodereview/buck-cache/gwtorm-1.14-14-gf54f1f1-src.jar-3d17ae8a173eb34d89098c748f28cddd5080adbc
mv %{SOURCE101} /builddir/.gerritcodereview/buck-cache/gwtorm-1.14-14-gf54f1f1.jar-c02267e0245dd06930ea64a2d7c5ddc5ba6d9cfb
mv %{SOURCE102} /builddir/.gerritcodereview/buck-cache/prologcafe-1.3-src.jar-251d8e6e592feadd2a18567640a523b4d6a30ae7
mv %{SOURCE103} /builddir/.gerritcodereview/buck-cache/prologcafe-1.3.jar-5e0fbf18e8c98c4113f9acc978306884a1152870
mv %{SOURCE104} /builddir/.gerritcodereview/buck-cache/gwtjsonrpc-1.7-2-g272ca32-src.jar-7e6d8892f2e3bf21a9854afcfd2534263636dcbc
mv %{SOURCE105} /builddir/.gerritcodereview/buck-cache/gwtjsonrpc-1.7-2-g272ca32.jar-91be25537f7e53e0b5ff5edb9a42ebfc56f764b6
mv %{SOURCE106} /builddir/.gerritcodereview/buck-cache/antlr-2.7.7.jar-83cd2cd674a217ade95a4bb83a8a14f351f48bd0
mv %{SOURCE107} /builddir/.gerritcodereview/buck-cache/aopalliance-1.0-src.jar-d453043d02c6726a0df168ec0f9a95fe9afbb1e1
mv %{SOURCE108} /builddir/.gerritcodereview/buck-cache/aopalliance-1.0.jar-0235ba8b489512805ac13a8f9ea77a1ca5ebe3e8
mv %{SOURCE109} /builddir/.gerritcodereview/buck-cache/args4j-2.0.26-src.jar-c669607e3ddeaa7c8a013272550ac1e4a0bbedcd
mv %{SOURCE110} /builddir/.gerritcodereview/buck-cache/args4j-2.0.26.jar-01ebb18ebb3b379a74207d5af4ea7c8338ebd78b
mv %{SOURCE111} /builddir/.gerritcodereview/buck-cache/grappa-1.0.4-src.jar-2d212ef5085ed0e0608222de883770123b84200e
mv %{SOURCE112} /builddir/.gerritcodereview/buck-cache/grappa-1.0.4.jar-ad4b44b9c305dad7aa1e680d4b5c8eec9c4fd6f5
mv %{SOURCE113} /builddir/.gerritcodereview/buck-cache/auto-value-1.0-src.jar-ec7910343da1202f18ca703a83582169f1b42000
mv %{SOURCE114} /builddir/.gerritcodereview/buck-cache/auto-value-1.0.jar-5d13e60f5d190003176ca6ba4a410fae2e3f6315
mv %{SOURCE115} /builddir/.gerritcodereview/buck-cache/gson-2.1-src.jar-190799010a11f191101bc89431ea1f4e3c3d17d9
mv %{SOURCE116} /builddir/.gerritcodereview/buck-cache/gson-2.1.jar-2e66da15851f9f5b5079228f856c2f090ba98c38
mv %{SOURCE117} /builddir/.gerritcodereview/buck-cache/guava-18.0-src.jar-45b0363545dd28412143940c0a8ee5d75b58d0d6
mv %{SOURCE118} /builddir/.gerritcodereview/buck-cache/guava-18.0.jar-cce0823396aa693798f8882e64213b1772032b09
mv %{SOURCE119} /builddir/.gerritcodereview/buck-cache/gwt-dev-2.7.0.jar-c2c3dd5baf648a0bb199047a818be5e560f48982
mv %{SOURCE120} /builddir/.gerritcodereview/buck-cache/gwt-user-2.7.0.jar-bdc7af42581745d3d79c2efe0b514f432b998a5b
mv %{SOURCE121} /builddir/.gerritcodereview/buck-cache/guice-assistedinject-4.0-src.jar-81d475117b5adcc8264c95e2480ff301c59e0b01
mv %{SOURCE122} /builddir/.gerritcodereview/buck-cache/guice-assistedinject-4.0.jar-8fa6431da1a2187817e3e52e967535899e2e46ca
mv %{SOURCE123} /builddir/.gerritcodereview/buck-cache/guice-servlet-4.0-src.jar-a552d4b2dae7662e0cd293cfd4a528e01973a188
mv %{SOURCE124} /builddir/.gerritcodereview/buck-cache/guice-servlet-4.0.jar-4503da866f4c402b5090579b40c1c4aaefabb164
mv %{SOURCE125} /builddir/.gerritcodereview/buck-cache/guice-4.0-src.jar-887c14f2e777c89b93340bfb565d794ce7aab026
mv %{SOURCE126} /builddir/.gerritcodereview/buck-cache/guice-4.0.jar-0f990a43d3725781b6db7cd0acf0a8b62dfd1649
mv %{SOURCE127} /builddir/.gerritcodereview/buck-cache/closure-compiler-externs-v20141120-src.jar-8711a528293a49a445b16d3403df165b16317b45
mv %{SOURCE128} /builddir/.gerritcodereview/buck-cache/closure-compiler-externs-v20141120.jar-247eff337e2737de43c8d963aaaef15bd8cda132
mv %{SOURCE129} /builddir/.gerritcodereview/buck-cache/closure-compiler-v20141120-src.jar-a36e3c2823d1a09f458c858f7d4cac7759e05079
mv %{SOURCE130} /builddir/.gerritcodereview/buck-cache/closure-compiler-v20141120.jar-369618bf5a96f73e32655dc48919c0f97558d3b1
mv %{SOURCE131} /builddir/.gerritcodereview/buck-cache/protobuf-java-2.5.0-src.jar-7a27a7fc815e481b367ead5df19b4a71ace4a419
mv %{SOURCE132} /builddir/.gerritcodereview/buck-cache/protobuf-java-2.5.0.jar-a10732c76bfacdbd633a7eb0f7968b1059a65dfa
mv %{SOURCE133} /builddir/.gerritcodereview/buck-cache/javaewah-0.7.9-src.jar-dd7152dbfe349ce0d4e311f5bf2fd91935e22f77
mv %{SOURCE134} /builddir/.gerritcodereview/buck-cache/javaewah-0.7.9.jar-eceaf316a8faf0e794296ebe158ae110c7d72a5a
mv %{SOURCE135} /builddir/.gerritcodereview/buck-cache/juniversalchardet-1.0.3-src.jar-757189ba204b31781d1feeefa5f7804b2eb3b8b2
mv %{SOURCE136} /builddir/.gerritcodereview/buck-cache/juniversalchardet-1.0.3.jar-cd49678784c46aa8789c060538e0154013bb421b
mv %{SOURCE137} /builddir/.gerritcodereview/buck-cache/h2-1.3.174-src.jar-c490e234510149710dcae2bfc562a978803aecf0
mv %{SOURCE138} /builddir/.gerritcodereview/buck-cache/h2-1.3.174.jar-2fb55391f525bc3ef9f320a379d19350af96a554
mv %{SOURCE139} /builddir/.gerritcodereview/buck-cache/jsch-0.1.54-src.jar-91d6069df9be9e076bdb124e82fc2a9af9547616
mv %{SOURCE140} /builddir/.gerritcodereview/buck-cache/jsch-0.1.54.jar-da3584329a263616e277e15462b387addd1b208d
mv %{SOURCE141} /builddir/.gerritcodereview/buck-cache/commons-codec-1.4-src.jar-803197d8593ea641de0927614262119c2c695d24
mv %{SOURCE142} /builddir/.gerritcodereview/buck-cache/commons-codec-1.4.jar-4216af16d38465bbab0f3dff8efa14204f7a399a
mv %{SOURCE143} /builddir/.gerritcodereview/buck-cache/commons-collections-3.2.2.jar-8ad72fe39fa8c91eaaf12aadb21e0c3661fe26d5
mv %{SOURCE144} /builddir/.gerritcodereview/buck-cache/commons-dbcp-1.4-src.jar-62cbbdfaeca8e59d90399c75207c1cd5d456a7be
mv %{SOURCE145} /builddir/.gerritcodereview/buck-cache/commons-dbcp-1.4.jar-30be73c965cc990b153a100aaaaafcf239f82d39
mv %{SOURCE146} /builddir/.gerritcodereview/buck-cache/commons-io-1.4-src.jar-43a93031d20b4a5e71aca0286ac379876cfa51d7
mv %{SOURCE147} /builddir/.gerritcodereview/buck-cache/commons-io-1.4.jar-a8762d07e76cfde2395257a5da47ba7c1dbd3dce
mv %{SOURCE148} /builddir/.gerritcodereview/buck-cache/commons-lang-2.5-src.jar-c747750710c84726f7799a213ef2321b1e0c40d2
mv %{SOURCE149} /builddir/.gerritcodereview/buck-cache/commons-lang-2.5.jar-b0236b252e86419eef20c31a44579d2aee2f0a69
mv %{SOURCE150} /builddir/.gerritcodereview/buck-cache/commons-net-2.2-src.jar-c92796348df44278d586e39b17d56d55f94b73aa
mv %{SOURCE151} /builddir/.gerritcodereview/buck-cache/commons-net-2.2.jar-07993c12f63c78378f8c90de4bc2ee62daa7ca3a
mv %{SOURCE152} /builddir/.gerritcodereview/buck-cache/commons-pool-1.5.5.jar-7d8ffbdc47aa0c5a8afe5dc2aaf512f369f1d19b
mv %{SOURCE153} /builddir/.gerritcodereview/buck-cache/commons-validator-1.4.1-src.jar-9035eb023d24c9d86fe7d5f9baa99c5fdf9790a0
mv %{SOURCE154} /builddir/.gerritcodereview/buck-cache/commons-validator-1.4.1.jar-2231238e391057a53f92bde5bbc588622c1956c3
mv %{SOURCE155} /builddir/.gerritcodereview/buck-cache/automaton-1.11-8-src.jar-32ded3e2059c4b7ba77aee34075f991ccaa43224
mv %{SOURCE156} /builddir/.gerritcodereview/buck-cache/automaton-1.11-8.jar-6ebfa65eb431ff4b715a23be7a750cbc4cc96d0f
mv %{SOURCE157} /builddir/.gerritcodereview/buck-cache/mime-util-2.1.3.jar-0c9cfae15c74f62491d4f28def0dff1dabe52a47
mv %{SOURCE158} /builddir/.gerritcodereview/buck-cache/javax.inject-1-src.jar-ee28bc23e3202de7cdbdf4a9c11589ae37d6f401
mv %{SOURCE159} /builddir/.gerritcodereview/buck-cache/javax.inject-1.jar-6975da39a7040257bd51d21a231b76c915872d38
mv %{SOURCE160} /builddir/.gerritcodereview/buck-cache/validation-api-1.0.0.GA-src.jar-7a561191db2203550fbfa40d534d4997624cd369
mv %{SOURCE161} /builddir/.gerritcodereview/buck-cache/validation-api-1.0.0.GA.jar-b6bd7f9d78f6fdaa3c37dae18a4bd298915f328e
mv %{SOURCE162} /builddir/.gerritcodereview/buck-cache/joda-time-2.3-src.jar-4127e844731dd6f4a1f532232c9dbabf401ef5b5
mv %{SOURCE163} /builddir/.gerritcodereview/buck-cache/joda-time-2.3.jar-56498efd17752898cfcc3868c1b6211a07b12b8f
mv %{SOURCE164} /builddir/.gerritcodereview/buck-cache/log4j-1.2.17-src.jar-e93d50d4e7566a4fb6f31a5b6e6cd56bef7591dc
mv %{SOURCE165} /builddir/.gerritcodereview/buck-cache/log4j-1.2.17.jar-5af35056b4d257e4b64b9e8069c0746e8b08629f
mv %{SOURCE166} /builddir/.gerritcodereview/buck-cache/jitescript-0.4.0-src.jar-45a5ffec9d612d942919ad247d8653a4ea132992
mv %{SOURCE167} /builddir/.gerritcodereview/buck-cache/jitescript-0.4.0.jar-2e35862b0435c1b027a21f3d6eecbe50e6e08d54
mv %{SOURCE168} /builddir/.gerritcodereview/buck-cache/nekohtml-1.9.10.jar-14052461031a7054aa094f5573792feb6686d3de
mv %{SOURCE169} /builddir/.gerritcodereview/buck-cache/antlr-runtime-3.5.2-src.jar-e0858f3e5b0b35bbfac3067910fb458cad507910
mv %{SOURCE170} /builddir/.gerritcodereview/buck-cache/antlr-runtime-3.5.2.jar-cd9cd41361c155f3af0f653009dcecb08d8b4afd
mv %{SOURCE171} /builddir/.gerritcodereview/buck-cache/antlr-3.5.2-src.jar-92ffdf470ef14d1a10c787e70b2f61f50e902fe3
mv %{SOURCE172} /builddir/.gerritcodereview/buck-cache/antlr-3.5.2.jar-c4a65c950bfc3e7d04309c515b2177c00baf7764
mv %{SOURCE173} /builddir/.gerritcodereview/buck-cache/stringtemplate-4.0.2.jar-e28e09e2d44d60506a7bcb004d6c23ff35c6ac08
mv %{SOURCE174} /builddir/.gerritcodereview/buck-cache/commons-compress-1.7-src.jar-8a3633bf674f8435768c2a7639a323cec27e58ae
mv %{SOURCE175} /builddir/.gerritcodereview/buck-cache/commons-compress-1.7.jar-ab365c96ee9bc88adcc6fa40d185c8e15a31410d
mv %{SOURCE176} /builddir/.gerritcodereview/buck-cache/httpclient-4.3.4-src.jar-7a14aafed8c5e2c4e360a2c1abd1602efa768b1f
mv %{SOURCE177} /builddir/.gerritcodereview/buck-cache/httpclient-4.3.4.jar-a9a1fef2faefed639ee0d0fba5b3b8e4eb2ff2d8
mv %{SOURCE178} /builddir/.gerritcodereview/buck-cache/httpcore-4.3.2-src.jar-4809f38359edeea9487f747e09aa58ec8d3a54c5
mv %{SOURCE179} /builddir/.gerritcodereview/buck-cache/httpcore-4.3.2.jar-31fbbff1ddbf98f3aa7377c94d33b0447c646b6e
mv %{SOURCE180} /builddir/.gerritcodereview/buck-cache/httpmime-4.3.4-src.jar-0651e21152b0963661068f948d84ed08c18094f8
mv %{SOURCE181} /builddir/.gerritcodereview/buck-cache/httpmime-4.3.4.jar-54ffde537682aea984c22fbcf0106f21397c5f9b
mv %{SOURCE182} /builddir/.gerritcodereview/buck-cache/lucene-analyzers-common-4.10.2-src.jar-042c07de27089501b52460ffcc039792dff0cd42
mv %{SOURCE183} /builddir/.gerritcodereview/buck-cache/lucene-analyzers-common-4.10.2.jar-f977f8c443e8f4e9d1fd7fdfda80a6cf60b3e7c2
mv %{SOURCE184} /builddir/.gerritcodereview/buck-cache/lucene-core-4.10.2-src.jar-187a5d13a473a3b72e52071fa612421666fdb61d
mv %{SOURCE185} /builddir/.gerritcodereview/buck-cache/lucene-core-4.10.2.jar-c01e3d675d277e0a93e7890d03cc3246b2cdecaa
mv %{SOURCE186} /builddir/.gerritcodereview/buck-cache/lucene-queryparser-4.10.2-src.jar-908c90c56518d829679c7d6b5c599af2744ce3cf
mv %{SOURCE187} /builddir/.gerritcodereview/buck-cache/lucene-queryparser-4.10.2.jar-d70f54e1060d553ba7aeb4d49a71fd0c068499e8
mv %{SOURCE188} /builddir/.gerritcodereview/buck-cache/mina-core-2.0.8-src.jar-0ddcddbc2e8ebbc6061183d81151b58c1a0b22f2
mv %{SOURCE189} /builddir/.gerritcodereview/buck-cache/mina-core-2.0.8.jar-d6ff69fa049aeaecdf0c04cafbb1ab53b7487883
mv %{SOURCE190} /builddir/.gerritcodereview/buck-cache/solr-solrj-4.3.1-src.jar-fdc68976c7b41c4487bcccb6ffd7565bd893eecc
mv %{SOURCE191} /builddir/.gerritcodereview/buck-cache/solr-solrj-4.3.1.jar-433fe37796e67eaeb4452f69eb1fae2de27cb7a8
mv %{SOURCE192} /builddir/.gerritcodereview/buck-cache/sshd-core-0.14.0-src.jar-17fceec6f09fecf6072506dc707004e225440a9c
mv %{SOURCE193} /builddir/.gerritcodereview/buck-cache/sshd-core-0.14.0.jar-cb12fa1b1b07fb5ce3aa4f99b189743897bd4fca
mv %{SOURCE194} /builddir/.gerritcodereview/buck-cache/tomcat-servlet-api-8.0.5-src.jar-a31349e89a2266b551912e81bc8875fd56a19322
mv %{SOURCE195} /builddir/.gerritcodereview/buck-cache/tomcat-servlet-api-8.0.5.jar-9ef01afc25481b82aa8f3615db536869f2dc961e
mv %{SOURCE196} /builddir/.gerritcodereview/buck-cache/velocity-1.7-src.jar-4295172584ddbecb2b98bd8ec2689d1af1c2c876
mv %{SOURCE197} /builddir/.gerritcodereview/buck-cache/velocity-1.7.jar-2ceb567b8f3f21118ecdec129fe1271dbc09aa7a
mv %{SOURCE198} /builddir/.gerritcodereview/buck-cache/zookeeper-3.4.5-src.jar-aed5e40665a6111fefc801a688b0572da2e2d961
mv %{SOURCE199} /builddir/.gerritcodereview/buck-cache/zookeeper-3.4.5.jar-c0f69fb36526552a8f0bc548a6c33c49cf08e562
mv %{SOURCE200} /builddir/.gerritcodereview/buck-cache/asciidoctorj-1.5.0.jar-192df5660f72a0fb76966dcc64193b94fba65f99
mv %{SOURCE201} /builddir/.gerritcodereview/buck-cache/bcpg-jdk15on-1.51-src.jar-5a2fa52259ad6b5f561532ecfc697a6389c06909
mv %{SOURCE202} /builddir/.gerritcodereview/buck-cache/bcpg-jdk15on-1.51.jar-b5fa4c280dfbf8bf7c260bc1e78044c7a1de5133
mv %{SOURCE203} /builddir/.gerritcodereview/buck-cache/bcpkix-jdk15on-1.51-src.jar-0d88fb2a208218203dcee0a5f93c4718ab2b4f78
mv %{SOURCE204} /builddir/.gerritcodereview/buck-cache/bcpkix-jdk15on-1.51.jar-6c8c1f61bf27a09f9b1a8abc201523669bba9597
mv %{SOURCE205} /builddir/.gerritcodereview/buck-cache/bcprov-jdk15on-1.51-src.jar-dc47e31b9daae5798d903b5d03530401d6ce996c
mv %{SOURCE206} /builddir/.gerritcodereview/buck-cache/bcprov-jdk15on-1.51.jar-9ab8afcc2842d5ef06eb775a0a2b12783b99aa80
mv %{SOURCE207} /builddir/.gerritcodereview/buck-cache/jetty-continuation-9.2.9.v20150224-src.jar-7e33d7d43f5a7ae234bf5e6c8080e4e775cd3349
mv %{SOURCE208} /builddir/.gerritcodereview/buck-cache/jetty-continuation-9.2.9.v20150224.jar-476cae89c420170549b4851ed58dca25f349d16d
mv %{SOURCE209} /builddir/.gerritcodereview/buck-cache/jetty-http-9.2.9.v20150224-src.jar-80607ef1126e96bce593f3bd6d7813e51a114bf2
mv %{SOURCE210} /builddir/.gerritcodereview/buck-cache/jetty-http-9.2.9.v20150224.jar-8b30ddc8304df24a36efbfa267acc24b7403b692
mv %{SOURCE211} /builddir/.gerritcodereview/buck-cache/jetty-io-9.2.9.v20150224-src.jar-749c2971176cde374634f0965601798b4cdb32f2
mv %{SOURCE212} /builddir/.gerritcodereview/buck-cache/jetty-io-9.2.9.v20150224.jar-06a4a23ee9decf2762d052bc2ae0501c08cc9023
mv %{SOURCE213} /builddir/.gerritcodereview/buck-cache/jetty-jmx-9.2.9.v20150224-src.jar-5147deede3aad6963efd16c50e96ae4c4f921d60
mv %{SOURCE214} /builddir/.gerritcodereview/buck-cache/jetty-jmx-9.2.9.v20150224.jar-e0a9df505fbcc7c0481209325a106b922097468d
mv %{SOURCE215} /builddir/.gerritcodereview/buck-cache/jetty-security-9.2.9.v20150224-src.jar-c9831afcb3289ad8a7bcea3af46bf155f1d76fea
mv %{SOURCE216} /builddir/.gerritcodereview/buck-cache/jetty-security-9.2.9.v20150224.jar-1747a52b01afbf96b58b0ae0f352185560768fc2
mv %{SOURCE217} /builddir/.gerritcodereview/buck-cache/jetty-server-9.2.9.v20150224-src.jar-e64058a3bcfe9384e6c7ee672359a00611f11d78
mv %{SOURCE218} /builddir/.gerritcodereview/buck-cache/jetty-server-9.2.9.v20150224.jar-d30a52e992c3484569f58763f55097a1da3202ee
mv %{SOURCE219} /builddir/.gerritcodereview/buck-cache/jetty-servlet-9.2.9.v20150224-src.jar-a68cd9ea397e385de839f3e558b8fa1aa911038f
mv %{SOURCE220} /builddir/.gerritcodereview/buck-cache/jetty-servlet-9.2.9.v20150224.jar-1797875a3cc524d181733f323866a5f7bbca03a7
mv %{SOURCE221} /builddir/.gerritcodereview/buck-cache/jetty-util-9.2.9.v20150224-src.jar-2262f1cb24424490b16d14761dd37f2b7dee4697
mv %{SOURCE222} /builddir/.gerritcodereview/buck-cache/jetty-util-9.2.9.v20150224.jar-b5fb774a02158e9f66fed949581159a8d0dfcbe1
mv %{SOURCE223} /builddir/.gerritcodereview/buck-cache/org.eclipse.jgit.archive-4.0.1.201506240215-r-src.jar-da6c096dc0dd4968173f87d335bd609284b3ad06
mv %{SOURCE224} /builddir/.gerritcodereview/buck-cache/org.eclipse.jgit.archive-4.0.1.201506240215-r.jar-124e353f51adbbc1af12b143012cc1ebfa2c1012
mv %{SOURCE225} /builddir/.gerritcodereview/buck-cache/org.eclipse.jgit.http.server-4.0.1.201506240215-r-src.jar-5b1028efbd34a40c2b586963d34d757b71ea24d2
mv %{SOURCE226} /builddir/.gerritcodereview/buck-cache/org.eclipse.jgit.http.server-4.0.1.201506240215-r.jar-8c73719477224802eda2a2da65bce8946d0fac6f
mv %{SOURCE227} /builddir/.gerritcodereview/buck-cache/org.eclipse.jgit-4.0.1.201506240215-r-src.jar-c8ab3011612a4680791df394e2ef1ab8debeaed6
mv %{SOURCE228} /builddir/.gerritcodereview/buck-cache/org.eclipse.jgit-4.0.1.201506240215-r.jar-3bdf2d666df1a5373f7ad291c075ab1329560afd
mv %{SOURCE229} /builddir/.gerritcodereview/buck-cache/joda-convert-1.2-src.jar-781079f64587340e29602d70a005a9c3d64e62f9
mv %{SOURCE230} /builddir/.gerritcodereview/buck-cache/joda-convert-1.2.jar-35ec554f0cd00c956cc69051514d9488b1374dec
mv %{SOURCE231} /builddir/.gerritcodereview/buck-cache/jruby-complete-1.7.4.jar-74984d84846523bd7da49064679ed1ccf199e1db
mv %{SOURCE232} /builddir/.gerritcodereview/buck-cache/noggit-0.5-src.jar-6ff328a34f594e10e8268196052fb294bb48cd48
mv %{SOURCE233} /builddir/.gerritcodereview/buck-cache/noggit-0.5.jar-8e6e65624d2e09a30190c6434abe23b7d4e5413c
mv %{SOURCE234} /builddir/.gerritcodereview/buck-cache/openid4java-0.9.8-src.jar-0a277d188360027e813db6fd0143aca5d332e17b
mv %{SOURCE235} /builddir/.gerritcodereview/buck-cache/openid4java-0.9.8.jar-de4f1b33d3b0f0b2ab1d32834ec1190b39db4160
mv %{SOURCE236} /builddir/.gerritcodereview/buck-cache/asm-analysis-5.0.3-src.jar-01c6dc92b4a2d737f65de08b2193c433573ef334
mv %{SOURCE237} /builddir/.gerritcodereview/buck-cache/asm-analysis-5.0.3.jar-c7126aded0e8e13fed5f913559a0dd7b770a10f3
mv %{SOURCE238} /builddir/.gerritcodereview/buck-cache/asm-commons-5.0.3-src.jar-4548ec1f2efdddea1eeb520f84847c8c08e86aad
mv %{SOURCE239} /builddir/.gerritcodereview/buck-cache/asm-commons-5.0.3.jar-a7111830132c7f87d08fe48cb0ca07630f8cb91c
mv %{SOURCE240} /builddir/.gerritcodereview/buck-cache/asm-tree-5.0.3-src.jar-828bf786e7a9d70f28ac4f782c66215ce3fd44a4
mv %{SOURCE241} /builddir/.gerritcodereview/buck-cache/asm-tree-5.0.3.jar-287749b48ba7162fb67c93a026d690b29f410bed
mv %{SOURCE242} /builddir/.gerritcodereview/buck-cache/asm-util-5.0.3-src.jar-1fa5c89876166e884450ae527455a3a99e9da23d
mv %{SOURCE243} /builddir/.gerritcodereview/buck-cache/asm-util-5.0.3.jar-1512e5571325854b05fb1efce1db75fcced54389
mv %{SOURCE244} /builddir/.gerritcodereview/buck-cache/asm-5.0.3-src.jar-c7b0ec7061c88f6dc09875838ba74a887799dc33
mv %{SOURCE245} /builddir/.gerritcodereview/buck-cache/asm-5.0.3.jar-dcc2193db20e19e1feca8b1240dbbc4e190824fa
mv %{SOURCE246} /builddir/.gerritcodereview/buck-cache/pegdown-1.4.2-src.jar-661d602cd9314e205bc68d62018b2ddd872ca095
mv %{SOURCE247} /builddir/.gerritcodereview/buck-cache/pegdown-1.4.2.jar-d96db502ed832df867ff5d918f05b51ba3879ea7
mv %{SOURCE248} /builddir/.gerritcodereview/buck-cache/jcl-over-slf4j-1.7.7-src.jar-ff4a13177aa0613416530d55037d2fefe79919f6
mv %{SOURCE249} /builddir/.gerritcodereview/buck-cache/jcl-over-slf4j-1.7.7.jar-56003dcd0a31deea6391b9e2ef2f2dc90b205a92
mv %{SOURCE250} /builddir/.gerritcodereview/buck-cache/slf4j-api-1.7.7-src.jar-7e1bd53c9097ea359d7d34844a561281d677a3ad
mv %{SOURCE251} /builddir/.gerritcodereview/buck-cache/slf4j-api-1.7.7.jar-2b8019b6249bb05d81d3a3094e468753e2b21311
mv %{SOURCE252} /builddir/.gerritcodereview/buck-cache/slf4j-log4j12-1.7.7-src.jar-659c227738887ce10b5643316ad1730e1ec6c8fa
mv %{SOURCE253} /builddir/.gerritcodereview/buck-cache/slf4j-log4j12-1.7.7.jar-58f588119ffd1702c77ccab6acb54bfb41bed8bd
mv %{SOURCE254} /builddir/.gerritcodereview/buck-cache/xz-1.4.jar-18a9a2ce6abf32ea1b5fd31dae5210ad93f4e5e3
mv %{SOURCE255} /builddir/.gerritcodereview/buck-cache/codemirror-5.0.jar-24982be364be130fd7b2930c41f7203b63dbd86c
mv %{SOURCE256} /builddir/.gerritcodereview/buck-cache/oro-2.0.8.jar-5592374f834645c4ae250f4c9fbb314c9369d698
mv %{SOURCE257} /builddir/.gerritcodereview/buck-cache/postgresql-9.1-901-1.jdbc4.jar-9bfabe48876ec38f6cbaa6931bad05c64a9ea942
mv %{SOURCE258} /builddir/.gerritcodereview/buck-cache/xercesimpl-2.8.1.jar-25101e37ec0c907db6f0612cbf106ee519c1aef1

%build
# Patch git describe
sed -i "s/import subprocess/return 'v%{version}'/" tools/git.defs
sed -i "s/git describe HEAD/echo v%{version}/" tools/default.defs
buck build release
buck build plugins/avatars-gravatar
buck build plugins/delete-project
buck build plugins/reviewers-by-blame

%install
install -p -D -m 755 buck-out/gen/release.war %{buildroot}%{_libdir}/gerrit/release.war
# Gerrit needs lib with version number
install -p -D -m 755 buck-out/gen/lib/bouncycastle/bcprov/bcprov-jdk15on-1.51.jar %{buildroot}%{_libdir}/gerrit/lib/bcprov-jdk15on-1.51.jar
install -p -D -m 755 buck-out/gen/lib/bouncycastle/bcpkix/bcpkix-jdk15on-1.51.jar %{buildroot}%{_libdir}/gerrit/lib/bcpkix-jdk15on-1.51.jar
ln -s /usr/share/java/mysql-connector-java.jar %{buildroot}%{_libdir}/gerrit/lib/mysql-connector-java-5.1.21.jar

install -p -D -m 755 buck-out/gen/plugins/commit-message-length-validator/commit-message-length-validator.jar %{buildroot}%{_libdir}/gerrit/plugins/commit-message-length-validator.jar
install -p -D -m 755 buck-out/gen/plugins/download-commands/download-commands.jar %{buildroot}%{_libdir}/gerrit/plugins/download-commands.jar
install -p -D -m 755 buck-out/gen/plugins/replication/replication.jar %{buildroot}%{_libdir}/gerrit/plugins/replication.jar
install -p -D -m 755 buck-out/gen/plugins/reviewnotes/reviewnotes.jar %{buildroot}%{_libdir}/gerrit/plugins/reviewnotes.jar
install -p -D -m 755 buck-out/gen/plugins/singleusergroup/singleusergroup.jar %{buildroot}%{_libdir}/gerrit/plugins/singleusergroup.jar
install -p -D -m 755 buck-out/gen/plugins/avatars-gravatar/avatars-gravatar.jar %{buildroot}%{_libdir}/gerrit/plugins/avatars-gravatar.jar
install -p -D -m 755 buck-out/gen/plugins/delete-project/delete-project.jar %{buildroot}%{_libdir}/gerrit/plugins/delete-project.jar
install -p -D -m 755 buck-out/gen/plugins/reviewers-by-blame/reviewers-by-blame.jar %{buildroot}%{_libdir}/gerrit/plugins/reviewers-by-blame.jar

install -p -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/gerrit.service

install -d -m 755 %{buildroot}%{_sysconfdir}/sysconfig/
echo "GERRIT_HEAP_LIMIT=2g" > %{buildroot}%{_sysconfdir}/sysconfig/gerrit
install -d -m 755 %{buildroot}%{_sysconfdir}/gerrit
install -d -m 750 %{buildroot}%{_localstatedir}/log/gerrit

install -d -m 755 %{buildroot}%{_sharedstatedir}/gerrit/
install -d -m 755 %{buildroot}%{_sharedstatedir}/gerrit/hooks
ln -s /usr/lib64/gerrit/ %{buildroot}%{_sharedstatedir}/gerrit/bin
ln -s /usr/lib64/gerrit/plugins/ %{buildroot}%{_sharedstatedir}/gerrit/plugins
ln -s %{_localstatedir}/log/gerrit/ %{buildroot}%{_sharedstatedir}/gerrit/logs
ln -s /usr/lib64/gerrit/lib/ %{buildroot}%{_sharedstatedir}/gerrit/lib
ln -s /etc/gerrit/ %{buildroot}%{_sharedstatedir}/gerrit/etc

%pre
# Create users
getent group gerrit >/dev/null || groupadd -r gerrit
getent passwd gerrit > /dev/null || useradd -r -g gerrit \
    -d %{_sharedstatedir}/gerrit -s /sbin/nologin \
    -c "Gerrit service account" gerrit
exit 0

%post
%systemd_post gerrit.service

%preun
%systemd_preun gerrit.service

%files
%{_libdir}/gerrit/release.war
%{_libdir}/gerrit/lib/
%dir %{_libdir}/gerrit/plugins
%{_sysconfdir}/gerrit
%{_sysconfdir}/sysconfig/gerrit
%{_unitdir}/gerrit.service
%attr(0750,gerrit,gerrit) %dir %{_localstatedir}/log/gerrit
%attr(0755,gerrit,gerrit) %dir %{_sharedstatedir}/gerrit
%attr(0755,gerrit,gerrit) %dir %{_sysconfdir}/gerrit
%{_sharedstatedir}/gerrit/*

%files plugin-commit-message-length-validator
%{_libdir}/gerrit/plugins/commit-message-length-validator.jar

%files plugin-download-commands
%{_libdir}/gerrit/plugins/download-commands.jar

%files plugin-replication
%{_libdir}/gerrit/plugins/replication.jar

%files plugin-reviewnotes
%{_libdir}/gerrit/plugins/reviewnotes.jar

%files plugin-singleusergroup
%{_libdir}/gerrit/plugins/singleusergroup.jar

%files plugin-avatars-gravatar
%{_libdir}/gerrit/plugins/avatars-gravatar.jar

%files plugin-delete-project
%{_libdir}/gerrit/plugins/delete-project.jar

%files plugin-reviewers-by-blame
%{_libdir}/gerrit/plugins/reviewers-by-blame.jar

%changelog
* Fri Feb 23 2018 Fabien Boucher <fboucher@redhat.com> 2.11.10-3
- Bump JSCH to 0.1.54

* Thu Apr 27 2017 Fabien Boucher <fboucher@redhat.com> 2.11.10-2
- Change gerrit.service mode to 644

* Sun Dec 04 2016 Tristan Cacqueray <tdecacqu@redhat.com> 1.0.2-1
- First (dirty) package
