
import subprocess
import ftplib
import os
def task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    try:
        # Connect to the FTP server
        ftp = ftplib.ftp(ftp_server)
        ftp.login(ftp_user, ftp_password)
        
        # Change to the specified directory
        ftp.cwd(ftp_dir)
        
        # List files in the directory
        files = ftp.nlst()
        
        # Download all files
        downloaded_files = []
        for file_name in files:
            local_file_path = os.path.join(ftp_dir, file_name)
            subprocess.run(['wget', '-O', local_file_path, f'ftp://{ftp_server}/{ftp_dir}/{file_name}'])
            downloaded_files.append(file_name)
        
        return downloaded_files
    except ftplib.all_errors as e:
        raise Exception(f"Failed to connect to FTP server {ftp_server}: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to log into FTP server {ftp_server} with user {ftp_user}: {str(e)}")