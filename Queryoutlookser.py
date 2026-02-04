import win32com.client

try:
    win32 = win32com
    outlook = win32.client.DispatchEx('Outlook.Application', 'HQQUA03030.rcen.marines.usmc.mil').GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 = Inbox folder
    print("Outlook is running and connected.")
    print(f"Inbox contains {inbox.Items.Count} items.")
except Exception as e:
    print("Cannot connect to Outlook:", e)
