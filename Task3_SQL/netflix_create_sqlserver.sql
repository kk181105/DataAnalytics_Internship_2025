
IF OBJECT_ID('dbo.netflix','U') IS NOT NULL
    DROP TABLE dbo.netflix;
GO

CREATE TABLE dbo.netflix (
    show_id        NVARCHAR(100) PRIMARY KEY,
    content_type   NVARCHAR(50),
    title          NVARCHAR(500),
    director       NVARCHAR(1000),
    cast_list      NVARCHAR(MAX),
    country        NVARCHAR(500),
    date_added_raw NVARCHAR(100),
    date_added     DATE NULL,
    release_year   INT NULL,
    rating         NVARCHAR(50),
    duration_raw   NVARCHAR(100),
    duration_min   INT NULL,
    listed_in      NVARCHAR(1000),
    description    NVARCHAR(MAX)
);
GO
