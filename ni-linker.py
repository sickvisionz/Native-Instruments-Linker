import os
import xml.etree.ElementTree as ET
import winreg

def create_registry_entries(root_folder, xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()
    products = root.findall('Product')

    # Iterate through the folders in the root directory
    root_folders = os.listdir(root_folder)
    for folder_name in root_folders:
        folder_path = os.path.join(root_folder, folder_name)
        if os.path.isdir(folder_path):
            # Find the corresponding <Product> element in the XML file
            product_name = None
            product_element = None
            for product in products:
                product_name = product.find('Name').text
                # straight match?
                if product_name == folder_name:
                    product_element = product
                    break
                # library match?
                if product_name == folder_name.replace(' Library', ''):
                    product_element = product
                    break

            # Create the registry key if this folder is a product folder
            if product_element is not None:
                reg_key = product_element.find('RegKey').text
                key_path = r"SOFTWARE\Native Instruments\{0}".format(reg_key)
                try:
                    key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
                    winreg.SetValueEx(key, "ContentDir", 0, winreg.REG_SZ, folder_path)

                    HU = product_element.find('ProductSpecific/HU')
                    if HU is not None:
                        winreg.SetValueEx(key, "HU", 0, winreg.REG_SZ, HU.text)

                    JDX = product_element.find('ProductSpecific/JDX')
                    if JDX is not None:
                        winreg.SetValueEx(key, "JDX", 0, winreg.REG_SZ, JDX.text)

                    relevance_element = product_element.find('Relevance')
                    if relevance_element is not None:
                        winreg.SetValueEx(key, "ContentVersion", 0, winreg.REG_SZ, relevance_element.get('minVersion'))
                    else:
                        winreg.SetValueEx(key, "ContentVersion", 0, winreg.REG_SZ, "")

                    visibility_element = product_element.find('ProductSpecific/Visibility')
                    if visibility_element is not None:
                        winreg.SetValueEx(key, "Visibility", 0, winreg.REG_DWORD, int(visibility_element.text))
                    else:
                        winreg.SetValueEx(key, "Visibility", 0, winreg.REG_DWORD, 3)

                    winreg.CloseKey(key)
                    print(f"Created registry entry for {product_name}")
                except Exception as e:
                    print(f"Error creating registry entry for {product_name}: {e}")
            else:
                print(f'No matching <Product> element found for folder "{folder_name}"')

# Prompt the user for the root folder and XML file
root_folder = input("Enter the root folder path: ")
xml_file = input("Enter the XML file path: ")

# Create the registry entries
create_registry_entries(root_folder, xml_file)

# Save the registry entries to a .reg file
with open("registry_entries.reg", "w") as reg_file:
    reg_file.write("Windows Registry Editor Version 5.00\n\n")
    reg_file.write(r"[HKEY_LOCAL_MACHINE\SOFTWARE\Native Instruments]" + "\n")
