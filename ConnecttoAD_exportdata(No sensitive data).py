from ldap3 import Server, Connection, ALL, NTLM, SUBTREE
import csv
import getpass

# Server: 

# Global Catalog (port 3268, forest root base)
gc_server = '.:389' #'yourdc.yourforest.:3268'
base_dn = 'dc=, dc=, dc=usmc, dc='  # Forest root, not domain root
username = '''AD Username:''' r'\'
password = getpass.getpass('Password:')

# 2. Connect and bind
conn = ldap.initialize(f'ldap://FQDN DC/GC server')
conn.simple_bind_s('.', 'password')

# 3. Asyerrornc search 
'''ous = [
        'ou=12,ou=Districts,DC=,dc=,dc=usmc,dc='
        'ou=1,ou=Districts,DC=,dc=,dc=usmc,dc='
        'ou=4,ou=Districts,DC=,dc=,dc=usmc,dc='
        'ou=6,ou=Districts,DC=,dc=,dc=usmc,dc='
        'ou=8,ou=Districts,DC=,dc=,dc=usmc,dc='
        'ou=9,ou=Districts,DC=,dc=,dc=usmc,dc='
]
'''
msgid = conn.search(
    base_dn='ou=Districts,dc=yourforest,dc=', 
    ldap.SCOPE_SUBTREE,
    '( &(objectClass=user)(yourAttribute=yourSearchValue) )',  # Your case filter
    ['sAMAccountName', 'displayName', 'mail', 'department', '']  # GC-available attrs only)
results, _, _, _ = conn.result(msgid, timeout=30) # Collect when ready)

# Export to CSV
output_file = 'ad_users.csv'

with open(output_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    # header row
    writer.writerow(ATTRIBUTES)

    for entry in conn.entries:
        row = []
        for attr in ATTRIBUTES:
            value = getattr(entry, attr, None)
            if value is None:
                row.append('')
            else:
                # most AD attributes are lists; .value gives single / first value
                row.append(str(value.value))
        writer.writerow(row)

conn.unbind()
print(f"Exported {len(conn.entries)} entries to {output_file}")
