const express = require('express');
const app = express();
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://admin:adminpassword@mongo_service:27017/';
const dbName = 'assignment_1';

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  MongoClient.connect(url, { useNewUrlParser: true }, (err, client) => {
    if (err) throw err;
    const db = client.db(dbName);
    const collection = db.collection('student_grades');

    collection.find({}).toArray((err, grades) => {
      if (err) throw err;

      const minimum_grade = grades.find(grade => grade.hasOwnProperty('Minimum Grade'))['Minimum Grade'];
      const maximum_grade = grades.find(grade => grade.hasOwnProperty('Maximum Grade'))['Maximum Grade'];
      const average_grade = grades.find(grade => grade.hasOwnProperty('Average Grade'))['Average Grade'];

      client.close();

      res.render('index', {
        students: [
          {
            minimum_grade: minimum_grade,
            maximum_grade: maximum_grade,
            average_grade: average_grade,
          },
        ],
      });
    });
  });
});

app.listen(5006, () => {
  console.log('Server started on port 5006');
});