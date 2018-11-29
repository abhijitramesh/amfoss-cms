# amFOSS Portal API 
The amFOSS portal supports `REST` API requests to get and post information on the portal. 

* The portal's API feature is powered by the `Django Rest Framework`  module
* API views, and urls are managed by the `API` app, and data serializers of models have
  been placed in their respective apps.
  

## API's Available

### Attendance API
API to post, and retrieve attendance records of members in the club 
```
<url>/api/attendance/
```

**GET: QUERY BY**
* **username** - Retrieve all attendance records of an individual member 

    ```
    <url>/api/attendance/?username=ashwin
    ```
*  **date** - Retrieve all attendance records from a date
     ```
     <url>/api/attendance/?date=23112018            #ddmmyyyy
     ```
* **batch** - Retrieve all attendance records of students belonging a particular batch 
              (batch year is the year of joining college)
    ```
    <url>/api/attendance/?batch=2018
    ```
* **year / month** - retrieve all attendance records from a given year/month
    ```
    <url>/api/attendance/?year=2018           # Yearly Register
    <url>/api/attendance/?month=11            # All Records in November
    <url>/api/attendance/?year=2018&month=11  # Monthly Register
    ```

### Profile API
API to retrieve member profile details
 ```
     <url>/api/profile/
 ```

**GET: QUERY BY**
*   **username** - Retrieve all details of an individual member

     ```
     <url>/api/profile/?username=ashwin
     ```
*   **birth_year / birth_month** - Retrieve profiles of members by their birth year / month
    ```
     <url>/api/profile/?birth_year=2000         # All members born in 2000
     <url>/api/profile/?birth_month=5           # All members born in May
     <url>/api/profile/?birth_month=2000&birth_year==2000  # All members born in May 2000
     ```
*   **location** - Retrieve profiles of members who are from the given location
    ```
     <url>/api/profile/?location=kochi               # All members from Kochi
     <url>/api/profile/?location=Andhra%20Pradesh    # All members from Andhra Pradesh
     ```
*   **interest** - Retrieve profiles of members who are interested in the given skill
    ```
     <url>/api/profile/?interest=cricket
     ```

*   **expertise** - Retrieve profiles of members who has expertise in the given skill
    ```
     <url>/api/profile/?expertise=django
     ```


### Responsibility API
API to retrieve club responsibilities assigned to various members

  ```
     <url>/api/responsibility
  ```
  
**GET: QUERY BY**
*   **username** - retrieve all responsibilities of an individual member

     ```
         <url>/api/responsibility/?username=ashwin
      ```
      
