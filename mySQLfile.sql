
CREATE TABLE IF NOT EXISTS usrs (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
surname text NOT NULL,
feedback text NOT NULL,
time integer NOT NULL
);