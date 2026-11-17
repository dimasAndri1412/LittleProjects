import os
from dotenv import load_dotenv

load_dotenv()

ConnectToDBLocal = {
    "host":os.getenv("DB_SERVER"),
    "port":os.getenv("DB_PORT"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASSWORD"),
    "database":"DataSourceDistributor",
}


#SOR ReconciliationConfig
ConnectToDBReconciliationConfig = {
    "host":os.getenv("DB_DEV_S0R1_SERVER"),
    "port":os.getenv("DB_DEV_S0R1_PORT"),
    "user":os.getenv("DB_DEV_S0R1_USER"),
    "password":os.getenv("DB_DEV_S0R1_PASSWORD"),
    "database":"ReconciliationConfig",
}

#SOR ParamEngine
ConnectToDBParamEngine = {
    "host":os.getenv("DB_DEV_S0R2_SERVER"),
    "port":os.getenv("DB_DEV_S0R2_PORT"),
    "user":os.getenv("DB_DEV_S0R2_USER"),
    "password":os.getenv("DB_DEV_S0R2_PASSWORD"),
    "database":"ParamEngine",
}