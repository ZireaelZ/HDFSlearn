import  happybase
connection = happybase.Connection('192.168.112.128',port=9090,timeout=5000)
# before first use:
connection.open()
# connection.create_table('users',{'cf1': dict()})
table=connection.table('users')
print(table)
connection.close()