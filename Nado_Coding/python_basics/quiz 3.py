website = "http://google.com"

index1 = website.index("/") + 2

index2 = website.index(".")

website_name = website[index1:index2]

part_1 = website_name[:3]
part_2 = len(website_name)
part_3 = website_name.count("e")
part_4 = "!"

password = str(part_1) + str(part_2) + str(part_3) + str(part_4)

print(password)