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
    "CREATE TABLE IF NOT EXISTS Reagents (reagent_lot_number INT NOT NULL, reagent_reagent_name VARCHAR(255), reagent_expiry_date DATE), PRIMARY KEY(reagent_lot_number), UNIQUE(reagent_reagent_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS QC_Sample (qc_lot_number INT NOT NULL, qc_name VARCHAR(255), qc_level VARCHAR(255), qc_low_limit INT, qc_high_limit INT, qc_mean INT, qc_sd INT, PRIMARY KEY(qc_lot_number), UNIQUE(qc_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS analyzer_test (analyzer_code INT NOT NULL, test_code INT NOT NULL, reagent_lot_number INT NOT NULL, FOREIGN KEY (analyzer_code) REFERENCES Analyzer(analyzer_code), FOREIGN KEY (test_code) REFERENCES Test(test_code), FOREIGN KEY (reagent_lot_number) REFERENCES Reagents(reagent_lot_number))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Derived_Calculated_Parameters (analyzer_code INT NOT NULL, test_code INT NOT NULL, reagent_lot_number INT NOT NULL, qc_lot_number INT NOT NULL, actual_sd INT NOT NULL, actual_cv INT NOT NULL, actual_mean INT NOT NULL, ewma INT NOT NULL, cusum INT NOT NULL, FOREIGN KEY (analyzer_code) REFERENCES Analyzer(analyzer_code)), FOREIGN KEY (test_code) REFERENCES Test(test_code)), FOREIGN KEY (reagent_lot_number) REFERENCES Reagents(reagent_lot_number)), FOREIGN KEY (qc_lot_number) REFERENCES QC_Sample(qc_lot_number))"
)

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)