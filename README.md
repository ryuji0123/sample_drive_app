# sample_drive_app

This is a sample application to download files from Google Drive using oAuth. Currently, you can use this repo only on localhost not on remote server, docker, etc. 

## Dependency
- python (>= 3.8) # maybe python3 is enough

## Installation
```sh
$ git clone git@github.com:ryuji0123/sample_drive_app.git
$ cd sample_drive_app
$ chmod +x install.sh
$ ./install.sh
```

## Create token.pickle
1. Following [Python Quickstart](https://developers.google.com/drive/api/v3/quickstart/python), create credentials.json and put it into config dir.
1. Execute quickstart.py (I changed SCOPES to download files): 
``` sh
$ python quickstart.py 
```
and put token.pickle into config dir.

## Download files
1. Create your own yaml file in config, seeing config/sample.yaml. If you want to add params, you can modify config/defaults.py.
1. Execute download.py: 
``` sh
$ python download.py --cfg_file ./config/your_own.yaml
``` 
and you'll find the file in files dir.

## Sample Tree
```sh
.
├── LICENSE
├── README.md
├── config
│   ├── __init__.py
│   ├── credentials.json
│   ├── defaults.py
│   ├── parse_console.py
│   ├── sample.yaml
│   └── token.pickle
├── download.py
├── files
│   └── sample.pdf
├── install.sh
├── quickstart.py
└── requirements.txt
```

## References
- [Download files](https://developers.google.com/drive/api/v3/manage-downloads)
- [Google Workspace and Drive MIME Types](https://developers.google.com/drive/api/v3/mime-types)
- [How to write BytesIO content to file in Python](https://techoverflow.net/2019/07/24/how-to-write-bytesio-content-to-file-in-python/)
- [Python Quickstart](https://developers.google.com/drive/api/v3/quickstart/python)
