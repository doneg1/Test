import xml.etree.ElementTree as ET

def check_xml(folder):
    pass

tree = ET.parse("TextCheck.xml")
root = tree.getroot()
root1 = root
# print((root[0]).tag)
for item in root1:
    if len(root1) > 0:
        root1 = root1[0]
        print(root1.tag)


print(root.tag)
    # for elem in root[0]:
    #     if elem.tag == "folder":
    #         print("ok")



# root = tree.getroot()
# print(root[0][0][0].tag)
# print(len(root[0][0]))



#
#
# tree = ET.parse('TextCheck.xml')
# root = tree.getroot()
#
# # for neighbor in root.iter('folder'):
# #     print(neighbor.attrib)
#
#
# for elem in root:
#     for subelem in elem.findall('folders'):
#         print(subelem.attrib)
#         print(subelem.get('name'))
#

#----------------------------------------------------
# for child in root:
#     print(child.tag, child.attrib)

# for rank in root.iter('rank'):
#     new_rank = int(rank.text) + 1
#     rank.text = str(new_rank)
#     rank.set('updated', 'yes')
#
# tree.write('output.xml')




















# ---------------------------------------------------------------
#print(ET.tostring(root, encoding='utf8').decode('utf8'))
# ---------------------------------------------------------------







#------------------------------------------------------


# import xml.etree.ElementTree as ET
#
# tree = ET.parse('TextCheck.xml')
# root = tree.getroot()
# for child in root.iter("folder"):
#     if "size" in child.attrib: !can find size!
#         print(child.attrib)

















