-- Data prepared by Andrea Whittaker, amwhitta@ualberta.ca

-- staff(staff_id, role, name, login, password)
INSERT INTO patients VALUES
('00001', 'N', 'Morgan', 'Morgman', 'DoggiesRule1'),
('00002', 'D', 'Mindy', 'Turtlez', 'DontGuessMyPassword333'),
('00003', 'A', 'Beverly', 'What', '!!!IDontWorkHere!!1');

-- patients(hcno, name, age_group, address, phone, emg_phone)
INSERT INTO patients VALUES
('64328', 'John', '20-30', 'street1, Edmonton, AB', '7806179109', '1538144594'),
('23769', 'Madison', '10-20', 'street2, Toronto, ON', '1246321395', '3642225888'),
('91623', 'Elizabeth', '20-30', 'street3, Calgary, AB', '4037172536', '4036046751'),
('75019', 'David', '10-20', 'street4, Edmonton, AB', '7805692237', '9183327158'),
('11137', 'James', '50-60', 'street5, Edmonton, AB', '6092213851', '6142222712'),
('88163', 'Rachel', '20-30', 'street6, Ottawa, ON', '2507507759', '2508687191'),
('35214', 'Ashley', '50-60', 'street7, Calgary, AB', '9985663327', '1168936509'),
('13372', 'Susan', '30-40', 'street8, Toronto, ON', '1248381117', '1162871789'),
('46547', 'Joseph', '30-40', 'street9, Regina, SK', '1248381117', '1162871789'),
('55599', 'Tarryn', '30-40', 'street10, Saskatoon, SK', '1248381117', '1162871789'),
('12234', 'Richard', '30-40', 'street11, Vancouver, BC', '1248381117', '1162871789');

-- charts(chart_id, hcno, adate, edate)
('60000', '64328', "2000-06-12 03:21:40.066", "2000-07-12 07:33:23.006"),
('70000', '75019', "2002-03-13 12:54:10.132", Null),
('90000', '91623', "2015-01-09 05:10:38.738", Null),
('13000', '13372', "2012-11-28 10:05:44.654", "2013-06-17 12:17:58.222");

-- symptoms(hcno, obs_date, sym_name)
INSERT INTO symptoms VALUES
('64328', "2000-06-12 03:21:40.066", 'fever'),
('64328', "2000-06-12 07:33:23.006", 'heartburn'),
('23769', "2012-11-29 10:05:44.654", 'headache'),
('23769', "2013-03-02 15:32:07.159", 'dizziness'),
('23769', "2013-06-17 12:17:58.222", 'hypertension'),
('91623', "2015-01-10 05:10:38.738", 'heartburn'),
('91623', "2015-01-13 22:40:11.346", 'vertigo'),
('91623', "2015-01-18 06:36:29.905", 'memory loss'),
('75019', "2002-03-15 12:54:10.132", 'dizziness'),
('75019', "2002-03-15 10:54:10.132", 'heartburn'),
('13372', "2012-11-29 10:05:44.654", 'headache'),
('13372', "2013-03-02 15:32:07.159", 'dizziness'),
('13372', "2013-06-17 12:17:58.222", 'hypertension'),
('11137', "2000-06-12 03:21:40.066", 'fever');

-- diagnoses(hcno, chart_id, staff_id, ddate, diagnosis)
('64328', '60000', '00002', "2000-07-12 07:33:23.006", 'Trypophobia');

-- medications(hcno, mdate, amount, days, drug_name)
INSERT INTO medications VALUES
('64328', "2001-07-13 01:44:19.357", 2, 3, 'Jardiance'),
('11137', "2001-07-13 01:44:19.357", 2, 3, 'Jardiance'),
('23769', "2012-11-29 14:33:41.984", 6, 11, 'Jardiance'),
('64328', "2000-07-13 01:44:19.357", 4, 10, 'Abelcet'),
('91623', "2015-01-10 02:10:38.738", 4, 20, 'Niacin'),
('75019', "2005-08-22 14:33:41.984", 6, 11, 'Obizur'),
('75019', "2005-08-22 14:33:41.984", 1, 7, 'Aleve'),
('35214', "2003-09-05 03:12:55.028", 207, 23, 'Niacin'),
('88163', "2003-09-05 03:12:55.028", 290, 30, 'Niacin'),
('13372', "2012-04-20 11:12:33.082", 220, 40, 'Niacin'),
('46547', "2003-09-05 03:12:55.028", 5, 23, 'Prozac'),
('55599', "2003-09-05 03:12:55.028", 20, 30, 'Prozac'),
('10234', "2012-04-20 11:12:33.082", 150, 10, 'Prozac');

-- reportedallergies(hcno, drug_name)
INSERT INTO reportedallergies VALUES
('64328', 'Jardiance'),
('88163', 'Motrin'),
('11137', 'Obizur'),
('75019', 'Jardiance'),
('23769', 'Metformin'),
('23769', 'Jardiance'),
('13372', 'Jardiance'),
('91623', 'Obizur'),
('13372', 'Metformin');

-- drugs(drug_name, category)
INSERT INTO drugs VALUES
('Abelcet', 'analgesic'),
('Jardiance', 'anti-pyretic'),
('Niacin', 'anti-inflammatory'),
('Prozac', 'anti-depressant'),
('Obizur', 'analgesic'),
('Motrin', 'anti-inflammatory'),
('Aleve', 'anti-inflammatory'),
('Metformin', 'salicylate');

-- dosage(drug_name, age_group, sug_amount, max_amount)
INSERT INTO dosage VALUES
('Abelcet', '10-20', 2, 3),
('Abelcet', '20-30', 2, 3),
('Abelcet', '30-40', 5, 6),
('Abelcet', '40-50', 5, 6),
('Abelcet', '50-60', 5, 6),
('Jardiance', '10-20', 10, 11),
('Jardiance', '20-30', 10, 11),
('Jardiance', '30-40', 10, 11),
('Jardiance', '40-50', 20, 23),
('Jardiance', '50-60', 20, 23),
('Niacin', '10-20', 4, 6),
('Niacin', '20-30', 4, 6),
('Niacin', '30-40', 4, 6),
('Niacin', '40-50', 4, 6),
('Niacin', '50-60', 4, 6),
('Prozac', '10-20', 1, 3),
('Prozac', '20-30', 1, 3),
('Prozac', '30-40', 1, 3),
('Prozac', '40-50', 1, 3),
('Prozac', '50-60', 1, 3),
('Obizur', '10-20', 2, 5),
('Obizur', '20-30', 2, 5),
('Obizur', '30-40', 8, 10),
('Obizur', '40-50', 8, 10),
('Obizur', '50-60', 8, 10),
('Motrin', '10-20', 5, 7),
('Motrin', '20-30', 5, 7),
('Motrin', '30-40', 5, 7),
('Motrin', '40-50', 5, 7),
('Motrin', '50-60', 5, 7),
('Aleve', '10-20', 1, 2),
('Aleve', '20-30', 1, 2),
('Aleve', '30-40', 3, 6),
('Aleve', '40-50', 3, 6),
('Aleve', '50-60', 3, 6),
('Metformin', '10-20', 1, 4),
('Metformin', '20-30', 1, 4),
('Metformin', '30-40', 3, 4),
('Metformin', '40-50', 3, 4),
('Metformin', '50-60', 2, 4);

-- inferredallergies(alg, canbe_alg)
INSERT INTO inferredallergies VALUES
('Obizur', 'Prozac'),
('Metformin', 'Motrin');
