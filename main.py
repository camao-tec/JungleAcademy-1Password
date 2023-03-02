# Connect Server needed https://github.com/1Password/connect
import onepasswordconnectsdk
import json

from onepasswordconnectsdk.client import (
    Client,
    new_client_from_environment,
    new_client
)

# creating client using environment variables
# OP_CONNECT_TOKEN = 1231289dahiu8zdhauzsd
# OP_CONNECT_HOST = http://localhost:8080
client: Client = new_client_from_environment()

print("Hello CAMAO!")

# Example get all accessable Vaults
get_all_vaults = client.get_vaults()
print("\nExample to get all accessable Vaults")
print(get_all_vaults)

# Example get vault by title and get its ID
vault_name = "JungleAcademy"
get_vault_id = client.get_vault_by_title(vault_name).id
print("\nExample get vault by title and get its ID")
print(get_vault_id)

# Example get full item with all attributes
item_title = "super_secret"
op_secret = client.get_item_by_title(item_title, get_vault_id)
print("\nExample get full item with all attributes")
print(op_secret)

# Example get single item, single attribute
op_attribute = op_secret.fields[1].value
print("\nExample get single item, single attribute")
print(op_attribute)