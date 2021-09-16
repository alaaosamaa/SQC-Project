import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS SQC")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mysql",
    database="SQC"
)
mycursor = mydb.cursor()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Analyzer (analyzer_code INT NOT NULL, analyzer_name VARCHAR(255), anlyzer_input VARCHAR(255), analyzer_output VARCHAR(255), PRIMARY KEY(analyzer_code), UNIQUE(analyzer_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Test (test_code INT NOT NULL, test_name VARCHAR(255), test_group VARCHAR(255), test_date DATE, test_linear_range INT, test_measuring_unit VARCHAR(255), PRIMARY KEY(test_code), UNIQUE(test_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Reagents (reagent_lot_number INT NOT NULL, reagent_name VARCHAR(255), reagent_expiry_date DATE, PRIMARY KEY(reagent_lot_number), UNIQUE(reagent_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS QC_Lot (qc_lot_number INT NOT NULL, qc_name VARCHAR(255), qc_level VARCHAR(255), qc_low_limit INT, qc_high_limit INT, qc_target_mean INT, qc_target_sd INT, PRIMARY KEY(qc_lot_number), UNIQUE(qc_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS QC_Results (qc_result_code INT NOT NULL, test_code INT NOT NULL, qc_lot_number INT NOT NULL, qc_result_mean INT, qc_result_sd INT, PRIMARY KEY(qc_result_code), FOREIGN KEY (test_code) REFERENCES Test(test_code), FOREIGN KEY (qc_lot_number) REFERENCES QC_Lot(qc_lot_number))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS analyzer_test (analyzer_code INT NOT NULL, test_code INT NOT NULL, reagent_lot_number INT NOT NULL, FOREIGN KEY (analyzer_code) REFERENCES Analyzer(analyzer_code), FOREIGN KEY (test_code) REFERENCES Test(test_code), FOREIGN KEY (reagent_lot_number) REFERENCES Reagents(reagent_lot_number))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Derived_Calculated_Parameters (analyzer_code INT NOT NULL, test_code INT NOT NULL, reagent_lot_number INT NOT NULL, qc_lot_number INT NOT NULL, actual_sd INT, actual_cv INT, actual_mean INT, ewma INT, cusum INT, FOREIGN KEY (analyzer_code) REFERENCES Analyzer(analyzer_code), FOREIGN KEY (test_code) REFERENCES Test(test_code), FOREIGN KEY (reagent_lot_number) REFERENCES Reagents(reagent_lot_number), FOREIGN KEY (qc_lot_number) REFERENCES QC_Lot(qc_lot_number))")


mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

###

sql = "INSERT INTO Analyzer (analyzer_code, analyzer_name, anlyzer_input, analyzer_output) VALUES (%s, %s, %s, %s)"
val = [
    ('1001', 'Analyzer1', 'input1', 'output1'),
    ('1002', 'Analyzer2', 'input2', 'output2'),
    ('1003', 'Analyzer3', 'input3', 'output3'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO Test (test_code, test_name, test_group, test_date, test_linear_range, test_measuring_unit) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    ('2001', 'Test1', 'Group1', '2021-01-01', '100', 'mm'),
    ('2002', 'Test2', 'Group2', '2021-02-02', '150', 'mm'),
    ('2003', 'Test3', 'Group3', '2021-03-03', '200', 'mm'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO Reagents (reagent_lot_number, reagent_name, reagent_expiry_date) VALUES (%s, %s, %s)"
val = [
    ('3001', 'Reagent1', '2041-01-01'),
    ('3002', 'Reagent2', '2041-02-02'),
    ('3003', 'Reagent3', '2041-03-03'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO QC_Lot (qc_lot_number, qc_name, qc_level, qc_low_limit, qc_high_limit, qc_target_mean, qc_target_sd) VALUES (%s, %s, %s, %s, %s, %s, %s)"
val = [
    ('4001', 'QC1', 'Level1', '100', '200', '45', '75'),
    ('4002', 'QC2', 'Level2', '150', '340', '80', '62'),
    ('4003', 'QC3', 'Level3', '200', '500', '110', '89'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO QC_Results (qc_result_code, test_code, qc_lot_number, qc_result_mean, qc_result_sd) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('5001', '2001', '4001', '120', '92'),
    ('5002', '2002', '4002', '130', '35'),
    ('5003', '2003', '4003', '250', '65'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO analyzer_test (analyzer_code, test_code, reagent_lot_number) VALUES (%s, %s, %s)"
val = [
    ('1001', '2001', '3001'),
    ('1002', '2002', '3002'),
    ('1003', '2003', '3003'),

]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO Derived_Calculated_Parameters (analyzer_code, test_code, reagent_lot_number, qc_lot_number) VALUES (%s, %s, %s, %s)"
val = [
    ('1001', '2001', '3001', '4001'),
    ('1001', '2001', '3001', '4001'),
    ('1001', '2001', '3001', '4001'),
]

mycursor.executemany(sql, val)
mydb.commit()

###