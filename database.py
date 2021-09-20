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
    "CREATE TABLE IF NOT EXISTS test_qc_results (t_code INT NOT NULL, a_id INT NOT NULL, r_lot_number INT NOT NULL, qc_lot_number INT NOT NULL, qc_assigned_mean INT, qc_assigned_sd INT, qc_assigned_cv INT, qualitative_assigned INT, qc_result INT, qc_flag BOOLEAN, qc_date DATE, qc_calculated_mean INT, qc_calculated_sd INT, qc_calculated_cv INT, qc_overall_status VARCHAR(255), FOREIGN KEY (t_code) REFERENCES Test(test_code), FOREIGN KEY (a_id) REFERENCES Analyzer(analyzer_id), FOREIGN KEY (r_lot_number) REFERENCES Reagents(reagent_lot_number), FOREIGN KEY (qc_lot_number) REFERENCES QC_Parameters(qc_lot_number))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Calculated_Parameters (ids INT NOT NULL, no_of_points INT, mu INT, ewma INT, cusum INT, PRIMARY KEY(ids))")

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Lab (lab_id INT NOT NULL, a_id INT NOT NULL, lab_branch VARCHAR(255), lab_unit VARCHAR(255), PRIMARY KEY(lab_id), FOREIGN KEY (a_id) REFERENCES Analyzer(analyzer_id))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)

###



