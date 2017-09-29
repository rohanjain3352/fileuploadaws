import os, sys
import math
import boto
from filechunkio import FileChunkIO
from boto.s3.connection import S3Connection


def upload_file(s3, bucketname, file_path):
    b = s3.get_bucket(bucketname)
    file_path.seek(0, os.SEEK_END)
    file_length = file_path.tell()
    filename = file_path.name
    k = b.new_key(filename)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    filepath = ROOT_DIR + '/' + filename
    mp = b.initiate_multipart_upload(filename)

    source_size = os.stat(filepath).st_size
    bytes_per_chunk = 10000 * 1024 * 1024
    chunks_count = int(math.ceil(source_size / float(bytes_per_chunk)))

    for i in range(chunks_count):
        offset = i * bytes_per_chunk
        remaining_bytes = source_size - offset
        bytes = min([bytes_per_chunk, remaining_bytes])
        part_num = i + 1

        print("uploading part" + str(part_num) + " of " + str(chunks_count))
        with FileChunkIO(filepath, 'r', offset=offset,
                         bytes=bytes) as fp:
            fp.seek(offset)
            mp.upload_part_from_file(fp=fp, part_num=part_num, size=bytes)

    if len(mp.get_all_parts()) == chunks_count:
        mp.complete_upload()
        text = "File Uploaded Successfully"
    else:
        mp.cancel_upload()
        text = "Uploading Failed"
    return text