import cx_Oracle

dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid="ORCL")

conn = cx_Oracle.connect(user='rm97100', password='fiap23',dsn=dsn)

cursor = conn.cursor()



cursor.close()
conn.clone()