sql = "INSERT INTO Analyzer (analyzer_id, analyzer_name, anlyzer_manufacturer, analyzer_model, analyzer_branch, analyzer_lab_unit) VALUES (%s, %s, %s, %s, %s, %s)"
val = [
    ('1001', 'Analyzer1','Company1','M1','GTS','Hematology'),
    ('1002', 'Analyzer2','Company1','M2','GTS','Hematology'),
    ('1003', 'Analyzer3','Company1','M3','GTS','Hematology'),
    ('1004', 'Analyzer4','Company2','M4','GTS','Hematology'),
    ('1005', 'Analyzer5','Company2','M5','GTS','Hematology'),
    ('1006', 'Analyzer6','Company2','M6','GTS','Hematology'),
    ('1007', 'Analyzer7','Company3','M7','GTS','Hematology'),
    ('1008', 'Analyzer8','Company3','M8','GTS','Hematology'),
    ('1009', 'Analyzer9','Company3','M9','GTS','Hematology'),
    ('1010', 'Analyzer10','Company4','M10','GTS','Hematology'),
    ('1011', 'Analyzer11','Company4','M11','GTS','Hematology'),
    ('1012', 'Analyzer12','Company4','M12','GTS','Hematology'),
    ('1013', 'Analyzer13','Company5','M13','GTS','Hematology'),
    ('1014', 'Analyzer14','Company5','M14','GTS','Hematology'),
    ('1015', 'Analyzer15','Company5','M15','GTS','Hematology'),
    ('1016', 'Analyzer16','Company6','M16','GTS','Hematology'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO Test (test_code, test_name, test_measurement_unit, test_delta_check, test_analytical_quality_goal, test_group) VALUES (%s, %s,%s, %s, %s, %s)"
val = [
    ('2001', 'Test1','Unit1','Function1','Goal1','Group1'),
    ('2002', 'Test2','Unit2','Function2','Goal2','Group2'),
    ('2003', 'Test3','Unit3','Function3','Goal3','Group3'),
    ('2004', 'Test4','Unit4','Function4','Goal4','Group4'),
    ('2005', 'Test5','Unit5','Function5','Goal5','Group5'),
    ('2006', 'Test6','Unit6','Function6','Goal6','Group6'),
    ('2007', 'Test7','Unit7','Function7','Goal7','Group7'),
    ('2008', 'Test8','Unit8','Function8','Goal8','Group8'),
    ('2009', 'Test9','Unit9','Function9','Goal9','Group9'),
    ('2010', 'Test10','Unit10','Function10','Goal10','Group10'),
    ('2011', 'Test11','Unit11','Function11','Goal11','Group11'),
    ('2012', 'Test12','Unit12','Function12','Goal12','Group12'),
    ('2013', 'Test13','Unit13','Function13','Goal13','Group13'),
    ('2014', 'Test14','Unit14','Function14','Goal14','Group14'),
    ('2015', 'Test15','Unit15','Function15','Goal15','Group15'),
    ('2016', 'Test16','Unit16','Function16','Goal16','Group16'),
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO Reagents (reagent_lot_number, reagent_name, reagent_manufacturer, reagent_expiry_date) VALUES (%s, %s, %s, %s)"
val = [
    ('3001', 'Reagent1', 'M1',  '2021-1-1'),
    ('3002', 'Reagent2', 'M2',  '2021-2-26'),
    ('3003', 'Reagent3', 'M3',  '2021-3-30'),
    ('3004', 'Reagent4', 'M4',  '2021-4-4'),
    ('3005', 'Reagent5', 'M5',  '2021-5-5'),
    ('3006', 'Reagent6', 'M6',  '2021-6-6'),
    ('3007', 'Reagent7', 'M7',  '2021-7-17'),
    ('3008', 'Reagent8', 'M8',  '2021-8-8'),
    ('3009', 'Reagent9', 'M9',  '2021-9-9'),
    ('3010', 'Reagent10', 'M10','2021-10-10'),
    ('3011', 'Reagent11', 'M9', '2021-10-6'),
    ('3012', 'Reagent12', 'M9', '2021-11-16'),
    ('3013', 'Reagent13', 'M11','2021-12-28'),
    ('3014', 'Reagent14', 'M12','2021-11-13'),
    ('3015', 'Reagent15', 'M13','2021-10-21'),
    ('3016', 'Reagent16', 'M13','2021-12-12'),
    
]

mycursor.executemany(sql, val)
mydb.commit()

###

sql = "INSERT INTO QC_Parameters (qc_lot_number, qc_name, qc_type, qc_level, qc_manufacturer,qc_speciality, qc_expiry_date) VALUES (%s, %s,%s, %s, %s, %s, %s)"
val = [
    ('4001', 'QC1', 'Type1', 'Level1', 'M1', 'SP1','2022-1-1'),
    ('4002', 'QC2', 'Type2', 'Level1', 'M2', 'SP2','2022-1-1'),
    ('4003', 'QC3', 'Type3', 'Level1', 'M3', 'SP3','2022-2-2'),
    ('4004', 'QC4', 'Type4', 'Level1', 'M4', 'SP4','2022-2-2'),
    ('4005', 'QC5', 'Type5', 'Level2', 'M5', 'SP5','2022-3-3'),
    ('4006', 'QC6', 'Type6', 'Level2', 'M6', 'SP6','2022-3-3'),
    ('4007', 'QC7', 'Type7', 'Level2', 'M7', 'SP7','2022-4-4'),
    ('4008', 'QC8', 'Type8', 'Level2', 'M8', 'SP8','2022-4-4'),
    ('4009', 'QC9', 'Type9', 'Level3', 'M9', 'SP9','2022-5-5'),
    ('4010', 'QC10', 'Type10', 'Level3', 'M10', 'SP10','2022-5-5'),
    ('4011', 'QC11', 'Type11', 'Level3', 'M11', 'SP11','2022-6-6'),
    ('4012', 'QC12', 'Type12', 'Level3', 'M12', 'SP12','2022-6-6'),
    ('4013', 'QC13', 'Type13', 'Level4', 'M13', 'SP13','2022-7-7'),
    ('4014', 'QC14', 'Type14', 'Level4', 'M14', 'SP14','2022-7-7'),
    ('4015', 'QC15', 'Type15', 'Level4', 'M15', 'SP15','2022-8-8'),
    ('4016', 'QC16', 'Type16', 'Level4', 'M16', 'SP16','2022-8-8'),
    
]

mycursor.executemany(sql, val)
mydb.commit()



sql = "INSERT INTO test_qc_results (t_code, a_id, r_lot_number, qc_lot_number, qc_assigned_mean, qc_assigned_sd, qc_assigned_cv, qualitative_assigned, qc_result, qc_flag, qc_date, qc_calculated_mean, qc_calculated_sd, qc_calculated_cv, qc_overall_status) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
val = [
    ('2001', '1001', '3001', '4001', '92', '11', '15', '17', '99', '1',       '2021-1-1', '95', '9', '19', 'PENDING'),
    ('2002', '1002', '3002', '4002', '90', '5', '10', '15', '100', '1',       '2021-1-2', '94', '10', '16', 'PENDING'),
    ('2003', '1003', '3003', '4003', '70', '20', '80', '70', '90', '1',       '2021-2-23', '75', '19', '70', 'COMPLETE'),
    ('2004', '1004', '3004', '4004', '50', '40', '19', '50', '100', '0',     '2021-2-4', '54', '45', '20', 'COMPLETE'),
    ('2005', '1005', '3005', '4005', '100', '50', '40', '50', '99', '1',      '2021-3-5', '95', '40', '20', 'COMPLETE'),
    ('2006', '1006', '3006', '4006', '30', '90', '80', '48', '120', '1',      '2021-3-26', '35', '91', '89', 'COMPLETE'),
    ('2007', '1007', '3007', '4007', '90', '40', '19', '38', '100', '0',     '2021-4-7', '95', '30', '20', 'PENDING'),
    ('2008', '1008', '3008', '4008', '83', '14', '20', '99', '28', '1',       '2021-5-8', '80', '15', '19', 'PENDING'),
    ('2009', '1009', '3009', '4009', '27', '90', '92', '18', '37', '1',       '2021-6-9', '30', '80', '80', 'COMPLETE'),
    ('2010', '1010', '3010', '4010', '38', '100', '26', '138', '100','1',    '2021-7-10', '50', '90', '100', 'COMPLETE'),
    ('2011', '1011', '3011', '4011', '80', '110', '150', '90', '128','1',    '2021-8-8', '90', '100', '145', 'PENDING'),
    ('2012', '1012', '3012', '4012', '15', '20', '70', '28', '37','1',       '2021-9-18', '20', '26', '78', 'PENDING'),
    ('2013', '1013', '3013', '4013', '93', '74', '18', '28', '94','1',       '2021-9-29', '90', '70', '15', 'PENDING'),
    ('2014', '1014', '3014', '4014', '100', '110', '150', '82', '100','0',  '2021-10-15', '95', '107', '152', 'PENDING'),
    ('2015', '1015', '3015', '4015', '76', '92', '61', '21', '83','1',       '2021-11-20', '75', '90', '60', 'PENDING'),
    ('2016', '1016', '3016', '4016', '92', '100', '29', '63', '100','1',     '2021-12-22', '95', '90', '19', 'PENDING'),
]

mycursor.executemany(sql, val)
mydb.commit()



sql = "INSERT INTO test_analyzer (a_id, t_code, r_lot_number, linear_range_from , linear_range_to) VALUES (%s, %s, %s, %s, %s)"
val = [
    ('1001', '2001', '3001', '10','20'),
    ('1002', '2002', '3002', '10','20'),
    ('1003', '2003', '3003', '10','20'),
    ('1004', '2004', '3004', '10','20'),
    ('1005', '2005', '3005', '10','20'),
    ('1006', '2006', '3006', '10','20'),
    ('1007', '2007', '3007', '10','20'),
    ('1008', '2008', '3008', '10','20'),
    ('1009', '2009', '3009', '10','20'),
    ('1010', '2010', '3010', '10','20'),
    ('1011', '2011', '3011', '10','20'),
    ('1012', '2012', '3012', '10','20'),
    ('1013', '2013', '3013', '10','20'),
    ('1014', '2014', '3014', '10','20'),
    ('1015', '2015', '3015', '10','20'),
    ('1016', '2016', '3016', '10','20')
]
    

mycursor.executemany(sql, val)
mydb.commit()

# ###

# sql = "INSERT INTO Calculated_Parameters (ids, no_of_points, mu, ewma, cusum) VALUES (%s, %s, %s, %s, %s)"
# val = [
#     ('6001', '120', '13', '18','29'),
# ]

# mycursor.executemany(sql, val)
# mydb.commit()

# ###


###

sql = "INSERT INTO Lab (lab_id, a_id, lab_branch, lab_unit) VALUES (%s, %s, %s, %s)"
val = [
    ('0001', '1001', 'GTS', 'Hematology'),
    ('0002', '1002', 'GTS', 'Hematology'),
    ('0003', '1003', 'GTS', 'Hematology'),
    ('0004', '1004', 'GTS', 'Hematology'),
    ('0005', '1005', 'GTS', 'Hematology'),
    ('0006', '1006', 'GTS', 'Hematology'),
    ('0007', '1007', 'GTS', 'Hematology'),
    ('0008', '1008', 'GTS', 'Hematology'),
    ('0009', '1009', 'GTS', 'Hematology'),
    ('0010', '1010', 'GTS', 'Hematology'),
    ('0011', '1011', 'GTS', 'Hematology'),
    ('0012', '1012', 'GTS', 'Hematology'),
    ('0013', '1013', 'GTS', 'Hematology'),
    ('0014', '1014', 'GTS', 'Hematology'),
    ('0015', '1015', 'GTS', 'Hematology'),
    ('0016', '1016', 'GTS', 'Hematology'),
]

mycursor.executemany(sql, val)
mydb.commit()

###