import xml.etree.ElementTree as ET

# Открываем файл
tree = ET.parse('TextCheck.xml')

# Получаем корневой элемент
root = tree.getroot()

# Функция для рекурсивного обхода элементов XML и создания многомерного массива
def parse_element(element):
    result = {}
    result['name'] = element.attrib.get('name')
    result['format'] = element.attrib.get('format')
    result['Image_size'] = element.attrib.get('Image_size')
    result['folders'] = []
    for subelement in element:
        if subelement.tag == 'folder':
            result['folders'].append(parse_element(subelement))
    return result

# Обходим корневой элемент и получаем многомерный массив
result = []
for element in root:
    if element.tag == 'folder':
        result.append(parse_element(element))

# Выводим многомерный массив

print(result)
# Выводим информацию о папке "2.HP"
for folder in result:
    if folder['name'] == '2.HP':
        print(folder)