from ansible_vault import Vault
import os
ans_pass=os.getenv('ANSIBLE_PASSWORD')
vault=Vault(ans_pass)
secrets=vault.load(open('vault.yml').read())
print("The secret for user is: " + secrets['user'] + "\n" + "The secret for password is: " + secrets['password'] + "\n" + "The secret for the database endpoint is: " + secrets['dsn'])

