DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS quizzes;
DROP TABLE IF EXISTS quiz_results;

CREATE TABLE students (
   student_id INTEGER PRIMARY KEY,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);

CREATE TABLE quizzes (
   quiz_id INTEGER PRIMARY KEY NOT NULL,
   subject TEXT NOT NULL,
   questions INTEGER,
   quiz_date TEXT NOT NULL
);

CREATE TABLE quiz_results (
   student_id INT NOT NULL,
   quizzes_id INT NOT NULL,
   score INT NOT NULL
);

INSERT INTO quizzes (quiz_id, subject, questions, quiz_date) VALUES
(1, 'Python Basics', 5, '2015-05-02');

INSERT INTO students (student_id, first_name, last_name) VALUES
(1, 'John', 'Smith');

INSERT INTO quiz_results (score, quizzes_id, student_id) VALUES
(85, 1, 1);
