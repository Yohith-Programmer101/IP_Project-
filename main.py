import pandas as pd
import numpy as np
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fiona', 'George', 'Hannah', 'Ian', 'Julia'],
    'Class': [10, 10, 11, 12, 11, 10, 12, 11, 12, 10],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F'],
    'Stream': ['Science', 'Commerce', 'Science', 'Arts', 'Science', 'Commerce', 'Arts', 'Science', 'Commerce', 'Arts'],
    'Address': [
        '12, Park St', '5B, River Rd', '22A, Maple Ave', '33C, Lake View', '9, Hill Rd',
        '17, Green Ln', '4D, Ocean Dr', '28, Sunset Blvd', '14B, Main St', '7, Pine Grove'
    ]
}
df = pd.DataFrame(data)
df.index = [f'R{i}' for i in range(1, len(df)+1)]
for (i, d) in df.iterrows():
    print(d["Class"])