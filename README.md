### Hello there, I'm David - aka **BMW330I**

## I am a Father, Pilot and DevSecOps Engineer
- There is a new partner for my work: **Grok**
- Working with Ansible YAML, and Python for **MS Azure Automation**
- Working as a DevSecOps Engineer, **Azure, PaaS, IaaS mostly**, SQLDB, MySQL, PostgreSQL
- Fun fact:  **USHPA P3 Paraglider, and Private Pilot Certified**

## Connect with me: 
- [bmw330i@mac.com](mailto:bmw330i@mac.com)

## Advice: 
- Get to know AI, pick any, my choice is **Grok**. Good partner who won't tell you you ask too many questions.
- **JSON, Python and JavaScript** are indispensable tools. 
- Be humble, always give credit to those who gave you the ideas when you are praised, flattered.
- SQLDB is quite easy to interact with in Python using **pyodbc**, trusted connections are also easy to get working
- **Microsoft Online Training** is very helpful, take advantage and learn online as much as you can

## My Code explained
- **datapump.py** is a program to do export or import of a list of tables using Python `callproc` to `DBMS_DATAPUMP`.

  - Some interesting things about it are:
    - I use **parallel** processing
    - Connect with an **Oracle wallet**
    - Show some real world usage. The examples online I found were either one table or entire schema or full database etc. Often you want a list of tables and no metadata or table exist action etc. 
    - I am currently working on getting status from the job while running. In the meantime when I do this in my code I loop in a query of `dbms_datapump_jobs` for state of not **NOT RUNNING** [i.e. executing or other processing]. Then returning to my code as the job has completed or error'd out.
