CREATE TABLE staging.stg_posts (
    userId INT,
    id INT,
    title NVARCHAR(200),
    body NVARCHAR(MAX)
);

select * from staging.stg_posts