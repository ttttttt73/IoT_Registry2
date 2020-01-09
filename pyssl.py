import os
from OpenSSL import crypto as c
from OpenSSL._util import lib as cryptolib

certFileName = "key.pem"

if os.path.exists(certFileName):
    cert_data = open(certFileName).read()
    # open certificate
    cert = c.load_certificate(c.FILETYPE_PEM, cert_data)

pkey = cert.get_pubkey()
# pkey.generate_key(c.TYPE_RSA, 2048)

def pem_publickey(pkey):
    """Format a public key as a PEM"""
    bio = c._new_mem_buf()
    cryptolib.PEM_write_bio_PUBKEY(bio, pkey._pkey)
    return c._bio_to_string(bio)