-- creates a table called first_table in the current database.
-- If the table already exists, it will not fail.

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
