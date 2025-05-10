import os
import shutil


print(r"""       _.-- ,.--.
     .'   .'     /
     | @       |'..--------._
    /      \._/              '.
   /  .-.-                     \
  (  /    \                     \
  \\      '.                  | #
   \\       \   -.           /
    :\       |    )._____.'   \
     "       |   /  \  |  \    )
             |   |./'  :__ \.-'
             '--'
             Made by Jeewan:)
""")

folder_path = '/home/appimage'
desktop_file_path = '/usr/share/applications'

try:
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder created successfully at: {folder_path}")
except PermissionError:
    print("Permission denied. Please run this script as root or with sufficient permissions.")
    input('Press ENTER to exit.')
    exit()

file_path = input("Select an AppImage file (provide the full path): ")

if file_path.lower().endswith('.appimage') and os.path.isfile(file_path):
    try:
        shutil.copy(file_path, folder_path)
        print(f"File copied successfully to: {folder_path}")

        app_name = input("Enter the application name: ")
        icon_path = input("Select an icon file (provide the full path): ")
        comment = input("Enter a brief description (comment): ")
        category = input("Enter a category (e.g., Development;IDE;): ")

        if not os.path.isfile(icon_path):
            print("Invalid icon file path. Exiting.")
            input('Press ENTER to exit.')
            exit()

        desktop_file_content = f"""[Desktop Entry]
Type=Application
Name={app_name}
Icon={icon_path}
Exec={os.path.join(folder_path, os.path.basename(file_path))}
Comment={comment}
Categories={category}
Terminal=false
"""
        desktop_file_name = f"{app_name}.desktop"
        desktop_file_full_path = os.path.join(desktop_file_path, desktop_file_name)

        try:
            with open(desktop_file_full_path, 'w') as desktop_file:
                desktop_file.write(desktop_file_content)
            print(f".desktop file created successfully at: {desktop_file_full_path}")
        except PermissionError:
            print("Permission denied. Please run this script as root or with sufficient permissions.")
        except Exception as e:
            print(f"An error occurred while creating the .desktop file: {e}")
    except PermissionError:
        print("Permission denied. Please run this script as root or with sufficient permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print("Please select a valid AppImage file.")

input('Press ENTER to exit.')