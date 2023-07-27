import sys
import nbformat as nbf

nb = nbf.v4.new_notebook()

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Import""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""import lab
import lab.plot
import lab.data
import lab.mmath as mmath
import lab.utils as utils
import lab.arr as arr
import lab.linfit as lf
import lab.constants as const
import lab.utils as utils
from lab.unit import unit as u
from uncertainties import ufloat
import matplotlib.pyplot as plt
print("Import done!")""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Read data""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""data = lab.data.Data("../data/data.csv")
data.head(5)""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Texify primary data""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""utils.totex(data)""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Add values""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""r_hg = ufloat(13550, 1) * u.kg / u.m ** 3
r_w = ufloat(1000, 1) * u.kg / u.m ** 3
g = ufloat(9.8154, 1e-4) * u.m / u.s ** 2
dh = ufloat(8.4, 0.0025) * u.cm
r_hg, r_w, g, dh""")]


nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Compute""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""data["p"] = ((data["h1"] - data["h2"]) * r_hg * g - r_w * g * dh).ito(u.Pa)
data["1/T"] = data["T"] ** -1
data["lnp"] = mmath.log(data["p"].m)
data.df.head(5)""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Plot""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""p1 = lab.plot.Plot(yl="$P$", xl="$T$")
p1.plot(data["T"], data["p"], fmt=".")""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""p2 = lab.plot.Plot(yl="$\\\\ln P$", xl="$1/T$")
p2.plot(data["1/T"], data["lnp"], fmt=".")""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Linear fit""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""k1, b1 = lf.chi2(data["T"], data["p"])
k2, b2 = lf.chi2(data["1/T"], data["lnp"])
print(f"k1 = {k1}\\nk2 = {k2}")
print(f"b1 = {b1}\\nb2 = {b2}")""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Plot lines and save""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""p1.line(k1, b1, color="black")
p1.save("../img/plot1.png")""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""p2.line(k2, b2, color="black")
p2.save("../img/plot2.png")""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Result""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""L1 = const.R * data["T"].arr.mean() ** 2 / data["p"].arr.mean() * k1
L2 = -const.R * k2
print(f"L1 = {L1}\\nL2 = {L2}")""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""utils.totex(L1)
utils.totex(L2)""")]

nb["cells"] += [nbf.v4.new_markdown_cell(
"""# Texify intermediate data""")]

nb["cells"] += [nbf.v4.new_code_cell(
"""utils.totex(data, columns={
    "T": "T",
    "h1": "h_1",
    "h2": "h_2",
    "p": "P",
    "1/T": "T^{-1}",
    "lnp": "\ln P",
})""")]

# write notebook
with open(sys.argv[1] + ".ipynb", "w", encoding="utf-8") as f:
    nbf.write(nb, f)

