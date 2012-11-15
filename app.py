########################################################################
# Imports
########################################################################

import flask
import shutil
from flask import Flask, request, session, g, redirect, url_for, \
   abort, render_template, flash, Response
from contextlib import closing
import os

########################################################################
# Configuration
########################################################################

DEBUG = True
# create app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = '123bsdfwedfs'

task_dic = {} # name: task_list

@app.route('/todo', methods=['GET', 'POST'])
def todo():

  print request.form.get('delete')
  print request.form.get('add')
  # check if its a delete post
  if request.method == 'POST' and request.form.get('delete') and not request.form.get('add'):
    keep_list = []
    for task in task_dic[session['person']]:
      if request.form.get(task) == None:
        keep_list.append(task)
    task_dic[session['person']] = keep_list

  # check if its an add post
  if request.method == 'POST' and request.form.get('add'):
    task_dic[session['person']].append(request.form.get('task'))
  



  if session['person'] not in task_dic:
    task_dic[session['person']] = []
    
  return render_template('todo.html', name = session['person'], task_list = task_dic[session['person']])

@app.route('/', methods=['GET', 'POST'])
def main():
  if request.method == "POST":
    if request.form.get('person') not in session:
      session['person'] = request.form.get('person')
    return redirect(url_for('todo'))
  return render_template('main.html')

########################################################################
# Entry
########################################################################

if __name__ == '__main__':
  app.run()


