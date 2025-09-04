# src/app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session, g, jsonify, Response
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np

app = Flask(__name__)
app.secret_key = 'e5b0b6ce3b7b2b3e8f2c9c5c4b6a7d9a2e3c4e5f6a7b8c9d'

@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/translator')
def translator():
    return render_template('translator.html')