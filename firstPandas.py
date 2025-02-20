import numpy as np
import pandas as pd

print(np.__version__)

testing = {
    "names" : ["John Paul", "Ed", "Ben"],
    "major": ["ECE", "AE", "MECH"]


}
df = pd.DataFrame(testing)
print(df)
