import xml.etree.ElementTree as ET
import pandas as pd
import csv

df_columns = ['symkar', 'ean', 'cena_promocyjna',
              'cena', 'rabat', 'cena_promocyjna_netto', 'cena_netto', 'url']
rows = []

input_file = 'source/CUSTOM_1012_pl.xml'
output_file = 'result/result.csv'

# TODO: policz rabat


def run():
    tree = ET.parse(input_file)
    root = tree.getroot()
    for product in root:
        symkar = product.find('symkar').text
        ean = product.find('ean').text

        cena_promocyjna = product.find('price').text
        cena = product.find('basePrice').text
        cena_promocyjna_netto = product.find('priceNet').text
        cena_netto = product.find('basePriceNet').text

        rabat = round((float(cena) - float(cena_promocyjna)) / float(cena), 2)

        url = product.find('url').text.strip()

        rows.append([symkar, ean, cena_promocyjna, cena, rabat,
                    cena_promocyjna_netto, cena_netto, url])

    out_df = pd.DataFrame(rows, columns=df_columns)
    out_df.to_csv(output_file, index=False,
                  encoding='utf-8', quoting=csv.QUOTE_ALL)


if __name__ == "__main__":
    run()
