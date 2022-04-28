set echo on feeback on term on

spool '/home/oracle/clixx_db_vers_1.0_gap_joycelyne.log'

show user
select * from global_name;

select systimestamp from dual;


--Dropping existing VERS_1.0 tables
drop table orders;
drop table products;
drop table tracking;
drop table credit_card;
drop table demographics;
drop table customer;


--Creating VERS_1.0 tables

create table CUSTOMER(
CUST_ID number,
FNAME varchar2(26),
LNAME varchar2(26),
GENDER char,
DOB date,
EMAIL varchar2(26));


create table DEMOGRAPHICS(
CUST_ID number,
DEM_ID number,
ADDRESS varchar2(50),
ADDRESS_TYPE char,
DEFAULTS char);

create table CREDIT_CARD(
CUST_ID number,
CC_NO varchar2(16),
CC_EXP date,
CC_CVV number,
CC_TYPE varchar2(10));

create table PRODUCTS(
PROD_ID number,
PROD_NAME varchar2(26),
PROD_TYPE varchar2(26),
QTY number,
SKU varchar2(26),
PRICE number);

create table TRACKING(
TRACK_ID number,
TRACK_NO varchar2(26),
CUST_ID number,
DELIV_TYPE varchar2(26),
ORDER_STATUS varchar2(26),
DELIV_DATE date);

create table ORDERS(
CUST_ID number,
ORDER_ID number,
ORDER_STATUS varchar2(26),
ORDER_DATE date,
DELIV_TYPE varchar2(26),
PROD_ID number,
TRACK_ID number);

--Creating VERS_1.0 constraints

alter table CUSTOMER add constraint PK_CUSTOMER_CUST_ID PRIMARY KEY(CUST_ID);
alter table DEMOGRAPHICS add constraint PK_DEMOGRAPHICS_DEM_ID PRIMARY KEY(DEM_ID);
alter table CREDIT_CARD add constraint PK_CREDIT_CARD_CC_NO PRIMARY KEY(CC_NO);
alter table PRODUCTS add constraint PK_PRODUCTS_PROD_ID PRIMARY KEY(PROD_ID);
alter table TRACKING add constraint PK_TRACKING_TRACK_ID PRIMARY KEY(TRACK_ID);
alter table DEMOGRAPHICS add constraint FK_DEMOGRAPHICS_CUST_ID FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER(CUST_ID);

alter table CREDIT_CARD add constraint FK_CREDIT_CARD_CUST_ID FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER(CUST_ID);

alter table ORDERS add constraint FK_ORDERS_CUST_ID FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER(CUST_ID);
alter table ORDERS add constraint FK_ORDERS_PROD_ID FOREIGN KEY(PROD_ID) REFERENCES PRODUCTS(PROD_ID);
alter table ORDERS add constraint FK_ORDERS_TRACK_ID FOREIGN KEY(TRACK_ID) REFERENCES TRACKING(TRACK_ID);

alter table TRACKING add constraint FK_TRACKING_CUST_ID FOREIGN KEY(CUST_ID) REFERENCES CUSTOMER(CUST_ID);

--Inserting data into CUSTOMER table

insert into CUSTOMER
values (1,'Sandra','Smith','F',to_date('01/02/1984', 'MM/DD/YYYY'),'Sandra.smith@stackit.com');

insert into CUSTOMER
values (2,'Tom','Dean','M',to_date('03/04/1995', 'MM/DD/YYYY'),'Tom.dean@stackit.com');

insert into CUSTOMER
values (3,'Brenda','Bell','F',to_date('05/06/1973', 'MM/DD/YYYY'),'Brenda.bell@stackit.com');

insert into CUSTOMER
values (4,'Frank','Crane','M',to_date('12/31/1965', 'MM/DD/YYYY'),'Frank.crane@stackit.com');

insert into CUSTOMER
values (5,'Judy','Park','F',to_date('06/24/1990', 'MM/DD/YYYY'),'Judy.park@stackit.com');
commit;

--Inserting data into DEMOGRAPHICS table

insert into DEMOGRAPHICS
values (1,1,'234 S Bladensburg, MD','B','B');

insert into DEMOGRAPHICS
values (1,2,'777 Chicago, IL','S','B');


insert into DEMOGRAPHICS
values (2,3,'534 Dallas, TX','B','B');


insert into DEMOGRAPHICS
values (2,4,'111 S Hope St, MD','S','B');


insert into DEMOGRAPHICS
values (3,5,'647 W 9th St, Houston, TX','B','S');

insert into DEMOGRAPHICS
values (3,6,'102 Pine St, Pittsburg, KS','S','S');

insert into DEMOGRAPHICS
values (4,7,'345 Laurel St, MD','B','B');

insert into DEMOGRAPHICS
values (4,8,'311 College Park Ave, VA','S','B');

insert into DEMOGRAPHICS
values (5,9,'16 S. Pine St, IL','B','S');

insert into DEMOGRAPHICS
values (5,10,'12 Columbia Pkwy, VA','S','S');
commit;

--Inserting data into CREDIT_CARD table
insert into CREDIT_CARD
values (1,1234567892345678,to_date('12/23','MM/DD'),978,'VISA');

