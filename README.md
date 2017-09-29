# fileuploadaws
1. We need django 1.7 and python3.4 with boto==1.3.1 to run the project
2. After setting up the project, runserver.  python manage.py runserver
3. Go to browser and hit the link : http://localhost:8000/upload/
4. Select a file from location fileupload directory in the project. The file you want to upload should be present in fileupload directory of the project.
5. Click on upload. If file is uploaded successfully on aws server then File uploaded successfully message will be shown else uploading failed will be shown.
