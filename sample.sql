

CREATE TABLE Pharmacy
(
  pharma_name VARCHAR(20) NOT NULL,
  pharmacy_id VARCHAR NOT NULL,
  pharma_location VARCHAR(20) NOT NULL
);

CREATE TABLE Hospital
(
  h_name VARCHAR(15) NOT NULL,
  hosp_id VARCHAR NOT NULL,
  hosp_address VARCHAR(20) NOT NULL,
  pharmacy_id VARCHAR NOT NULL
);

CREATE TABLE Doctor
(
  doc_name VARCHAR(15) NOT NULL,
  doc_location VARCHAR(20) NOT NULL,
  doc_id VARCHAR NOT NULL,
  hosp_id VARCHAR NOT NULL
);

CREATE TABLE Medicine_name
(
  medicine_id VARCHAR NOT NULL,
  cost_price VARCHAR NOT NULL,
  mfgd DATE NOT NULL,
  expd DATE NOT NULL
);

CREATE TABLE Patient
(
  pat_name VARCHAR(15) NOT NULL,
  phone VARCHAR(10) NOT NULL,
  pid VARCHAR NOT NULL,
  p_address VARCHAR(20) NOT NULL,
  gender CHAR NOT NULL,
  age VARCHAR NOT NULL,
  doc_id VARCHAR NOT NULL
);

CREATE TABLE Bill
(
  bill_id VARCHAR NOT NULL,
  quantity VARCHAR NOT NULL,
  amount VARCHAR NOT NULL,
  patient_id VARCHAR NOT NULL,
  medicine_id VARCHAR NOT NULL,
  pharmacy_id VARCHAR NOT NULL
);

CREATE TABLE Supplier
(
  supplier_id VARCHAR NOT NULL,
  supplier_name VARCHAR(15) NOT NULL,
  supplier_location VARCHAR(15) NOT NULL,
  pharmacy_id VARCHAR NOT NULL,
  medicine_id VARCHAR NOT NULL,
  price VARCHAR NOT NULL
);

CREATE TABLE Employee
(
  emp_name VARCHAR(15) NOT NULL,
  eid VARCHAR NOT NULL,
  salary VARCHAR NOT NULL,
  emp_address VARCHAR(20) NOT NULL,
  mail_id VARCHAR(25) NOT NULL,
  gender CHAR NOT NULL,
  pharmacy_id VARCHAR NOT NULL
);

CREATE TABLE Pharmacy_phone
(
  phone VARCHAR NOT NULL,
  pharmacy_id VARCHAR NOT NULL
);

CREATE TABLE Doctor_phone
(
  phone VARCHAR NOT NULL,
  doc_id VARCHAR NOT NULL
);

CREATE TABLE Hospital_phone
(
  phone VARCHAR NOT NULL,
  hosp_id VARCHAR NOT NULL
);

--alter table commands for primary keys
ALTER TABLE Pharmacy ADD CONSTRAINT Pharmacy_pkey PRIMARY KEY(pharmacy_id);
ALTER TABLE Hospital ADD CONSTRAINT Hospital_pkey PRIMARY KEY(hosp_id);
ALTER TABLE Doctor ADD CONSTRAINT Doctor_pkey PRIMARY KEY(doc_id);
ALTER TABLE Patient ADD CONSTRAINT Patient_pkey PRIMARY KEY(pid);
ALTER TABLE Medicine_name ADD CONSTRAINT Medicine_name_pkey PRIMARY KEY(medicine_id);
ALTER TABLE Bill ADD CONSTRAINT Bill_pkey PRIMARY KEY(bill_id,medicine_id);
ALTER TABLE Supplier ADD CONSTRAINT Supplier_pkey PRIMARY KEY(supplier_id,medicine_id);
ALTER TABLE Employee ADD CONSTRAINT Employee_pkey PRIMARY KEY(eid);
ALTER TABLE Pharmacy_phone ADD CONSTRAINT Pharmacy_phone_pkey PRIMARY KEY(phone,pharmacy_id);
ALTER TABLE Doctor_phone ADD CONSTRAINT Doctor_phone_pkey PRIMARY KEY(phone,doc_id);
ALTER TABLE Hospital_phone ADD CONSTRAINT Hospital_phone_pkey PRIMARY KEY(phone,hosp_id);

