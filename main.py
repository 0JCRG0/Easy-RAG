import logging
from typing import Any
from pydantic import BaseModel
from unstructured.partition.pdf import partition_pdf

PATH = "/Users/juanreyesgarcia/Dev/Python/LLMSandbox/data/"

class Element(BaseModel):
    type: str
    text: Any


log_format = "%(asctime)s %(levelname)s: \n%(message)s\n"
logging.basicConfig(filename="logging.log", level=logging.INFO, format=log_format)


raw_pdf_elements = partition_pdf(
    filename=PATH + "llama2.pdf",
    extract_images_in_pdf=False,
    infer_table_structure=True,
    chunking_strategy="by_title",
    max_characters=4000,
    new_after_n_chars=3800,
    combine_text_under_n_chars=2000,
    image_output_dir_path=PATH,
)

print(raw_pdf_elements)

def inspect_raw_pdf_elements(raw_pdf_elements: list) -> tuple[dict, set, list, list]:
    category_counts = {}
    categorized_elements = []

    for element in raw_pdf_elements:
        category = str(type(element))
        if category in category_counts:
            category_counts[category] += 1
        elif category not in category_counts:
            category_counts[category] = 1
        elif "unstructured.documents.elements.Table" in str(type(element)):
            categorized_elements.append(Element(type="table", text=str(element)))
        elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
            categorized_elements.append(Element(type="text", text=str(element)))
        else:
            continue


    unique_categories = set(category_counts.keys())
    
    table_elements = [e for e in categorized_elements if e.type == "table"]
    print(len(table_elements))

    text_elements = [e for e in categorized_elements if e.type == "text"]
    print(len(text_elements))


    return category_counts, unique_categories, table_elements, text_elements




if __name__ == "__main__":
    print(inspect_raw_pdf_elements(raw_pdf_elements))