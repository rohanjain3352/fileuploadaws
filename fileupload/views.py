from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from . import utils
import requests
import os
import inspect
import boto



class Upload(APIView):
    """
    To Upload large files
    """


    def post(self, request):
        """
        Uploading File
        """
        template_name = 'upload.html'
        file = request.FILES['myfile']
        AWS_ACCESS_KEY_ID = 'AKIAJ4WDB3IY3BMOQ5JA'
        AWS_SECRET_ACCESS_KEY = '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'
        REGION_HOST = 's3.ap-south-1.amazonaws.com'

        # conn = S3Connection((AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
        s3 = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, host=REGION_HOST)

        res = utils.upload_file(s3, 'rohan3352', file)
        return render(request,template_name,{'message':res})
