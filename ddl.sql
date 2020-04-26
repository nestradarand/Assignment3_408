CREATE TABLE auth_user_2
(
	id INT auto_increment
		PRIMARY KEY,
	password VARCHAR(128) NOT NULL,
	last_login DATETIME(6) null,
	is_superuser TINYINT(1) NOT NULL,
	username VARCHAR(150) NOT NULL,
	first_name VARCHAR(30) NOT NULL,
	last_name VARCHAR(150) NOT NULL,
	email VARCHAR(254) NOT NULL,
	is_staff TINYINT(1) NOT NULL,
	is_active TINYINT(1) NOT NULL,
	date_joined DATETIME(6) NOT NULL,
	constraint username
		unique (username)
);

CREATE TABLE Sports(
    SportId INTEGER PRIMARY KEY AUTO_INCREMENT,
    Sport VARCHAR(32) UNIQUE
);
INSERT INTO Sports(Sport)
VALUE ('Baseball');
INSERT INTO Sports(Sport)
VALUE ('Basketball');
INSERT INTO Sports(Sport)
VALUE ('Hockey');
INSERT INTO Sports(Sport)
VALUE ('Football');
INSERT INTO Sports(Sport)
VALUE ('Horses');
INSERT INTO Sports(Sport)
VALUE ('Casino');
INSERT INTO Sports(Sport)
VALUE ('Other');

CREATE TABLE Transactions(
    TransactionId INTEGER PRIMARY KEY AUTO_INCREMENT,
    UserId INTEGER NOT NULL,
    Description VARCHAR(40) DEFAULT NULL,
    SportId INTEGER NOT NULL,
    Success BOOLEAN DEFAULT NULL,
    DateDeleted DATETIME DEFAULT NULL,
    FOREIGN KEY(UserId) REFERENCES Chapman_2.auth_user(id),
    FOREIGN KEY (SportID) REFERENCES Chapman_2.Sports(SportId)
);

CREATE TABLE Dates(
    TransactionId INTEGER UNIQUE NOT NULL,
    DateRecorded DATETIME NOT NULL,
    DateFinished DATETIME DEFAULT NULL,
    FOREIGN KEY(TransactionId) REFERENCES Transactions(TransactionId)
);

CREATE TABLE Spent(
    TransactionId INTEGER UNIQUE NOT NULL,
    Amount FLOAT(12,2) NOT NULL,
    FOREIGN KEY(TransactionId) REFERENCES Transactions(TransactionId)
);

CREATE PROCEDURE `Insert_New_Bet`(
    IN curr_user_id INTEGER,
    IN new_spend FLOAT(12,2),
    IN new_sport VARCHAR(20),
    IN win_status BOOLEAN,
    IN recorded_date DATETIME,
    IN ended_date DATETIME,
    IN new_description VARCHAR(40)
)
BEGIN
    START TRANSACTION;
        INSERT INTO Transactions(UserId, Description, SportId, Success)
        VALUES(curr_user_id,new_description,(SELECT DISTINCT(SportId) FROM Sports WHERE Sport = new_sport),win_status);
        SELECT @recent_insert:= last_insert_id();

        INSERT INTO Spent(TransactionId, Amount)
        VALUES(@recent_insert,new_spend);

        INSERT INTO Dates(Transactionid, Daterecorded, Datefinished)
        VALUES(@recent_insert,recorded_date,ended_date);
    COMMIT;
END


