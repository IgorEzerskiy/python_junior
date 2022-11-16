def find_lingerie(size_it: str) -> dict:
    lingerie = {"1": {"EUR": "34-36", "RUS": "40-42", "Standart": "XS"},
                "2": {"EUR": "38", "RUS": "44", "Standart": "S"},
                "3": {"EUR": "40", "RUS": "46", "Standart": "M"},
                "4": {"EUR": "42", "RUS": "48", "Standart": "L"},
                "5": {"EUR": "44", "RUS": "50", "Standart": "XL"},
                "6": {"EUR": "46", "RUS": "52", "Standart": "2XL"},
                "7": {"EUR": "48", "RUS": "54", "Standart": "3XL"},
                "8": {"EUR": "50", "RUS": "56", "Standart": "4XL"},
                "9": {"EUR": "52", "RUS": "58", "Standart": "5XL"},
                "10": {"EUR": "54", "RUS": "60", "Standart": "6XL"},
                "11": {"EUR": "56", "RUS": "62", "Standart": "7XL"}}
    for k, v in lingerie.items():
        if str(size_it) == k:
            return v


size_it = int(input("Wrtite your internetional size: "))
if (size_it <= 11) and (size_it > 0):
    print(find_lingerie(size_it))
else:
    print("This is not size of lingerie!!!")
