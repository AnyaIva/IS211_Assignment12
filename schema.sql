DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS quizzes;
DROP TABLE IF EXISTS quiz_results;

CREATE TABLE students (
   id INTEGER PRIMARY KEY,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);

CREATE TABLE quizzes (
   id INTEGER PRIMARY KEY NOT NULL,
   subject TEXT NOT NULL,
   questions INTEGER,
   quiz_date TEXT NOT NULL
);

CREATE TABLE quiz_results (
   student_id INT NOT NULL,
   quizzes_id INT NOT NULL,
   score INT NOT NULL
);
