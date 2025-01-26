import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    emp = employees.head(3)
    return emp
    
