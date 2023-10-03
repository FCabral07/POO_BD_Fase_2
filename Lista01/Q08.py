import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

# Criando o elemento raiz
root = ET.Element("produtos")

# Definindo uma função para adicionar produtos
def adicionar_produto(id, nome, caracteristica):
    produto = ET.SubElement(root,   "produto")
    ET.SubElement(produto, "id").text = str(id)
    ET.SubElement(produto, "nome").text = nome
    for c in caracteristica:
        ET.SubElement(produto, "caracteristica").text = c
  
# Adicionando os produtos      
adicionar_produto(1, "PS5", ["Cor: Branco", "Modelo: PS1625", "Categoria: Eletronico", "Idade mínima: 6 anos", "Garantia: 1 ano"])
adicionar_produto(2, "Geladeira", ["Cor: Chumbo", "Modelo: Samsung FrostFree", "Categoria: Eletrodomestico", "Idade mínima: 14 anos", "Garantia: 3 anos"])

# Salvando o XML
xml_string = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")

with open("Q08.xml", "w") as xml_file:
    xml_file.write(xml_string)