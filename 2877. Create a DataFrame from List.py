import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    new_df = pd.DataFrame(student_data, columns = ["student_id","age"] )
    return new_df
    
