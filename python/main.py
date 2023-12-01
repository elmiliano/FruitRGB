
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


def process_rgb(value):
    rgb_list = value.split(',')
    rounded_rgb = [str(round(int(x) / 10) * 10) for x in rgb_list]
    rounded_rgb = ', '.join(map(str, rounded_rgb))
    return rounded_rgb

def calculate_rgb_average(series):
    avg_r, avg_g, avg_b = 0, 0, 0
    total_items = len(series)

    for item in series:
        r, g, b = map(int, item.split(','))
        avg_r += r
        avg_g += g
        avg_b += b

    avg_r /= total_items
    avg_g /= total_items
    avg_b /= total_items

    return [int(avg_r), int(avg_g), int(avg_b)]


def main():
    server = Server()
    server.up()
    try:
        while True:      
            server.connect()
            server.clientthread()
            server.handlebyte()
            res = pd.Series(server.messages)
            res = res.apply(process_rgb)
            print(res)
            mode = res.mode()[0]
            mode = mode.split(',')
            result = [int(i) for i in mode]
            #result = calculate_rgb_average(res)
            rgb = RGB(result[0], result[1], result[2])
            rgb.evaluate_banana()
            data = rgb.dictgrade()
            print(data)
            result = pool.execute('''INSERT INTO SensorGrades (r, g, b, maturity_level, char_level, moment)
                                    VALUES (%s, %s, %s, %s, %s, %s)''', 
                                (data['R'], 
                                data['G'], 
                                data['B'], 
                                data['Grade'], 
                                data['Maturity'], 
                                data['Moment']))
            conn.commit()
            server.messages = []
    except KeyboardInterrupt:
        print("Closing the program...")
        server.server.close()
        conn.close()    
        print("Program closed.")


main()