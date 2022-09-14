#!/usr/bin/env python3
# encoding: utf-8
"""Demonstrates how to implement an API for an HSM"""

from mtls import *
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from flask import Flask, jsonify, request
from flask_json import FlaskJSON, as_json

app = Flask(__name__)
json = FlaskJSON(app)
next_key_id = 0

chosen_hash = hashes.SHA256()
mypad = padding.PSS(mgf=padding.MGF1(chosen_hash), salt_length=padding.PSS.MAX_LENGTH)

users = dict()

class User:
    def __init__(self, uid, sym_key, asym_key):
        self.uid = uid
        self.sym_key = sym_key
        self.asym_key = asym_key


@app.route('/')
def index():
    return "This is an API with following Endpoints: \n- /create_user\n- /encrypt/USER_ID\n/decrypt/USER_ID\n- /sign/USER_ID\n-/verify/USER_ID"


@as_json
@app.route("/create_user", methods=['POST', 'GET'])
def create_user():
    return dict(key_id=_create_user())


@as_json
@app.route("/encrypt/<int:user_id>", methods=['POST', 'GET'])
def encrypt(user_id):
    """Encrypts given plaintext and returns ciphertext, with 16 byte tag appended, and nonce"""
    pass

@as_json
@app.route("/decrypt/<int:user_id>", methods=['POST', 'GET'])
def decrypt(user_id):
    """Decrypts given ciphertext with given nonce"""
    pass

@as_json
@app.route("/sign/<int:user_id>", methods=['POST', 'GET'])
def sign(user_id):
    """Signs given data with users master key"""
    pass

@as_json
@app.route("/verify/<int:user_id>", methods=['POST', 'GET'])
def verify(user_id):
    """Verifies given signature with users master key"""
    pass

def _create_user():
    pass

_create_user()
app.run(debug=True, port=5001, ssl_context='adhoc')
