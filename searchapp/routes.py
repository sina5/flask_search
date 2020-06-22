# Programmer: Sina Fathi-Kazerooni
# Email: sina@sinafathi.com
# WWW: sinafathi.com 

from flask import render_template, flash, url_for
from searchapp import searchapp
from searchapp.forms import query_form

import numpy as np
import pandas as pd


arr = np.random.randint(1,500, (20,5))
arr = arr.astype('str')
df = pd.DataFrame(arr, columns=['a', 'b', 'c', 'd', 'e'])

@searchapp.route('/', methods=['GET', 'POST'])
@searchapp.route('/index', methods=['GET', 'POST'])
def index():
	form=query_form()
	row=[]
	if form.validate_on_submit(): # To check info when user inputs value into the form
		q = form.query.data
		row = list(df.loc[df['a'] == str(q)].values.tolist())
	
	return render_template('index.html', 
						title='Home', 
						df=list(df.values.tolist()),
						column_names = df.columns.values, 
						form=form,
						result=row, 
						zip=zip)
