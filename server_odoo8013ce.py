#encoding: utf-8

import os
port = 8013
name = 'odoo13ce'
dblink = 'db5013'
localpsth = os.path.abspath(".")

print("STOP DOCKER CONTAINER")
os.system("docker stop %s" %(name))

print("REMOVE DOCKER CONTAINER")
os.system("docker rm %s" %(name))

cmd  = "docker run "
cmd += '--name %s ' %(name)
cmd += '-v %s/odoo13ce.conf:/etc/odoo/odoo.conf ' %(localpsth)
cmd += '-v %s/var_lib_odoo:/var/lib/odoo ' %(localpsth)
cmd += '-v %s/extra-addons:/mnt/extra-addons ' %(localpsth)

cmd += '-p %s:8069 ' %(port)
cmd += '--link %s:db ' %(dblink)
cmd += '-t odoo:13.0 '

vcmd = cmd
vcmd = vcmd.replace("-v","\n-v")
vcmd = vcmd.replace("-p","\n-p")
print(vcmd)
os.system(cmd)

