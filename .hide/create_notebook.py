import sys
import nbformat
from notebook import transutils as _
from notebook.services.contents.filemanager import FileContentsManager as FCM

try:
    notebook_fname = sys.argv[1].strip('.ipynb')
except IndexError:
    print("Usage: create-notebook <notebook>")
    exit()

notebook_fname += '.ipynb'  # ensure .ipynb suffix is added
FCM().new(path=notebook_fname)

# read
with open(notebook_fname) as f:
    nb = nbformat.read(f, as_version=4)

# add import cell
nb["cells"] += [nbformat.v4.new_code_cell(
"""import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("https://raw.githubusercontent.com/LeonidPilyugin/mpl-style/main/simple.mplstyle")
print("Import done!")""")]

# add polyfit cell
nb["cells"] += [nbformat.v4.new_code_cell(
"""def polyfit(x, y):
    pp, V = np.polyfit(x, y, 1, cov=True)
    k, b = pp
    k_err, b_err = np.sqrt(V[0][0]), np.sqrt(V[1][1])
    return k, b, k_err, b_err""")]

# add read data cell
nb["cells"] += [nbformat.v4.new_code_cell(
"""data = pd.read_csv("../data/data.csv")
data""")]

# add plot cell
nb["cells"] += [nbformat.v4.new_code_cell(
"""# set data
x = np.linspace(-5, 5, 10)
y = x ** 2 * ((np.random.rand(10) - 0.5) * 0.1 + 1.0)
x = x ** 2

# polyfit
k, b, kerr, berr = polyfit(x, y)
print(f"k = {k} +/- {kerr}\\nb = {b} +/- {berr}")

# plot data
plt.errorbar(x, y, xerr=0.0, yerr=0.0, fmt=".")
plt.axline([min(x), min(x) * k + b], [max(x), max(x) * k + b], color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Title")
plt.savefig("../img/plot.png")""")]

# add dump cell
nb["cells"] += [nbformat.v4.new_code_cell(
"""data.to_csv("../data/data.csv", index=False)""")]

# write notebook
with open(notebook_fname, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)


