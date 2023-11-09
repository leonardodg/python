def get_product_name(product_name: str):
    product_name_words = set(product_name.split(" "))

    cases = {
            "ALTOQI HUB": {"PLATAFORMA"},
            "AltoQi Eberick": {"EBERICK", "Eberick"},
            "AltoQi Builder": {"BUILDER", "Builder", "QIBUILDER", "QiBuilder"},
            "AltoQi Cloud": {
                                "CLOUD",
                                "Cloud",
                                "QICLOUD",
                                "QiCloud",
                                "Colaboração",
                                "Colaboracao",
                                "COLABORAÇÃO",
                                "COLABORACAO",
                                "Collab"
                            },
            "AltoQi Visus": {"VISUS", "Visus", "QIVISUS", "QiVisus"},
            "AltoQi Workflow": {"WORKFLOW", "Workflow", "workflow"},
        }

    for formatted_product_name, words in cases.items():
        if product_name_words.intersection(words):
            return formatted_product_name

    return product_name


if __name__ == '__main__':
    produts = {
                "ALTOQI HUB",
                "AltoQi Visus Collab",
                "ALTOQI VISUS ORÇAMENTISTA",
                "ALTOQI EBERICK 2021 PLENA",
                "AltoQi Visus Colaboração",
                "ALTOQI WORKFLOW",
                "BUILDER 2022 PLENA",
                "Builder Assinatura Enterprise CLOUD",
                "Builder Assinatura Infinity",
                "BUILDER BASIC",
                "BUILDER PLENA",
                "EBERICK 2022 PLENA",
                "EBERICK PLENA",
                "QIBUILDER 2021 PLENA",
                "QIVISUS ORÇAMENTO EM BIM 5D",
                "Builder Assinatura Infinity CLOUD",
                "Eberick Assinatura Infinity CLOUD",
                "Eberick Assinatura Infinity",
                "QIBUILDER 2020 PLENA",
                "Builder 2023 Infinity",
                "PLATAFORMA VISUS",
                "Eberick 2023 Infinity",
                "Eberick Assinatura Professional",
                "ALTOQI VISUS PROJETISTA",
                "Builder Assinatura Professional CLOUD",
                "AltoQi Visus Colaboração",
                }

    i = 1

    for prod in produts:
        result = get_product_name(product_name=prod)
        print(prod, " - ", result)
        print()
        i += 1
