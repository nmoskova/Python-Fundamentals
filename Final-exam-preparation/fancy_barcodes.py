import re

count_barcodes = int(input())
pattern = r"(^)@#+(?P<barcode>[A-Z][A-Za-z\d]{4,}[A-Z])@#+($)"
matches = []
pattern_digits = r"\d"


for _ in range(count_barcodes):
    barcode = input()
    check_for_match = re.match(pattern, barcode)

    if check_for_match is not None:

        for match in re.finditer(pattern, barcode):
            barcode = match.group('barcode')
            pr_group = ""

            for ch in barcode:
                if ch.isdigit():
                    pr_group += ch

            if pr_group == "":
                print("Product group: 00")
            else:
                print(f"Product group: {pr_group}")

    else:
        print("Invalid barcode")






