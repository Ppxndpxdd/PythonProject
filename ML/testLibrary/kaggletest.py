import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(
    "/PythonProject/ML/dataset/english.csv",
    dtype={"image": pd.StringDtype(), "label": pd.CategoricalDtype()}
)
img = mpimg.imread("/PythonProject/ML/dataset/" + df.at[473, "image"])
plt.imshow(img)