# ---
# jupyter:
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# Add description here
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %%
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None


# %%
import os
product = {
    "nb": f"{os.getcwd()}/product/nb/get.ipynb",
    "data": f"{os.getcwd()}/product/data/data.csv"
}

# %%
from sklearn.datasets import load_iris
raw = load_iris(as_frame = True)

df = raw['data']
df['target'] = raw['target']

# Guardo datos
df.to_csv(product['data'],index=False)