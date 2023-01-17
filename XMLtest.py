import xml.etree.ElementTree as ET

def check_xml(folder):
    pass


tree = ET.parse("TextCheck.xml")
root = tree.getroot()
sf = 0

myArray = []
print(len(root))
for elem in root:
    print("folder: " + elem.get("name"))
    folder_id = elem.get("name")
    myArray.append({'folder': folder_id})
    for item in root[sf]:
        print(item.get("name"))
    print("--------")
    sf += 1

    # invoice_id = elem.get('Invoice_ID')
    # invoice_owner_id = elem.get('Invoice_Owner_ID')
    # icn_id = elem.get('ICN_ID')
    # icn_owner_id = elem.get('ICN_Owner_ID')
    # receipt_date = elem.get('Receipt_Date')
    # myArray.append({'Invoice_ID': invoice_id, 'Invoice_Owner_ID': invoice_owner_id, 'ICN_ID': icn_id, 'ICN_Owner_ID': icn_owner_id, 'Receipt_Date': receipt_date})
print("----------------------------------------------------------------------")
for x in myArray:
    print(x)










# tree = ET.parse("TextCheck.xml")
# root = tree.getroot()
# root1 = root
# flag=1
# # print((root[0]).tag)
# for item in root1:
#     if len(root1) > 0:
#         root1 = root1[0]
#     flag *= len(item)
#     print(flag)


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

















