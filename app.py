
from flask import Flask
import pymssql

app = Flask(__name__)

# Replace with your SQL Server credentials and details
server = 'devsqlserverfortesting.database.windows.net'
database = 'acctest-db-d'
username = '4dm1n157r470r'
password = '4-v3ry-53cr37-p455w0rd'

conn = pymssql.connect(server=server, database=database, user=username, password=password)

@app.route('/')
def test_connection():
    try:
        with conn.cursor() as cursor:
            cursor.execute('SELECT 1')
            result = cursor.fetchone()
            return "Connection to SQL Server successful!"
    except Exception as e:
        return f"Connection to SQL Server failed. Error: {str(e)}"
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)
