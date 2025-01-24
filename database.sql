CREATE TABLE company(
    id INT PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(50) NOT NULL UNIQUE,
    last_refreshed TIMESTAMP NOT NULL,
    intervaltime VARCHAR(20) NOT NULL,
    output_size VARCHAR(20) NOT NULL,
    time_zone TIME VARCHAR(50) NOT NULL
);

CREATE TABLE stock_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    timestampp TIMESTAMP NOT NULL,
    open_price DECIMAL(10,4) NOT NULL,
    high_price DECIMAL(10,4) NOT NULL,
    low_price DECIMAL(10,4) NOT NULL,
    close_price DECIMAL(10,4) NOT NULL,
    volume INT NOT NULL,
    company_id INT,
    FOREIGN KEY(company_id) REFERENCES company (id)
);

