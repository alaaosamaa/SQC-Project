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
    "CREATE TABLE IF NOT EXISTS Analyzer (analyzer_id INT NOT NULL, analyzer_name VARCHAR(255), anlyzer_manufacturer VARCHAR(255), analyzer_model VARCHAR(255), analyzer_branch VARCHAR(255), analyzer_lab_unit VARCHAR(255),PRIMARY KEY(analyzer_id), UNIQUE(analyzer_model))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Test (test_code INT NOT NULL, test_name VARCHAR(255), test_measurement_unit VARCHAR(255), test_delta_check VARCHAR(255), test_analytical_quality_goal VARCHAR(255), test_group VARCHAR(255), PRIMARY KEY(test_code), UNIQUE(test_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Reagents (reagent_lot_number INT NOT NULL, reagent_name VARCHAR(255), reagent_manufacturer VARCHAR(255), reagent_expiry_date DATE, PRIMARY KEY(reagent_lot_number), UNIQUE(reagent_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS test_analyzer (a_id INT NOT NULL, t_code INT NOT NULL, r_lot_number INT NOT NULL, linear_range_from INT, linear_range_to INT, FOREIGN KEY (a_id) REFERENCES Analyzer(analyzer_id), FOREIGN KEY (t_code) REFERENCES Test(test_code), FOREIGN KEY (r_lot_number) REFERENCES Reagents(reagent_lot_number))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS QC_Parameters (qc_lot_number INT NOT NULL, qc_name VARCHAR(255), qc_type VARCHAR(255), qc_level VARCHAR(255), qc_manufacturer VARCHAR(255), qc_speciality VARCHAR(255), qc_expiry_date DATE, PRIMARY KEY(qc_lot_number), UNIQUE(qc_name))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS test_qc_results (t_code INT NOT NULL, a_id INT NOT NULL, r_lot_number INT NOT NULL, q_c_lot_number INT NOT NULL, qc_assigned_mean INT, qc_assigned_sd INT, qc_assigned_cv INT, qualitative_assigned INT, qc_result INT, qc_flag BOOLEAN, qc_date DATE, qc_calculated_mean INT, qc_calculated_sd INT, qc_calculated_cv INT, qc_overall_status VARCHAR(255), FOREIGN KEY (t_code) REFERENCES Test(test_code), FOREIGN KEY (a_id) REFERENCES Analyzer(analyzer_id), FOREIGN KEY (r_lot_number) REFERENCES Reagents(reagent_lot_number), FOREIGN KEY (q_c_lot_number) REFERENCES QC_Parameters(qc_lot_number))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Calculated_Parameters (ids INT NOT NULL, no_of_points INT, mu INT, ewma INT, cusum INT, PRIMARY KEY(ids))")



mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

###

sql = "INSERT INTO Analyzer (analyzer_id, analyzer_name) VALUES (%s, %s)"
val = [
    ('1001', 'Analyzer1'),
    ('1002', 'Analyzer2'),
    ('1003', 'Analyzer3'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO Test (test_code, test_name) VALUES (%s, %s)"
val = [
    ('2001', 'Test1'),
    ('2002', 'Test2'),
    ('2003', 'Test3'),
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

sql = "INSERT INTO QC_Parameters (qc_lot_number, qc_name) VALUES (%s, %s)"
val = [
    ('4001', 'QC1'),
    ('4002', 'QC2'),
    ('4003', 'QC3'),
]

mycursor.executemany(sql, val)
mydb.commit()

# ###

# sql = "INSERT INTO QC_Results (qc_result_code, test_code, qc_lot_number, qc_result_mean, qc_result_sd) VALUES (%s, %s, %s, %s, %s)"
# val = [
#     ('5001', '2001', '4001', '120', '92'),
#     ('5002', '2002', '4002', '130', '35'),
#     ('5003', '2003', '4003', '250', '65'),
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

# ###

sql = "INSERT INTO test_analyzer (a_id, t_code, r_lot_number) VALUES (%s, %s, %s)"
val = [
    ('1001', '2001', '3001'),
    ('1002', '2002', '3002'),
    ('1003', '2003', '3003'),

]

mycursor.executemany(sql, val)
mydb.commit()

# ###

# sql = "INSERT INTO Calculated_Parameters (analyzer_id, test_code, reagent_lot_number, qc_lot_number) VALUES (%s, %s, %s, %s)"
# val = [
#     ('1001', '2001', '3001', '4001'),
#     ('1001', '2001', '3001', '4001'),
#     ('1001', '2001', '3001', '4001'),
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

# ###