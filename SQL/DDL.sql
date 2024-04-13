
CREATE TABLE equipment (
    equipment_id integer NOT NULL,
    status integer
);

CREATE TABLE members (
    memberid integer NOT NULL,
    name character varying(255),
    email character varying(255),
    password character varying(255),
    fitnessgoals text,
    healthmetrics text
);

CREATE TABLE payment (
    bill_id integer NOT NULL,
    member_id integer,
    amount integer,
    paid integer
);

CREATE TABLE roombookings (
    bookingid integer NOT NULL,
    roomid integer,
    bookingdate date,
    starttime time without time zone,
    endtime time without time zone
);

CREATE TABLE rooms (
    roomid integer NOT NULL,
    roomname character varying(255),
    capacity integer
);

CREATE TABLE sessionbooking (
    session_id integer NOT NULL,
    member_id integer,
    trainer_id integer,
    booking_date date,
    start_time time without time zone,
    end_time time without time zone,
    "group" integer
);

CREATE TABLE traineravailability (
    trainerid integer NOT NULL,
    availabledate date NOT NULL,
    starttime time without time zone NOT NULL,
    endtime time without time zone
);

CREATE TABLE trainers (
    trainerid integer NOT NULL,
    name character varying(255)
);