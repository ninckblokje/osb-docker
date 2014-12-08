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

FROM centos:centos6

MAINTAINER ninckblokje

RUN groupadd dba
RUN useradd -d /home/oracle -g dba -G wheel -m -s /bin/bash oracle

RUN mkdir -p /tmp/software

ADD jdk-7u67-linux-x64.rpm /tmp/software/jdk-7u67-linux-x64.rpm

ADD fmw_12.1.3.0.0_wls.jar /tmp/software/fmw_12.1.3.0.0_wls.jar
ADD oraInst.loc /tmp/software/oraInst.loc
ADD wls.install.file /tmp/software/wls.install.file

ADD fmw_12.1.3.0.0_infrastructure.jar /tmp/software/fmw_12.1.3.0.0_infrastructure.jar
ADD infrastructure.install.file /tmp/software/infrastructure.install.file

ADD fmw_12.1.3.0.0_osb.jar /tmp/software/fmw_12.1.3.0.0_osb.jar
ADD osb.install.file /tmp/software/osb.install.file

RUN rpm -ivh /tmp/software/jdk-7u67-linux-x64.rpm
RUN rm /tmp/software/jdk-7u67-linux-x64.rpm

RUN mkdir -p /u01/oracle
RUN chown -R oracle:dba /u01/oracle

RUN chown -R oracle:dba /tmp/software

USER oracle

ENV JAVA_HOME /usr/java/jdk1.7.0_67
ENV ORACLE_HOME /u01/oracle/fmw_osb

RUN $JAVA_HOME/bin/java -jar /tmp/software/fmw_12.1.3.0.0_wls.jar -silent -responseFile /tmp/software/wls.install.file -invPtrLoc /tmp/software/oraInst.loc -jreLoc $JAVA_HOME
RUN rm /tmp/software/fmw_12.1.3.0.0_wls.jar

RUN $JAVA_HOME/bin/java -jar /tmp/software/fmw_12.1.3.0.0_infrastructure.jar -silent -responseFile /tmp/software/infrastructure.install.file -invPtrLoc /tmp/software/oraInst.loc -jreLoc $JAVA_HOME
RUN rm /tmp/software/fmw_12.1.3.0.0_infrastructure.jar

RUN $JAVA_HOME/bin/java -jar /tmp/software/fmw_12.1.3.0.0_osb.jar -silent -responseFile /tmp/software/osb.install.file -invPtrLoc /tmp/software/oraInst.loc -jreLoc $JAVA_HOME
RUN rm /tmp/software/fmw_12.1.3.0.0_osb.jar

