import cx_Oracle
import os

def main():
    """Make an Oracle database connection using the Secure Wallet"""
    # we will need TNS_ADMIN value set let's do it
    wallet_loc = "/home/auser/wallet"
    os.setenv['TNS_ADMIN'] = wallet_loc
    # I have stored a credential in the wallet for my_ez_con_str value
    my_ez_con_str = localhost:12521/SAMPLEDB
    my_query      = """select version from v$instance"""
    # dbc,cur are just variables don't stress over the name
    dbc = cx_Oracle.connect("/@"+my_ez_con_str)
    cur = cx_Oracle.cursor()
    cur.execute(my_query)
    # Go to the Docs: https://cx-oracle.readthedocs.io/en/latest/
    print(cur.fetchone())
    cur.close()
    dbc.close()

if __name__ == '__main__':
    main()
