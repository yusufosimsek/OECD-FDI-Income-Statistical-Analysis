import duckdb
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, text
import glob

# 1. Fetch CSV via DuckDB to drop phantom columns (column05, etc.)
files = glob.glob(r'c:\Users\Yusuf\Desktop\OECD-FDI-Income-Analysis\data\raw\*.csv')
if not files:
    print("CSV not found")
    exit(1)

file_path = files[0]
print("Loading original CSV...")
conn_duck = duckdb.connect()

# We know from the report that phantom columns follow a pattern "columnNN". We can just select real columns:
real_columns = [
    "STRUCTURE", "STRUCTURE_ID", "ACTION", "REF_AREA", "MEASURE", "UNIT_MEASURE", 
    "MEASURE_PRINCIPLE", "ACCOUNTING_ENTRY", "TYPE_ENTITY", "FDI_COMP", "SECTOR", 
    "COUNTERPART_AREA", "LEVEL_COUNTERPART", "ACTIVITY", "FREQ", "FDI_COLLECTION_ID", 
    "TIME_PERIOD", "OBS_VALUE", "OBS_STATUS", "UNIT_MULT", "CONF_STATUS", "CURRENCY", "DECIMALS"
]
cols_sql = ", ".join([f'"{c}"' for c in real_columns])
df = conn_duck.execute(f"SELECT {cols_sql} FROM read_csv_auto('{file_path}', delim=';', header=True, ignore_errors=True)").df()

print(f"Loaded DataFrame with shape: {df.shape}")

# 2. Upload to MS SQL Server
print("Connecting to MS SQL LocalDB...")
# Create Database OECD_FDI if it doesn't exist (must be done without transaction)
engine_master = create_engine('mssql+pyodbc://@(localdb)\\MSSQLLocalDB/master?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes')
with engine_master.connect() as con:
    con.execution_options(isolation_level="AUTOCOMMIT")
    res = con.execute(text("SELECT name FROM sys.databases WHERE name = 'OECD_FDI'")).fetchall()
    if not res:
        print("Creating OECD_FDI database...")
        con.execute(text("CREATE DATABASE OECD_FDI"))

# Connect to target DB
engine = create_engine('mssql+pyodbc://@(localdb)\\MSSQLLocalDB/OECD_FDI?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes', fast_executemany=True)

print("Publishing to SQL Server...")
df.to_sql('fdi_data', con=engine, if_exists='replace', index=False)
print("Data saved to fdi_data.")

# 3. Perform Type Casting via SQL execution directly
with engine.connect() as con:
    # OBS_VALUE becomes a strictly casted float (converting 'Oca.86' and '19.400...' naturally to NULL)
    print("Converting OBS_VALUE to Numeric via TRY_CAST...")
    con.execute(text("ALTER TABLE fdi_data ADD OBS_VALUE_NUM FLOAT;"))
    con.execute(text("UPDATE fdi_data SET OBS_VALUE_NUM = TRY_CAST(OBS_VALUE AS FLOAT);"))
    con.commit()

print("Schema conversions completed.")

