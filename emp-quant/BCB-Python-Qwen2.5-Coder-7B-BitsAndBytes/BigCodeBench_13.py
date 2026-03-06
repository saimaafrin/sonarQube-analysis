
import subprocess
import ftplib
import os

def task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_server)
        ftp.login(user=ftp_user, passwd=ftp_password)
        
        # Change to the specified directory
        ftp.cwd(ftp_dir)
        
        # List all files in the directory
        files = ftp.nlst()
        
        # Create a temporary directory to store downloaded files
        temp_dir = 'temp_ftp_files'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
        
        # Download each file using wget
        downloaded_files = []
        for file in files:
            local_file_path = os.path.join(temp_dir, file)
            command = f'wget -O {local_file_path} ftp://{ftp_user}:{ftp_password}@{ftp_server}/{ftp_dir}/{file}'
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                downloaded_files.append(file)
            else:
                print(f"Failed to download {file}: {result.stderr}")
        
        # Close the FTP connection
        ftp.quit()
        
        return downloaded_files
    
    except ftplib.all_errors as e:
        if 'FTP error:' in str(e):
            raise Exception(f"Failed to connect to FTP server {ftp_server}: {str(e)}")
        elif 'Login failed' in str(e):
            raise Exception(f"Failed to log into FTP server {ftp_server} with user {ftp_user}: {str(e)}")
        elif 'No such file or directory' in str(e):
            raise Exception(f"Failed to change to directory {ftp_dir} on server {ftp_server}: {str(e)}")
        else:
            raise Exception(f"An unexpected FTP error occurred: {str(e)}")
    
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {str(e)}")