import sys
import cryptography.exceptions
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
import base64
from cryptography.hazmat.primitives import hashes

PEM = (b"""-----BEGIN RSA PRIVATE KEY-----
-----END RSA PRIVATE KEY-----""")

def via_pyopenssl_verify(message, digest="sha256"):
   with open('signature.sig', 'rb') as f:
      signature = base64.b64decode(f.read())
   public_key = load_pem_public_key(open('baekseok.pub', 'rb').read(),default_backend())
   # Perform the verification.
   try:
      ret =public_key.verify(
          signature,
          #b"plaintextMessage",
          message,
          padding.PSS(
             mgf = padding.MGF1(hashes.SHA256()),
             salt_length = padding.PSS.MAX_LENGTH,
          ),
          hashes.SHA256(),
      )
      print (ret)
      return ret 
   except cryptography.exceptions.InvalidSignature as e:
      print('ERROR: Payload and/or signature files failed verification!')


def via_pyopenssl_sign256(message, digest="sha256"):
    import OpenSSL
    with open('baekseok.pem', 'rb') as key_file:
        key = load_pem_private_key(
           key_file.read(),
           password = None,
           backend = default_backend(),
        )
    # Sign the payload file.
    sign = base64.b64encode(
       key.sign(
          message,
          padding.PSS(
             mgf = padding.MGF1(hashes.SHA256()),
             salt_length = padding.PSS.MAX_LENGTH,
          ),
          hashes.SHA256(),
      )
    )
    with open('signature.sig', 'wb') as f:
       f.write(sign)
    return sign

def via_openssl_keygen(message):
    import subprocess
    import tempfile
    with open("key1.pem", "wb+") as f:
       f.write(PEM)
       f.flush()
       p = subprocess.Popen("openssl genrsa -out " + f.name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate(input=message)
    if stderr or p.returncode != 0:
        print(stderr)

    with open("key1.pub", "wb+") as f:
       f.write(PEM)
       f.flush()
       p = subprocess.Popen("openssl rsa -in key1.pem -pubout > " + f.name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate(input=message)
    if stderr or p.returncode != 0:
        print(stderr)
    return stdout

def via_openssl_keygen2(id):
    import subprocess
    import tempfile
    with open(id+".pem", "wb+") as f:
       f.write(PEM)
       f.flush()
       p = subprocess.Popen("openssl genrsa -out " + f.name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate(input=message)
    if stderr or p.returncode != 0:
        print(stderr)

    with open(id+ ".pub", "wb+") as f1:
       f1.write(PEM)
       f1.flush()
       p = subprocess.Popen("openssl rsa -in " + f.name + " -pubout > " + f1.name, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    stdout, stderr = p.communicate(input=message)
    if stderr or p.returncode != 0:
        print(stderr)
    return stdout

if __name__ == "__main__":
    message = b"asdf"
    # via_openssl_keygen2("baekseok")
    #via_openssl_keygen(message)
    # print(via_pyopenssl_sign256(message, digest="sha256"))
    via_pyopenssl_verify(message, digest="sha256")
