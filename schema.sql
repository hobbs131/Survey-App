drop table survey_responses;

create table survey_responses (
  id SERIAL PRIMARY KEY,
  input varchar(255),
  radio_button varchar(255),
  select_box varchar(255),
  checkbox varchar(255),
  ts TIMESTAMPTZ
);
