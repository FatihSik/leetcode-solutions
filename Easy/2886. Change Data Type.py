import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.assign(grade = [int(x) for x in students['grade']])

    ''' from solutions could use the attribute .astype()

        return students.assign(grade = students['grade'].astype('int64'))
        
        it is also faster to use students.grade rather than students['grade'] '''
