# Demo 1Password Connect and Python Project

Repository for Jungle Academy Presentation from 03.03.2023

## Connect Server
[docs](https://github.com/1Password/connect#create-server-and-access-token)
1. Create Secrets Automation Integration (In UI or CLI)
   1. `op connect server create <name> --vaults <vault>[,<vault>]`
1. Get 1password-credentials.json (put it in .secret/1password-credentials.json or adjust path in docker-compose)
2. Mount JSON to Connect Server
3. Run Connect Server

## Using Connect Server
[docs](https://github.com/1Password/connect#create-server-and-access-token)
1. Issue token for auth against connect server (In UI or CLI)
   1. `op connect token create <token_name> --server <server_name> --vaults <vault_uuid>[,(r|w|rw)]`
2. Add as env variable or simply pass it into script "OP_CONNECT_TOKEN"
3. Go!



Sources:
- https://github.com/1Password/connect-sdk-python
- https://github.com/1Password/connect
- https://github.com/1Password/connect/blob/main/examples/docker/compose/docker-compose.yaml