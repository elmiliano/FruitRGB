import express from "express";
import { Int } from "mssql";
import mysql from 'mysql';

const app = express(); // define express server
app.use(express.json());

const db = mysql.createConnection({ // connect to MySQL DB
    user : 'app_usr',
    password : '7@Rvopcpwc',
    host : 'localhost',
    database : 'sys'
})

db.connect();

app.listen(3000, () => // begin listen
  console.log('Example app listening on port 3000!'),
);

app.get('/data', (req,res) => { // return most recent DB SensorGrades table entry
    const result = db.query('SELECT * FROM SensorGrades ORDER BY idSensorGrades DESC LIMIT 1', (error,results,fields)=>{
        if (error) throw error;
        res.send(results)
    });
})

app.post('/id?', (req,res) => {
    const parameters = {id: req.body.id_value}
    const result = db.query('SELECT * FROM SensorGrades WHERE idSensorGrades = ?', parameters[id] ,(error, results, fields) => {
        if(error) throw error;
        res.send(results)
    });
});

