import os.path
import time
from base64 import b64encode, b64decode
from hashlib import sha1

def encode(str):
    return b64encode(str.encode("utf-8")).decode("utf-8")
def decode(str):
    return b64decode(str.encode("utf-8")).decode("utf-8")
def encode_sha1(str):
    return sha1(str).hexdigest()


def encode_upload_file(instance, filename):
    name = filename[:filename.rfind('.')]
    ext = filename[filename.rfind('.') + 1:]
    return 'uploads/file/{}.{}'.format(encode(name), ext)
def encode_upload_image(instance, filename):
    name = filename[:filename.rfind('.')]
    ext = filename[filename.rfind('.') + 1:]
    return 'uploads/image/{}.{}'.format(encode(name), ext)
def encode_upload_music(instance, filename):
    name = filename[:filename.rfind('.')]
    ext = filename[filename.rfind('.') + 1:]
    return 'uploads/music/{}.{}'.format(encode(name), ext)
def encode_upload_video(instance, filename):
    name = filename[:filename.rfind('.')]
    ext = filename[filename.rfind('.') + 1:]
    return 'uploads/video/{}.{}'.format(encode(name), ext)
def encode_upload_docs(instance, filename):
    name = filename[:filename.rfind('.')]
    ext = filename[filename.rfind('.') + 1:]
    return 'uploads/docs/{}.{}'.format(encode(name), ext)
def decode_upload_file(file):
    filename = file.open().name.split("/")[-1]
    name = filename[:filename.rfind('.')]
    ext = filename[filename.rfind('.') + 1:]
    return decode(name)

# def encode_upload_file(instance, filename):
#     ext = filename[filename.rfind('.') + 1:]
#     return 'uploads/file/{}.{}'.format(encode_sha1(instance.data.open().read()), ext)
# def encode_upload_image(instance, filename):
#     ext = filename[filename.rfind('.') + 1:]
#     return 'uploads/image/{}.{}'.format(encode_sha1(instance.data.open().read()), ext)
# def encode_upload_video(instance, filename):
#     ext = filename[filename.rfind('.') + 1:]
#     return 'uploads/video/{}.{}'.format(encode_sha1(instance.data.open().read()), ext)
# def encode_upload_docs(instance, filename):
#     ext = filename[filename.rfind('.') + 1:]
#     return 'uploads/docs/{}.{}'.format(encode_sha1(instance.data.open().read()), ext)


