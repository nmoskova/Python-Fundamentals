version = "".join(input().split("."))
new_version = int(version) + 1
new_version_string = str(new_version)
new_version_list = list(new_version_string)

print(f"""{".".join(new_version_list)}""")

