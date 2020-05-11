from django.shortcuts import render, get_object_or_404
from .models import Forms, Languages, About
from .tables import LanguagesTable, LanguageDetailTable
import pandas as pd
from collections import defaultdict, OrderedDict
from string import ascii_uppercase
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json
import re
import random

#import django_tables2 as tables
# django_tables2 test
#from django_tables2 import SingleTableView


class DefaultListOrderedDict(OrderedDict):
	def __missing__(self, k):
		self[k] = []
		return self[k]

# Create your views here.
def home(request):
	# get terms
	terms_list = []
	while(len(terms_list) < 6):
		# pick a language at random
		languages = list(Languages.objects.values('id', 'name'))
		random_language = random.choice(list(languages))
		terms = Forms.objects.filter(parameter_id__in = ['mF', 'mM', 'meB', 'meZ', 'myB', 'myZ'], language_id = random_language['id'], form__isnull=False).values('parameter_id', 'form')
		terms_list = list(terms)
		terms_list = list({t['parameter_id']:t for t in terms_list}.values())
	
	terms_list.append({'language_name': random_language['name']})
	print(terms_list)
	terms_json = json.dumps(terms_list, cls=DjangoJSONEncoder)
	return render(request, 'kb/home.html', {'terms': terms_json})

# def home(request):
# 	counts = Forms.objects.all().values('parameter_id').annotate(total=Count('parameter_id'))
# 	counts_list = list(counts)

# 	# subset to parameters in the graphic
# 	counts_subset = [c['parameter_id'] for c in counts_list if re.match(r'^(f|m)', c['parameter_id'])]

# 	# sum across male and female speakers
# 	counts_list = []
# 	for c in counts_subset:
# 		print(c['total'])
# 		base_id = re.sub(r'^(f|m)', '', c['parameter_id'])
# 		matching_ids = [c2 for c2 in counts_list if c2['parameter_id'] == base_id]
# 		totals = [m['total'] for m in matching_ids]
# 		new_total = sum(totals)
# 		counts_list.append({'parameter_id': base_id, 'total': new_total})

# 	counts_json = json.dumps(counts_list, cls=DjangoJSONEncoder)
# 	return render(request, 'kb/home.html', {'counts': counts_json})

# for list of languages
# class LanguagesTable(SingleTableView):
# 	model = Languages
# 	table_class = LanguagesTable
# 	template_name = 'kb/languages.html'


# def languages(request):
# 	language = Languages.objects.values().order('name')
# 	return render(request, 'kb/languages.html', {'languages': language})


def languages(request):
	"""Culture Index"""
	locations = []
	cultures = []
	for c in Languages.objects.values('name', 'glottocode').distinct():
		# if c['name']:
		#     for e in c['name'].split('; '):
		#         if len(e) > 0:
		#             cultures.append({'culture': e}) #, 'slug': c.slug
		cultures.append({'culture': c['name'], 'glottocode': c['glottocode']}) #, 'slug': c.slug
		#cultures.sort()
		cultures.sort(key=lambda x: x['culture'], reverse=False)

		lat = Languages.objects.filter(name=c['name']).values_list('latitude', flat=True)[0]
		longi = Languages.objects.filter(name=c['name']).values_list('latitude', flat=True)[0]

		if lat is not None and longi is not None:
		    locations.append(
		        {"lat": lat, "long": longi, "culture": c['name']}) # , "slug": c.slug

	ethonymDict = DefaultListOrderedDict()
	for a in ascii_uppercase:
		ethonymDict[a].append(None)
	for d in cultures:
		ethonymDict[d['culture'][0]].append(d)

	return render(request, 
		'kb/languages.html',
		{'ethonyms': OrderedDict(ethonymDict), 'latlong': locations}
		)

# -- Functions for Language detail -- # 
# def PrettyLanguageDetail(df):
#     #df = df[df.glottocode == pk]
# 	df = pd.DataFrame(df)

# 	## Seperate M & F speakers
# 	# F Speakers
# 	f_speaker = df[df['parameter_id'].str.contains(r'^f')]
# 	f_speaker = f_speaker[['language_id', 'form', 'comment', 'source', 'parameter_id']]
# 	f_speaker['parameter'] = f_speaker['parameter_id'].str[1:]

# 	# M Speakers
# 	m_speaker = df[df['parameter_id'].str.contains(r'^m')]
# 	m_speaker = m_speaker[['language_id', 'form', 'comment', 'source', 'parameter_id']]
# 	m_speaker['parameter'] = m_speaker['parameter_id'].str[1:]


# 	display_table = pd.merge(f_speaker, m_speaker, on='parameter', how='outer')

# 	display_table = display_table[['parameter', 'form_x', 'form_y', 'source_x', 'source_y']]
# 	# display_table = display_table[['parameter', 'form_x', 'form_y']]

# 	source = []
# 	for index, row in display_table.iterrows():
# 	    if row['source_x'] == row['source_y']:
# 	    	source.append(row['source_x'])
# 	    if row['source_x'] is None:
# 	    	source.append(row['source_y'])
# 	    if row['source_y'] is None:
# 	    	source.append(row['source_x'])
# 	    else:
# 	    	source.append("what?")
# 	    	#source.append(row["source_x"] + "; " + row["source_y"])

# 	#print(source.shape())

# 	display_table['source'] = pd.Series(source)
# 	del display_table['source_x']
# 	del display_table['source_y']
# 	display_table.columns = [['kin_category', 'woman_speaking', 'man_speaking', 'source']]
# 	#display_table.columns = [['kin_category', 'woman_speaking', 'man_speaking']]

# 	return(display_table)

# for languages detail
def language_detail(request, pk):
	table = LanguageDetailTable(Forms.objects.filter(glottocode=pk).values())

	return render(request, "kb/language_detail.html", {
		"table": table
	})

def phylogeny(request):
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/phylogeny.html', {'test': n_languages})

def about(request): 
	about = About.objects.all()
	n_languages = Forms.objects.values('language_id').distinct().count()
	return render(request, 'kb/about.html', {'about': about, 'n_languages' : n_languages})




