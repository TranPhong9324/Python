
import pyodbc

conn = pyodbc.connect('DRIVER={SQL Server};SERVER=DESKTOP-LL7P35M\\SQLEXPRESS;DATABASE=QLMonAn;UID=sa;PWD=sa;Encrypt=no')
cursor =  conn.cursor
cursor.execute("Select @@version")
conn.close()
db_version = cursor.fetchone()
print("Bạn đang dùng hệ quản trị CSDL SQL server phiên bản: ",db_version)
