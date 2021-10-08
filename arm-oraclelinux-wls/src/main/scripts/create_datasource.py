# Copyright (c) 2021, Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.

connect('weblogic','gumby1234','t3://ejb1024010-ejb102401rg-ejb102401.eastus.cloudapp.azure.com:7001')
edit("Edwards-MacBook-Pro.local")
startEdit()
cd('/')
try:
  cmo.createJDBCSystemResource('postgreSQL-0')
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0')
  cmo.setName('postgreSQL-0')
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0/JDBCDataSourceParams/postgreSQL-0')
  set('JNDINames',jarray.array([String('jndi/postgreSQL-0')], String))
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0')
  cmo.setDatasourceType('GENERIC')
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0/JDBCDriverParams/postgreSQL-0')
  cmo.setUrl('jdbc:postgresql://20191015postgresql.postgres.database.azure.com:5432/wls20191015?sslmode=require')
  cmo.setDriverName('org.postgresql.Driver')
  cmo.setPassword('wlsEng@2019')
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0/JDBCConnectionPoolParams/postgreSQL-0')
  cmo.setTestTableName('SQL ISVALID\r\n\r\n\r\n\r\n')
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0/JDBCDriverParams/postgreSQL-0/Properties/postgreSQL-0')
  cmo.createProperty('user')
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0/JDBCDriverParams/postgreSQL-0/Properties/postgreSQL-0/Properties/user')
  cmo.setValue('weblogic@20191015postgresql')
  cd('/JDBCSystemResources/postgreSQL-0/JDBCResource/postgreSQL-0/JDBCDataSourceParams/postgreSQL-0')
  cmo.setGlobalTransactionsProtocol('EmulateTwoPhaseCommit')
  cd('/JDBCSystemResources/postgreSQL-0')
  set('Targets',jarray.array([ObjectName('com.bea:Name=cluster1,Type=Cluster')], ObjectName))
  save()
  resolve()
  activate()
except Exception, e:
  print "Already datasource with name postgreSQL-0 exists"
destroyEditSession("Edwards-MacBook-Pro.local",force = true)
disconnect()
