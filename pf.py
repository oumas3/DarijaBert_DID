import nbformat

notebook_path = "Arabert_fineTn.ipynb" 

# Load notebook
nb = nbformat.read(notebook_path, as_version=4)

# Remove any widgets metadata globally
nb['metadata'].pop('widgets', None)
for cell in nb['cells']:
    cell['metadata'].pop('widgets', None)

# Save the cleaned notebook
nbformat.write(nb, notebook_path)

print("Notebook cleaned. GitHub preview should work now.")
