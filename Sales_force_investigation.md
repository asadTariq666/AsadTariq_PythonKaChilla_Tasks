# Sales Force Investigation
## From Mirror DB

### 1. Number of calls
Table : vault.salesforce_task_mart

Query :
```
select distinct count(task_id) 
from vault.salesforce_task_mart
where task_sub_type like 'Call';
```

### 2. Call Duration
Table : vault.salesforce_task_mart

Query :
```
SELECT task_id,task_sub_type, task_status, task_completion, task_creation,
EXTRACT(EPOCH FROM (vault.salesforce_task_mart.task_completion - vault.salesforce_task_mart.task_creation)) /3600 AS Duration
from vault.salesforce_task_mart
where task_sub_type like 'Call' AND task_completion!= task_creation;
```
**Issue**

Many of the calls duration are negative (Started timestamp is grater than Completion time)

### 3. Emails Sent
Table : vault.salesforce_task_mart

Query :
```
select distinct count(task_id)
from vault.salesforce_task_mart
where task_sub_type like '%mail' 
AND  task_status Like 'Completed';
```
**Issue**
Difference between Emails and Linked Emails. Which are to be counted?

### 4. Account type
Account type can be retrieved from data with key : 'Contact_Type__c'.

Tables: 

salesforce.contacts , 

salesforce.accounts

Query:
```
select * from salesforce.contacts;

select * from salesforce.accounts;
```
"Account_Type__c": "Supplier".

"Contact_Type__c": "Buyer",.

"Contact_Type__c": "Supplier"


### 5. Onboarding Done
Key :  Onboarding_done__c

Tables:

salesforce.accounts 

salesforce.contacts

Query:
```
select * from salesforce.contacts;
```


### 6.  Different Buyers/Suppliers Touched
The 'vault.salesforce_task_mart' contains **hash keys for Companyid, accountid**. 

Form here we can retrieve Buyers and suppliers that have been contacted via Call, mail, fax e.t.c



