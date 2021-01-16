# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.9.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import matplotlib.pyplot as plt
# %matplotlib inline
from IPython.display import display, set_matplotlib_formats
set_matplotlib_formats('png','pdf')

# %%
# %load_ext watermark
# %watermark

# %% tags=["parameters"]
PRINT=False


# %%
import pandas as pd
if PRINT:
    pd.options.plotting.backend = "matplotlib"
else:
    pd.options.plotting.backend = "plotly"

# %%
df = pd.read_excel("https://github.com/dionresearch/demo_data/blob/master/excel/iris.xlsx?raw=true")

# %%
df.describe(include='all').T

# %%
df.plot(kind='scatter',x='sepal_length',y='sepal_width')

# %%
