CREATE TABLE user ( 
  firstname VARCHAR(100) NOT NULL, 
  lastname VARCHAR(100) NOT NULL 
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO user VALUES (
  'hiroshi', 
  'abe'
);