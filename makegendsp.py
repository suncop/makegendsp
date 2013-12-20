#!/usr/bin/env python

import json
import sys

fullname = sys.argv[1]

if fullname.endswith('.genexpr') is False :
	print('Not a .genexpr file!')
	quit()

shortname = fullname[:-8]

# add the first part of the .gendsp file:

gendsp_string = '{"patcher" : \n	{\n		"fileversion" : 1,\n		"appversion" : \n		{\n			"major" : 6,\n			"minor" : 1,\n			"revision" : 5,\n			"architecture" : "x86"\n		},\n\n		"rect" : [ 100.0, 100.0, 600.0, 450.0 ],\n		"bgcolor" : [ 0.9, 0.9, 0.9, 1.0 ],\n		"bglocked" : 0,\n		"openinpresentation" : 0,\n		"default_fontsize" : 12.0,\n		"default_fontface" : 0,\n		"default_fontname" : "Arial",\n		"gridonopen" : 0,\n		"gridsize" : [ 15.0, 15.0 ],\n		"gridsnaponopen" : 0,\n		"statusbarvisible" : 2,\n		"toolbarvisible" : 1,\n		"boxanimatetime" : 200,\n		"imprint" : 0,\n		"enablehscroll" : 1,\n		"enablevscroll" : 1,\n		"devicewidth" : 0.0,\n		"description" : "",\n		"digest" : "",\n		"tags" : "",\n		"boxes" : \n		[ 	\n'

# read the .genexpr file:

f = open(fullname, "r")
string1 = f.read()
f.close()

# determine how many inputs and outputs there are:

ins = 1
outs = 1
for i in range(2,65):
	if 'in{}'.format(i) in string1 and i > ins :
		ins = i
	if 'out{}'.format(i) in string1 and i > outs :
		outs = i

# determine the width of the codebox and the spacing for the in and out objects

if ins < 5 and outs < 5 :
	width = 200.0
elif ins > outs :
	width = ins * 50.0
else :
	width = outs * 50.0
if ins != 1:
	inspacing = (width-19)/(ins-1)
else :
	inspacing = 0;
if outs != 1 :
	outspacing = (width-19)/(outs-1)
else :
	outspacing = 0;

# generate the codebox object :

gendsp_string = gendsp_string + json.dumps({ 'box' : { 'code' : string1, 'fontname' : 'Arial', 'fontsize' : 12.0, 'id' : 'codebox1', 'maxclass' : 'codebox', 'numinlets' : ins, 'numoutlets' : outs, 'patching_rect' : [ 20, 50.0, width, 200.0 ] } },  sort_keys=True, indent=4)

# generate the in objects :

for i in range(ins):
	gendsp_string = gendsp_string + ',\n' + json.dumps({'box' : { 'fontname' : 'Arial', 'fontsize' : 12.0, 'id' : 'in{}'.format(i+1), 'maxclass' : 'newobj', 'numinlets' : 0, 'numoutlets' : 1, 'patching_rect' : [(20.0 + i*inspacing), 20.0, 35.0, 20.0], 'text' : 'in {}'.format(i+1)}}, sort_keys=True, indent=4)

# generate the out objects :

for i in range(outs):
	gendsp_string = gendsp_string + ',\n' + json.dumps({'box' : { 'fontname' : 'Arial', 'fontsize' : 12.0, 'id' : 'out{}'.format(i+1), 'maxclass' : 'newobj', 'numinlets' : 1, 'numoutlets' : 0, 'outlettype' : [ "" ],'patching_rect' : [(20.0 + i*outspacing), 260.0, 35.0, 20.0], 'text' : 'out {}'.format(i+1)}}, sort_keys=True, indent=4)

gendsp_string = gendsp_string + '],\n "lines" : [\n'

# generate the patch cords :

for i in range(ins) :
	gendsp_string = gendsp_string + json.dumps({ 'patchline' : { 'destination' : [ 'codebox1', i ], 'disabled' : 0, 'hidden' : 0, 'source' : ['in{}'.format(i+1), 0] } }, sort_keys=True, indent=4)
	if i != ins-1 :
		gendsp_string = gendsp_string + ',\n'

gendsp_string = gendsp_string + ',\n'

for i in range(outs) :
	gendsp_string = gendsp_string + json.dumps({ 'patchline' : { 'destination' : [ 'out{}'.format(i+1), 0], 'disabled' : 0, 'hidden' : 0, 'source' : [ 'codebox1', i] } }, sort_keys=True, indent=4)
	if i != outs-1 :
		gendsp_string = gendsp_string + ',\n'

# finish the file and write it

gendsp_string = gendsp_string + '\n]\n}\n}\n'

f = open('{}.gendsp'.format(shortname), "w")
f.write(gendsp_string)
f.close()