--alter table commads for unique keys
ALTER TABLE Patient ADD CONSTRAINT Patient_ukey UNIQUE(pid);
ALTER TABLE Doctor ADD CONSTRAINT Doctor_ukey UNIQUE(doc_id);
ALTER TABLE Medicine_name ADD CONSTRAINT Medicine_ukey UNIQUE(medicine_id);
ALTER TABLE Pharmacy ADD CONSTRAINT Pharmacy_ukey UNIQUE(pharmacy_id);
ALTER TABLE Hospital ADD CONSTRAINT Hospital_ukey UNIQUE(hosp_id);

--alter table commands for foreign keys
ALTER TABLE Hospital ADD CONSTRAINT Hospital_fkey FOREIGN KEY(pharmacy_id) REFERENCES Pharmacy(pharmacy_id) on DELETE CASCADE;
ALTER TABLE Doctor ADD CONSTRAINT Doctor_fkey FOREIGN KEY(hosp_id) REFERENCES Hospital(hosp_id) on DELETE CASCADE;
ALTER TABLE Patient ADD CONSTRAINT Patient_fkey1 FOREIGN KEY(doc_id) REFERENCES Doctor(doc_id) on DELETE CASCADE;
ALTER TABLE Bill ADD CONSTRAINT Bill_fkey1 FOREIGN KEY(pharmacy_id) REFERENCES Pharmacy(pharmacy_id) on DELETE CASCADE;
ALTER TABLE Bill ADD CONSTRAINT Bill_fkey2 FOREIGN KEY(patient_id) REFERENCES Patient(pid) on DELETE CASCADE;
ALTER TABLE Bill ADD CONSTRAINT Bill_fkey3 FOREIGN KEY(medicine_id) REFERENCES Medicine_name(medicine_id) on DELETE CASCADE;
ALTER TABLE Supplier ADD CONSTRAINT Supplier_fkey1 FOREIGN KEY(pharmacy_id) REFERENCES Pharmacy(pharmacy_id) on DELETE CASCADE;
ALTER TABLE Supplier ADD CONSTRAINT Supplier_fkey2 FOREIGN KEY(medicine_id) REFERENCES Medicine_name(medicine_id) on DELETE CASCADE;
ALTER TABLE Employee ADD CONSTRAINT Employee_fkey FOREIGN KEY(pharmacy_id) REFERENCES Pharmacy(pharmacy_id) on DELETE CASCADE;
ALTER TABLE Pharmacy_phone ADD CONSTRAINT Pharmacy_phone_fkey FOREIGN KEY(pharmacy_id) REFERENCES Pharmacy(pharmacy_id) on DELETE CASCADE;
ALTER TABLE Doctor_phone ADD CONSTRAINT Doctor_phone_fkey FOREIGN KEY(doc_id) REFERENCES Doctor(doc_id) on DELETE CASCADE;
ALTER TABLE Hospital_phone ADD CONSTRAINT Hospital_phone_fkey FOREIGN KEY(hosp_id) REFERENCES Hospital(hosp_id) on DELETE CASCADE;

--alter table commands for check constraint
ALTER TABLE Medicine_name ADD CONSTRAINT Medicine_name_ckey CHECK(expd > mfgd);

--insert values into pharmacy(name,id,loc)
INSERT INTO Pharmacy VALUES('himalaya',9,'bangalore');
INSERT INTO Pharmacy VALUES('apollo',7,'davangere');
INSERT INTO Pharmacy VALUES('ravi medicals',5,'mumbai');
INSERT INTO Pharmacy VALUES('abc pharmacy',1,'chennai');
INSERT INTO Pharmacy VALUES('best care pharmacy',8,'davangere');
INSERT INTO Pharmacy VALUES('lotus medicals',2,'bangalore');

