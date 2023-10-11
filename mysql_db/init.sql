USE analytics_data;

CREATE TABLE student_grades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(255),   
    student_id VARCHAR(100),         
    course VARCHAR(255),         
    grade DECIMAL(5,2)           
);