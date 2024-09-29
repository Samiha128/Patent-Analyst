from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


gauth = GoogleAuth()

gauth.settings['client_config_file'] = 'C:\\Users\\hp\\Desktop\\projet_machine_learning\\extraction_data\\client_secrets.json'

gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

file_id = '1akTSjzEB6vXSDc2HVX-wjQMEs8EyFiUtUf1XUfffNXc'
file_obj = drive.CreateFile({'id': file_id})

output_filename = 'FILE_NAME.xls'
try:
    file_obj.GetContentFile(output_filename, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    print(f"Contenu du fichier '{file_id}' téléchargé avec succès dans '{output_filename}'.")
except Exception as e:
    print(f"Erreur lors du téléchargement du fichier '{file_id}': {e}")
