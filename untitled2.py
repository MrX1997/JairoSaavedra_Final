import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = np.array([['','Col1','Col2'],
                ['Row1',1,2],
                ['Row2',3,4]])
                
print(pd.DataFrame(data=data,
                  index=[1,2,0],
                  columns=[1,0,1]))

    
