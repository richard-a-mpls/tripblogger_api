import imghdr
from swagger_server.models.photo import Photo
from PIL import Image
import math
import io
import os
from bson.binary import Binary
from swagger_server.models.photo import Photo

class FileTransformation:

    def transform(self, uploaded_file):
        header = uploaded_file.stream.read(512)
        uploaded_file.stream.seek(0)

        photo = Photo()
        photo.name = uploaded_file.filename
        photo.type = imghdr.what(None, header)
        photo.data = Binary(uploaded_file.stream.read());

        if os.fstat(uploaded_file.fileno()).st_size > 1000000:
            # need to size it down if it's over 1MB
            print ("reduce image size")

            img = Image.open(uploaded_file.stream)
            x, y = img.size
            print ("image size: " + str(x) + ":" + str(y))
            x2, y2 = math.floor(x / 8), math.floor(y / 8)
            img = img.resize((x2, y2), Image.ANTIALIAS)
            byte_io = io.BytesIO()
            #img.save(byte_io, quality=50)
            img.save(byte_io, format='PNG', quality=25)
            x, y = img.size
            print ("image size: " + str(x) + ":" + str(y))

            print ("storing image size: " + str(byte_io.getbuffer().nbytes/1024/1024) + " MB")
            photo.data = Binary(byte_io.getvalue())

        return photo
