
import subprocess
import ftplib
import os

def task_func(ftp_server='ftp.dlptest.com', ftp_user='dlpuser', ftp_password='rNrKYTX9g7z3RgJRmxWuGHbeu', ftp_dir='/ftp/test'):
    try:
        with ftplib.FTP(ftp_server) as ftp:
            ftp.login(ftp_user, ftp_password)
            ftp.cwd(ftp_dir)
            filenames = []
            for filename in ftp.get_welcome_message():
                filenames.append(filename)
            return filenames
    except Exception as e:
        raise Exception(f"Failed to connect to FTP server {ftp_server}: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to log into FTP server {ftp_server} with user {ftp_user}: {str(e)}")
    except Exception as e:
        raise Exception(f"Failed to change to directory {ftp_dir} on server {ftp_server}: {str(e)}")