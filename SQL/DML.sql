

INSERT INTO members (memberid, name, email, password, fitnessgoals, healthmetrics) VALUES 
(1, 'Alex', '11@gmail.com', '11', '70kg', '11'),
(2, 'Sam', '12@gmail.com', '23', '50kg', '123'),
(3, 'Sara', '32@gmail.com', '23', '60kg', '32'),
(4, 'Test', '55@gmail.com', '55', '55kg', '55');

INSERT INTO equipment (equipment_id, status) VALUES 
(1, 1);

INSERT INTO payment (bill_id, member_id, amount, paid) VALUES 
(1, 7, 80, 0);

INSERT INTO roombookings (bookingid, roomid, bokingdate, starttime, endtime) VALUES 
(1, 1, '2012-02-02', '10:00:00', '15:00:00');

INSERT INTO rooms (roomid, roomname, capacity) VALUES 
(1, 'Yoga', NULL);

INSERT INTO sessionbooking (session_id, member_id, trainer_id, booking_date, start_time, end_time, group) VALUES 
(2, 1, 1, '2020-02-01', '11:00:00', '11:59:00', 1),
(3, 3, 1, '2020-02-02', '10:00:00', '10:10:00', 1),
(1, 1, 1, '2020-02-01', '11:00:00', '11:59:00', 1),
(4, 7, 1, '2023-02-02', '01:00:00', '02:00:00', 1);

INSERT INTO traineravailability (trainerid, availabledate, starttime, endtime) VALUES 
(1, '2023-02-02', '00:00:00', '23:00:00'),
(1, '2020-02-02', '10:00:00', '12:00:00');

INSERT INTO trainers (trainerid, name) VALUES 
(1, 'Alex Sam');