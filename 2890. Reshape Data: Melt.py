import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    melt_report = pd.melt(report,id_vars = 'product', var_name= 'quarter', value_name = 'sales')
    return melt_report
    
