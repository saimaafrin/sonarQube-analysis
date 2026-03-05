
import subprocess
import ftplib
import os

def task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    filenames = []
    try:
        # Connect to the FTP server
        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_user, ftp_password)
        print(f"Successfully connected to FTP server {ftp_server} and logged in with user {ftp_user}")
        
        # Change to the specified directory
        ftp.cwd(ftp_dir)
        print(f"Successfully changed to directory {ftp_dir} on server {ftp_server}")
        
        # List all files in the directory
        files = ftp.nlst()
        for file in files:
            filenames.append(file)
            # Construct the wget command to download the file
            wget_command = f"wget -O {file} ftp://{ftp_user}:{ftp_password}@{ftp_server}/{ftp_dir}/{file}"
            # Execute the wget command using subprocess
            subprocess.run(wget_command, shell=True, check=True)
            print(f"Successfully downloaded {file}")
    
    except ftplib.all_errors as e:
        if "FTP: error: connect" in str(e):
            raise Exception(f"Failed to connect to FTP server {ftp_server}: {str(e)}")
        elif "FTP: error: login" in str(e):
            raise Exception(f"Failed to log into FTP server {ftp_server} with user {ftp_user}: {str(e)}")
        elif "FTP: error: cwd" in str(e):
            raise Exception(f"Failed to change to directory {ftp_dir} on server {ftp_server}: {str(e)}")
        else:
            raise Exception(f"An unexpected error occurred: {str(e)}")
    
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to download file: {str(e)}")
    
    finally:
        # Close the FTP connection
        ftp.quit()
    
    return filenames