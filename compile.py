import os
import glob
import subprocess

proto_dir = "object_detection/protos"

protoc_path = r"C:\Users\NEGRESCO\OneDrive - IFRN\Projects\TCC\protoc-30.1-win64\bin\protoc"

for proto_file in glob.glob(os.path.join(proto_dir, "*.proto")):
    command = [protoc_path, "--python_out=.", proto_file]
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error compiling {proto_file}: {result.stderr}")
    else:
        print(f"Successfully compiled {proto_file}")