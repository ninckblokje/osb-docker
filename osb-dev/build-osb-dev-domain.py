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

import os
  
print("Creating OSB development domain")

oracleHome = '/u01/oracle/fmw_osb'
commonComponentsHome = oracleHome + '/oracle_common'
domainHome = oracleHome + '/user_projects/domains/OsbDevDomain'
osbHome = oracleHome + '/osb'

templateFile = oracleHome + '/wlserver/common/templates/wls/wls.jar'
serverName = 'AdminServer'
domainAdminUser = 'weblogic'
domainAdminPassword = 'Welcome01'
listenAddress = ''
listenPort = '7001'
sslListenPort = '7002'
cfgGrpProfile = 'Compact'

# Reading domain template
print("[progress] Reading template: " + templateFile);
readTemplate(templateFile, cfgGrpProfile)

# Configuring domain
cd('Servers/AdminServer')

print('Setting Name to \'' + serverName + '\'')
set('Name', serverName)

print('Setting ListenAddress to \'' + listenAddress + '\'')
set('ListenAddress', listenAddress)

print('Setting ListenPort to ' + listenPort)
set('ListenPort', int(listenPort))

set('TunnelingEnabled', 1)

cd('/Servers/' + serverName)
create (serverName, 'SSL')
cd('SSL/' + serverName)

print('Enabling SSL using port ' + sslListenPort)
set('Enabled' , 'true')
set('ListenPort', int(sslListenPort))

set('ClientCertificateEnforced', 'false')
set('TwoWaySSLEnabled', 'true')

cd('/')
cd('Security/base_domain/User/weblogic')

print('Setting domain administrator to \'' + domainAdminUser + '\'')
cmo.setName(domainAdminUser)

print('Setting domain password.')
cmo.setPassword(domainAdminPassword)

# Save domain
setOption('OverwriteDomain', 'true')

print("[progress] Writing domain: " + domainHome);
writeDomain(domainHome)

print("[progress] Closing template.")
closeTemplate()

# Set environment variables
os.putenv('COMMON_COMPONENTS_HOME', commonComponentsHome)
os.putenv('DOMAIN_HOME', domainHome)

# Extend the domain with templates
templates = \
[
  commonComponentsHome + "/common/templates/wls/oracle.jrf_template_12.1.3.jar",
  commonComponentsHome + "/common/templates/wls/oracle.wsmpm_template_12.1.3.jar",
  osbHome + "/common/templates/wls/oracle.osb_template_12.1.3.jar"
]

if len(templates) > 0:
  print("[progress] Reading domain: " + domainHome)
  readDomain(domainHome);

  for t in templates:
    print("[progress] Adding domain extension template: " + t)
    addTemplate(t)
    print("[progress] Updating domain.")
    updateDomain()

  print("[progress] Closing domain.")
  closeDomain()
  
print("*** Domain processing complete ***");  
  
exit()
