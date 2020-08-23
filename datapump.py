import os
import cx_Oracle

def export_table():
    """Export all tables in a list, using parallel 4"""
    global ez_conn_str, dbc, table_list, schema_name
    
    dump_file = "our_dumpfile_%U.dmp"
    dump_log  = "our_tumpfile.log"
    para_val  = 4
    dbc       = cx_Oracle.connect("/@"+ez_conn_str)
    cur       = dbc.cursor()
    job_parm  = dict(job_name=dbms_job_name, operation='EXPORT', job_mode='TABLE', version=dbms_job_vers)
    try:
        job_handler = cur.callfunc('DBMS_DATAPUMP.OPEN', keywordParameters=job_parm, returnType=cx_Oracle.NUMBER)
    except cs_Oracle.DatabaseError as e:
        print(e)
        return
    params_beg = dict(handle=job_handler, skip_current=0, abort_step=0)
    params_log = dict(handle=job_handler, filename=dump_log,  directory='DATA_PUMP_DIR', filetype=3, reusefile=1) 
    params_dmp = dict(handle=job_handler, filename=dump_file, directory='DATA_PUMP_DIR', filetype=1, reusefile=1) 
    params_scm = dict(handle=job_handler, name='SCHEMA_LIST', value=schema_name)
    params_tab = dict(handle=job_handler, name='NAME_LIST',   value=table_list) 
    params_par = dict(handle=job_handler, degree=para_val) 
    cur.callproc('DBMS_DATAPUMP.ADD_FILE',        keywordParameters=params_log)
    cur.callproc('DBMS_DATAPUMP.ADD_FILE',        keywordParameters=params_dmp)
    cur.callproc('DBMS_DATAPUMP.METADATA_FILTER', keywordParameters=params_scm)
    cur.callproc('DBMS_DATAPUMP.METADATA_FILTER', keywordParameters=params_tab)
    cur.callproc('DBMS_DATAPUMP.SET_PARALLEL',    keywordParameters=params_par)
    cur.callproc('DBMS_DATAPUMP.START_JOB',       keywordParameters=params_beg)


def import_table():
    """Import all tables in a list, using parallel 4, data only"""
    global ez_conn_str, dbc, table_list, schema_name
    
    dump_file = "our_dumpfile_%U.dmp"
    dump_log  = "our_tumpfile.log"
    para_val  = 4
    dbc       = cx_Oracle.connect("/@"+ez_conn_str)
    cur       = dbc.cursor()
    job_parm  = dict(job_name=dbms_job_name, operation='IMPORT', job_mode='TABLE', version=dbms_job_vers)
    try:
        job_handler = cur.callfunc('DBMS_DATAPUMP.OPEN', keywordParameters=job_parm, returnType=cx_Oracle.NUMBER)
    except cs_Oracle.DatabaseError as e:
        print(e)
        return
    params_beg = dict(handle=job_handler, skip_current=0, abort_step=0)
    params_log = dict(handle=job_handler, filename=dump_log,  directory='DATA_PUMP_DIR', filetype=3, reusefile=1) 
    params_dmp = dict(handle=job_handler, filename=dump_file, directory='DATA_PUMP_DIR') 
    params_scm = dict(handle=job_handler, name='SCHEMA_LIST', value=schema_name)
    params_tab = dict(handle=job_handler, name='NAME_LIST',   value=table_list) 
    params_par = dict(handle=job_handler, degree=para_val) 
    params_tea = dict(handle=job_handler, name='TABLE_EXISTS_ACTION', value='TRUNCATE')
    params_mta = dict(handle=job_handler, name='INCLUDE_METADATA',    value=0)
    cur.callproc('DBMS_DATAPUMP.ADD_FILE',        keywordParameters=params_log)
    cur.callproc('DBMS_DATAPUMP.ADD_FILE',        keywordParameters=params_dmp)
    cur.callproc('DBMS_DATAPUMP.METADATA_FILTER', keywordParameters=params_scm)
    cur.callproc('DBMS_DATAPUMP.METADATA_FILTER', keywordParameters=params_tab)
    cur.callproc('DBMS_DATAPUMP.SET_PARALLEL',    keywordParameters=params_par)
    cur.callproc('DBMS_DATAPUMP.SET_PARAMETER',   keywordParameters=params_tea)
    cur.callproc('DBMS_DATAPUMP.SET_PARAMETER',   keywordParameters=params_mta)
    cur.callproc('DBMS_DATAPUMP.START_JOB',       keywordParameters=params_beg)

def main():
    """Mainline program for export or importing using dbms_datapump"""
    global ez_conn_str, dbc 
    usage       = "USAGE: "+sys.arg[0]+" -e|-i [ e=export and i=import ]"
    table_list  = "'table1','table2','tablen'" 
    schema_name = "'WWOMAN'"
    oracle_wallet_log =  "/home/oracle/wallet"
    os.environ['TNS_ADMIN'] = oracle_wallet_loc
    try: 
        dbc       = cx_Oracle.connect("/@"+ez_conn_str)
    except cx_Oracle.DatabaseError as e: 
        error,    = e.args
        if error.code == 1017:
            print("You gave invalid credentials")
        else: 
            print("A Database Error happened")
        exit()
    if sys.argv[1] == '-e'   
        export_table()
    elif sys.argv[1] == '-i'
        import_table()
    else:
        print(usage)
        exit()