import express from "express";
import mysql from 'mysql';


const app = express();
app.use(express.json());

const db = mysql.createConnection({
    user : 'root',
    password : 'gsv.092465',
    host : 'localhost',
    database : 'sys'
})

db.connect();



app.listen(3000, () =>
  console.log('Example app listening on port 3000!'),
);

app.get('/data', (req,res) => {
    const result = db.query('SELECT * FROM SensorGrades ORDER BY idSensorGrades DESC LIMIT 1', function(error,results,fields){
        if (error) throw error;
        res.send(results)
    });
})
