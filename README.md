### Hello there, I'm David - aka BMW330I 

## I am a Father, Pilot and DevSecOps Engineer
- I have onboarded a partner, Bing/ChatGPT are my copilots in my work efforts
- I am currently working on MS Azure Automation, with Ansible, projects
- I presently work for a large Health Insurance Company in Calif
- Fun fact:  I hold a USHPA P3 Paraglider Rating and also a private pilot

## Connect with me: 
- bmw330i@mac.com

## Advice: 
- Ansible Automation Platform is quite useful, very quick to learn if you know Python
- Download and learn to use the "thin" client instead of the "fat" installed binaries
- setup immediately an Oracle wallet and use it inside your scripts and Python. No more username/password, now /@[wallet_key], i.e. cx_Oracle.connect("/@ahost:1521/aservice") will get you in.
- Use EZConnect and free yourself from tnsnames.ora. Put the EZConnect strings as your wallet keys, i.e. mkstore -wrl $TNS_ADMIN -createCredential ahost:12521/aservice userxyz "the#passw0rd" 
- If you have special chars in the password use double quotes around the password [ see above use ]
- If you open cursors, close them, if you open a database connection, close it. Be a good client don't waste DB resources
- AskTom is an Oracle Savant, I add "AskTom" to all my searches and go first to his answers. Do yourself a favor and do the same, trust me.

## My Code explained
- datapump.py is a program to do export or import of a list of tables using Python callproc to DBMS_DATAPUMP. Some interesting things about it are that I use parallel, connect with an oracle wallet and am showing some real world usage. The expamples online I found were either one table or entire schema or full database etc. Often you want a list of tables and no metadata or table exist action etc. I am currently working on getting status from the job while running. In the meantime when I do this in my code I loop in a query of dbms_datapump_jobs for state of not NOT RUNNING [ i.e. executing or other processing ]. Then returning to my code as the job has completed or error'd out. 
