
import subprocess
import ftplib
import os

def task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    # Connect to FTP server
    try:
        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_user, ftp_password)
        ftp.cwd(ftp_dir)
    except Exception as e:
        raise Exception(f"Failed to connect to FTP server {ftp_server}: {str(e)}")

    # Download files from FTP server
    filenames = []
    for filename in ftp.nlst():
        try:
            with open(filename, 'wb') as f:
                ftp.retrbinary('RETR ' + filename, f.write)
            filenames.append(filename)
        except Exception as e:
            raise Exception(f"Failed to download file {filename} from FTP server {ftp_server}: {str(e)}")

    # Close FTP connection
    ftp.quit()

    return filenames