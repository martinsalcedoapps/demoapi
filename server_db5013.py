#encoding: utf-8
import os

port = 5013
db_user = 'odoo13'
db_pass = 'odoo13'
localpath = os.path.abspath(".")

print("PREPARING DOCKER DB SERVER")
print("PORT: ", port)

cmd  = "docker run --name db%s " %(port)
cmd += "-e POSTGRES_USER=%s " %(db_user)
cmd += "-e POSTGRES_PASSWORD=%s " %(db_pass)
cmd += "-e POSTGRES_DB=postgres "
cmd += "-e PGDATA=/mnt/postgres "
cmd += "-v %s/postgres/:/mnt/postgres/ " %(localpath)
cmd += "-p %s:5432 " %(port)
cmd += "--restart=always "
cmd += "-d postgres:10 "

print(cmd)
os.system(cmd)
