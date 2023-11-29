import datetime 
import mysql.connector
from server import Server
from rgb import RGB
import pandas as pd


conn = mysql.connector.connect(
    user = 'root',
    password = 'gsv.092465',
    host = 'localhost',
    database = 'sys'
)

pool = conn.cursor()

now = datetime.datetime.today()
f = '%Y-%m-%d %H:%M:%S'
now = now.strftime(f)


def main():
    server = Server()
    server.up()
    while True:
        server.connect()
        server.clientthread()
    res = pd.Series(server.handlebyte())
    mode = res.mode()[0]
    mode.split(',')
    result = [int(i) for i in result]
    rgb = RGB(result[0],result[1],result[2])
    rgb.evaluate()
    data = rgb.dictgrade()
    result = pool.execute(f'''INSERT INTO SensorGrades (r, g, b, maturity_level, char_level, moment) VALUES (%s, %s, %s, %s, %s, %s)''', 
                          (data['R'], 
                           data['G'], 
                           data['B'], 
                           data['Grade'], 
                           data['Maturity'], 
                           data['Moment']))
    conn.commit()


main()