insert into CREDIT_CARD
values (1,5527654987612567,to_date('10/24','MM/DD'),162,'MASTERCARD');

insert into CREDIT_CARD
values (2,3652876549876523,to_date('09/22','MM/DD'),791,'AMEX');

insert into CREDIT_CARD
values (2,7832548346947924,to_date('11/23','MM/DD'),487,'VISA');

insert into CREDIT_CARD
values (3,1554811415974350,to_date('07/26','MM/DD'),393,'MASTERCARD');

insert into CREDIT_CARD
values (3,9975384469931352,to_date('10/23','MM/DD'),190,'AMEX');

insert into CREDIT_CARD
values (4,9852473513477348,to_date('12/25','MM/DD'),674,'VISA');

insert into CREDIT_CARD
values (4,4310615315011158,to_date('06/23','MM/DD'),795,'MASTERCARD');

insert into CREDIT_CARD
values (5,8784166119114314,to_date('04/25','MM/DD'),248,'AMEX');

insert into CREDIT_CARD
values (5,7015918012293700,to_date('03/23','MM/DD'),374,'VISA');
commit;

--Inserting data into PRODUCTS table

insert into PRODUCTS
values (001,'Morton Salt','Spices',80,3540759,0.99);

insert into PRODUCTS
values (002,'Domino Sugar','Sweetener',50,5367501,1.99);

insert into PRODUCTS
values (003,'Lipton','Black Tea',60,6145498,5.99);


insert into PRODUCTS
values (004,'SaraLee','Wheat Bread',23,1068370,3.19);

insert into PRODUCTS
values (005,'Barilla','Spaghetti',87,6879757,1.59);

insert into PRODUCTS
values (006,'Mahatma','Brown Rice',43,3570117,3.99);


insert into PRODUCTS
values (007,'Bounty','Paper Towel',15,1653668,16.79);

insert into PRODUCTS
values (008,'Dial','Hand Wash',65,2569504,2.49);

insert into PRODUCTS
values (009,'Eggland','Brown Eggs',24,7999478,3.69);

insert into PRODUCTS
values (010,'Deer Park','Bottled Water',50,9304871,4.39);
commit;

--Inserting data into TRACKING table

insert into TRACKING
values (01,111111,1,'Standard','Delivered',to_date('03/17/2022','MM/DD/YYYY'));


insert into TRACKING
values (02,222222,2,'Priority','Delivered',to_date('03/18/2022','MM/DD/YYYY'));


insert into TRACKING
values (03,333333,3,'Standard','Delivered',to_date('03/22/2022','MM/DD/YYYY'));


insert into TRACKING
values (04,444444,4,'Priority','Processing',to_date('03/23/2022','MM/DD/YYYY'));


insert into TRACKING
values (05,555555,5,'Standard','Processing',to_date('03/24/2022','MM/DD/YYYY'));
commit;

--Inserting data into ORDERS table

insert into ORDERS
values (1,1,'Completed',to_date('03/14/2022', 'MM/DD/YYYY'),'Standard',008,01);

insert into ORDERS
values (1,1,'Completed',to_date('03/14/2022', 'MM/DD/YYYY'),'Standard',005,01);

insert into ORDERS
values (2,2,'Completed',to_date('03/16/2022', 'MM/DD/YYYY'),'Priority',002,02);

insert into ORDERS
values (2,2,'Completed',to_date('03/16/2022', 'MM/DD/YYYY'),'Priority',001,02);

insert into ORDERS
values (3,3,'Completed',to_date('03/19/2022', 'MM/DD/YYYY'),'Standard',007,03);

insert into ORDERS
values (3,3,'Completed',to_date('03/19/2022', 'MM/DD/YYYY'),'Standard',003,03);


insert into ORDERS
values (4,4,'Processing',to_date('03/20/2022', 'MM/DD/YYYY'),'Priority',009,04);

insert into ORDERS
values (4,4,'Processing',to_date('03/20/2022', 'MM/DD/YYYY'),'Priority',007,04);


insert into ORDERS
values (5,5,'Processing',to_date('03/22/2022', 'MM/DD/YYYY'),'Standard',003,05);

insert into ORDERS
values (5,5,'Processing',to_date('03/22/2022', 'MM/DD/YYYY'),'Standard',009,05);
commit;

CREATE OR REPLACE VIEW VW_EXISTING_USER_PROFILE AS
SELECT 
a.FNAME,
a.LNAME,
a.DOB,
a.GENDER,
b.ADDRESS,
c.CC_NO,
c.CC_EXP, 
c.CC_CVV,
d.ORDER_DATE,
d.ORDER_ID,
d.ORDER_STATUS,
e.TRACK_NO
FROM CUSTOMER a
INNER JOIN DEMOGRAPHICS b
ON a.CUST_ID=b.CUST_ID
INNER JOIN CREDIT_CARD c
  ON a.CUST_ID = c.CUST_ID
INNER JOIN ORDERS d
  ON a.CUST_ID = d.CUST_ID
INNER JOIN TRACKING e
  ON a.CUST_ID = e.CUST_ID;


select systimestamp from dual;

spool off

