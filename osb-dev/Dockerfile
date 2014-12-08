# Copyright (c) 2014, ninckblokje
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

FROM ninckblokje/osb-base:12.1.3

MAINTAINER ninckblokje

USER root

ADD build-osb-dev-domain.py /tmp/software/build-osb-dev-domain.py
RUN chown -R oracle:dba /tmp/software

USER oracle

ENV JAVA_HOME /usr/java/jdk1.7.0_67
ENV ORACLE_HOME /u01/oracle/fmw_osb

RUN mkdir -p /u01/oracle/fmw_osb/user_projects/domains

RUN $ORACLE_HOME/wlserver/common/bin/wlst.sh /tmp/software/build-osb-dev-domain.py

EXPOSE 7001
EXPOSE 7002
EXPOSE 7453

ENTRYPOINT /u01/oracle/fmw_osb/domains/OsbDevDomain/bin/startWebLogic.sh > /u01/oracle/fmw_osb/domains/OsbDevDomain/servers/AdminServer/AdminServer.out 2>&1
