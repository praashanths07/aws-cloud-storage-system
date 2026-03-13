import boto3

s3 = boto3.client('s3')
bucket = "prashanth-cloud-storage"

def upload_file():
    file = input("Enter file name to upload: ")
    s3.upload_file(file, bucket, file)
    print("File uploaded successfully")

def list_files():
    response = s3.list_objects_v2(Bucket=bucket)

    if 'Contents' in response:
        for obj in response['Contents']:
            print(obj['Key'])
    else:
        print("No files found")

def download_file():
    file = input("Enter file name to download: ")
    s3.download_file(bucket, file, file)
    print("File downloaded")

def delete_file():
    file = input("Enter file name to delete: ")
    s3.delete_object(Bucket=bucket, Key=file)
    print("File deleted")

while True:
    print("\nCloud Storage System")
    print("1 Upload File")
    print("2 List Files")
    print("3 Download File")
    print("4 Delete File")
    print("5 Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        upload_file()
    elif choice == "2":
        list_files()
    elif choice == "3":
        download_file()
    elif choice == "4":
        delete_file()
    elif choice == "5":
        break
