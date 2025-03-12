import sqlite3

def get_connection():
    connection = sqlite3.connect('QLSinhVien.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()
        
def read_database_version():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        select_query = """select * from Lop"""
        cursor.execute(select_query)
        
        record = cursor.fetchall()
        
        print(f"Danh sách của các lớp là: ")
        for row in record:
            print("*"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])
            
        close_connection(connection)
    except (Exception, sqlite3.Error) as error:
        print("Đã có lỗi xảy ra. Thông tin lỗi: ", error)

read_database_version()