--insert values into medicine_name(id,price,mfgd,expd)
INSERT INTO Medicine_name VALUES(12753,250,'2019-12-10','2023-12-10');
INSERT INTO Medicine_name VALUES(82461,100,'2020-04-21','2022-04-20');
INSERT INTO Medicine_name VALUES(28466,470,'2021-07-31','2022-07-30');
INSERT INTO Medicine_name VALUES(24208,290,'2021-03-28','2023-03-27');
INSERT INTO Medicine_name VALUES(92161,130,'2018-09-01','2020-08-31');
INSERT INTO Medicine_name VALUES(72518,110,'2020-11-17','2023-11-16');
INSERT INTO Medicine_name VALUES(42613,175,'2021-10-19','2022-10-18');
INSERT INTO Medicine_name VALUES(51536,150,'2020-02-02','2021-02-01');
INSERT INTO Medicine_name VALUES(27541,150,'2019-08-30','2023-08-29');
INSERT INTO Medicine_name VALUES(42169,250,'2021-06-29','2024-06-28');

--insert values into hospital(name,id,loc,pharma id)
INSERT INTO Hospital VALUES('fortis',1375,'davangere',7);
INSERT INTO Hospital VALUES('narayana',8432,'bangalore',9);
INSERT INTO Hospital VALUES('columbia asia',3847,'bangalore',2);
INSERT INTO Hospital VALUES('vittal malya',4852,'hyderabad',9);
INSERT INTO Hospital VALUES('brundavan',2487,'chennai',1);
INSERT INTO Hospital VALUES('venlakh',4985,'mumbai',5);
INSERT INTO Hospital VALUES('victoria',9024,'chennai',7);
INSERT INTO Hospital VALUES('vity central',2862,'bangalore',9);
INSERT INTO Hospital VALUES('kims',7324,'davangere',8);
INSERT INTO Hospital VALUES('aarikei',1535,'mumbai',5);

--insert values into doctor(name,loc,id,hosp id)
INSERT INTO Doctor VALUES('leorio','mumbai',111,4985);
INSERT INTO Doctor VALUES('tenma','davangere',384,7324);
INSERT INTO Doctor VALUES('neferipitou','chennai',243,2487);
INSERT INTO Doctor VALUES('zeref','bangalore',984,8432);
INSERT INTO Doctor VALUES('aizen','bangalore',125,8432);
INSERT INTO Doctor VALUES('yujiro','bangalore',632,2862);
INSERT INTO Doctor VALUES('chopper','hyderabad',900,3847);
INSERT INTO Doctor VALUES('kaiji','davangere',420,1375);

--insert values into patient(name,phone,id,loc,gender,age,doc id)
INSERT INTO Patient VALUES('friend','9387483623',36,'bangalore','m',24,984);
INSERT INTO Patient VALUES('kaguya','8361465225',28,'bangalore','f',20,984);
INSERT INTO Patient VALUES('elise','7137197363',11,'chennai','f',31,243);
INSERT INTO Patient VALUES('akainu','9254134090',99,'davangere','m',65,384);
INSERT INTO Patient VALUES('sasori','6936253826',70,'mumbai','m',16,111);
INSERT INTO Patient VALUES('lucy','8297463847',49,'bangalore','f',24,632);
INSERT INTO Patient VALUES('hattori','8196384728',15,'davangere','m',70,420);
INSERT INTO Patient VALUES('iguni','9824976487',52,'mumbai','f',36,111);
INSERT INTO Patient VALUES('teresa','8724262813',41,'bangalore','f',28,125);
INSERT INTO Patient VALUES('yumeko','9748132864',67,'chennai','f',45,243);
INSERT INTO Patient VALUES('sasaki','9864382687',85,'davangere','m',42,420);
INSERT INTO Patient VALUES('nina','8157457728',13,'chennai','f',22,984);
INSERT INTO Patient VALUES('akeno','9246825428',97,'mumbai','f',27,384);
INSERT INTO Patient VALUES('yagami','7253762384',66,'bangalore','m',19,420);
INSERT INTO Patient VALUES('shizune','8274684321',89,'bangalore','f',73,632);
INSERT INTO Patient VALUES('denji','9452736572',73,'hyderabad','m',20,900);

