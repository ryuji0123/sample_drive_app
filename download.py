import io
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from config import update_args, parse_arguments


def main(args):
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None

    # put token.pickle in config
    if os.path.exists('./config/token.pickle'):
        with open('./config/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    else:
        raise Exception('Please put token.pickle in config dir.')

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    request = service.files().export_media(
            fileId=args.DOWNLOAD.FILE_ID,
            mimeType=args.DOWNLOAD.MIME_TYPE,
            )
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    with open(args.DOWNLOAD.FILE_PATH, 'wb') as f:
        f.write(fh.getbuffer())

if __name__ == '__main__':
    option = parse_arguments()
    args = update_args(cfg_file=option.cfg_file)
    main(args)
