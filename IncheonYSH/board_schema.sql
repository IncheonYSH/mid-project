CREATE TABLE `users` (
  `username` varchar(30) PRIMARY KEY NOT NULL
);

CREATE TABLE `board` (
  `article_number` int PRIMARY KEY AUTO_INCREMENT,
  `username` varchar(30),
  `title` varchar(35),
  `maintext` text,
  `time` timestamp
);

CREATE TABLE `reply` (
  `reply_number` int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `article_number` int NOT NULL,
  `replyreply_number` int,
  `username` varchar(30),
  `reply` varchar(500),
  `time` timestamp
);

ALTER TABLE `board` ADD FOREIGN KEY (`username`) REFERENCES `users` (`username`);

ALTER TABLE `reply` ADD FOREIGN KEY (`article_number`) REFERENCES `board` (`article_number`);

ALTER TABLE `reply` ADD FOREIGN KEY (`username`) REFERENCES `users` (`username`);
