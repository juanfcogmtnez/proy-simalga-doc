from docxtpl import DocxTemplate

doc = DocxTemplate("rapport.docx")
context = { 		'mes_m':'Nocembre',
					'mes': 'NOVEMBRE',
					'ano': '2021',}
tipo = 'rapport'
mes = context.get('mes') 
ano = context.get('ano') 
archivo = 'rapport/'+tipo+'_'+mes+'_'+ano+'.docx'
doc.render(context)
doc.save(archivo)
