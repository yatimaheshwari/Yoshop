import nbformat
from nbconvert import HTMLExporter
import pdfkit
import os
import re

#NEW CODE START

def convert_ipynb_to_pdf2(ipynb_file, pdf_file, selected_cell_tags, generateDebugHtml = False):
    # Read the ipynb file
    with open(ipynb_file, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, nbformat.NO_CONVERT)

    # Configure the HTMLExporter
    html_exporter = HTMLExporter()
    html_exporter.exclude_input_prompt = True
    html_exporter.exclude_output_prompt = True

    # Filter the notebook cells to include only markdown and code cells with outputs
    filtered_cells = []
    for cell in nb.cells:
        if any(tag in cell.get('metadata', {}).get('tags', []) for tag in selected_cell_tags):
            if cell.cell_type == 'markdown':
                filtered_cells.append(cell)
            elif cell.cell_type == 'code':
                output_cell = nbformat.v4.new_code_cell(outputs=cell['outputs'])
                filtered_cells.append(output_cell)

    # Create a new notebook with filtered cells
    filtered_nb = nbformat.v4.new_notebook(cells=filtered_cells)

    # Convert the filtered notebook to HTML
    body, resources = html_exporter.from_notebook_node(filtered_nb)

    # Remove <pre> tag elements
    body_without_pre = re.sub(r'<pre>.*?</pre>', '', body, flags=re.DOTALL)

    # Customize the CSS style to remove scroll bars and control content size
    style = """
    <style>
    body {
        overflow: hidden;
        margin: 1rem;
        padding: 1rem;
        width: 100%;
        height: 100%;
    }

    .output_area img, .output_area svg {
        max-width: 100%;
        max-height: 100%;
    }

    .output_area pre {
        white-space: pre-wrap;
        word-wrap: break-word;
    }

    pre {
        display: none
    }

    </style>
    """
    body_with_style = style + body_without_pre

    # Convert HTML with customized style to PDF using pdfkit
    options = {
        'page-size': 'Letter',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
    }

    if(generateDebugHtml):
        # Save the HTML content to a file
        html_file = os.path.splitext(pdf_file)[0] + '.html'
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(body_with_style)
        print(f"HTML file '{html_file}' created successfully.")

    pdfkit.from_string(body_with_style, pdf_file, options=options)

    print(f"PDF file '{pdf_file}' created successfully.")


#NEW CODE END