--insert values into bill(bill id,quantity,amount,pat id,med id,pharma id)
INSERT INTO bill VALUES(217387,10,1000,36,82461,9);
INSERT INTO bill VALUES(412846,25,3250,11,92161,1);
INSERT INTO bill VALUES(134872,5,500,97,82461,7);
INSERT INTO bill VALUES(926728,14,4060,41,24208,2);
INSERT INTO bill VALUES(825765,7,1750,52,12753,5);
INSERT INTO bill VALUES(283724,15,3750,99,42169,8);
INSERT INTO bill VALUES(236467,14,1500,73,72518,9);
INSERT INTO bill VALUES(217387,30,4500,36,51536,2);
INSERT INTO bill VALUES(654622,20,3000,13,27541,1);
INSERT INTO bill VALUES(357834,5,2350,70,28466,9);
INSERT INTO bill VALUES(283724,5,1250,99,12753,7);
INSERT INTO bill VALUES(926728,14,1500,41,72518,2);
INSERT INTO bill VALUES(679279,14,3500,28,42169,2);
INSERT INTO bill VALUES(468620,10,1300,15,92161,7);
INSERT INTO bill VALUES(134872,15,2250,97,51536,8);

--insert values into supplier(id,name,loc,pharm id, med id, price)
INSERT INTO Supplier VALUES(100,'joker','bangalore',9,72518,95);
INSERT INTO Supplier VALUES(200,'obito','davangere',8,72518,100);
INSERT INTO Supplier VALUES(300,'hitman','mumbai',8,51536,200);
INSERT INTO Supplier VALUES(100,'joker','bangalore',7,92161,100);
INSERT INTO Supplier VALUES(400,'hisoka','chennai',1,27541,145);
INSERT INTO Supplier VALUES(500,'chrollo','bangalore',9,28466,440);
INSERT INTO Supplier VALUES(300,'hitman','davangere',7,82461,90);
INSERT INTO Supplier VALUES(600,'toshiro','mumbai',5,12753,215);
INSERT INTO Supplier VALUES(700,'gin','bangalore',9,82461,85);
INSERT INTO Supplier VALUES(400,'hisoka','chennai',1,92161,115);
INSERT INTO Supplier VALUES(800,'zabuza','bangalore',2,24208,250);
INSERT INTO Supplier VALUES(200,'obito','davangere',7,12753,215);
INSERT INTO Supplier VALUES(500,'chrollo','davangere',8,42169,225);
INSERT INTO Supplier VALUES(500,'chrollo','bangalore',2,51536,125);
INSERT INTO Supplier VALUES(900,'killua','bangalore',2,42169,235);
INSERT INTO Supplier VALUES(900,'killua','bangalore',2,72518,105);

--insert values into employee(name,id,salary,loc,mail,gender,pharma id)
INSERT INTO Employee VALUES('gotoh',10,25000,'bangalore','gotoh@abc.com','m',2);
INSERT INTO Employee VALUES('canary',20,22500,'mumbai','canary@xyz.com','f',5);
INSERT INTO Employee VALUES('biscuit',30,30000,'bangalore','biscuit@xyz.com','f',9);
INSERT INTO Employee VALUES('netero',40,40000,'davangere','netero@xyz.com','m',7);
INSERT INTO Employee VALUES('zeno',50,40000,'chennai','zeno@abc.com','m',1);
INSERT INTO Employee VALUES('silva',60,35000,'bangalore','silva@abc.com','m',9);
INSERT INTO Employee VALUES('alluka',70,20000,'davangere','alluka@xyz.com','f',8);
INSERT INTO Employee VALUES('palm',80,32500,'bangalore','palm@abc.com','f',2);
INSERT INTO Employee VALUES('razor',90,37500,'davangere','razor@xyz.com','m',7);