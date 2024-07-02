import firebase_admin
from firebase_admin import credentials, db, storage

if not firebase_admin._apps:
        cred = credentials.Certificate("credentials.json") 
        firebase_admin.initialize_app(cred, {"databaseURL": "https://limble-30e8a-default-rtdb.asia-southeast1.firebasedatabase.app/"})

def add_user(user_data,user_type):
    ref = db.reference('/')
    user_ref = ref.child(user_type) #or mentee
    user_ref.push().set(user_data)
    print(f"New {user_type} added successfully.")

def check_user(user_type,email,pwd):
    if not firebase_admin._apps:
        cred = credentials.Certificate("credentials.json") 
        firebase_admin.initialize_app(cred, {"databaseURL": "https://limble-30e8a-default-rtdb.asia-southeast1.firebasedatabase.app/",'storageBucket': 'limble-30e8a.appspot.com'})
    ref = db.reference('/')
    user_ref = ref.child(user_type) #or mentee
    details=user_ref.get()
    flag=0
    for i in details:
        if email==details[i]["email"] and pwd==details[i]["password"]:
            flag=1
            name=details[i]["name"]
            mentee_details=details[i]      
    if flag==1:
        return [True,name,mentee_details]
    else:
        return [False]

def link(file):
    if not firebase_admin._apps:
        cred = credentials.Certificate("credentials.json") 
        firebase_admin.initialize_app(cred, {'storageBucket': 'your-storage-bucket-name.appspot.com'})  # Replace with your bucket name
    bucket = storage.bucket(name='limble-30e8a.appspot.com')
    blob = bucket.blob(file.filename)
    blob.upload_from_string(file.read(), content_type=file.content_type)
    blob.make_public()
    return blob.public_url