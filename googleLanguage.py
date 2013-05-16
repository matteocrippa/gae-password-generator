from os import environ

def googleLanguage():
 try:
  lang = environ['HTTP_ACCEPT_LANGUAGE']
  lang = lang[0:2]
 except:
  lang= 'en'
 return ("""<script type="text/javascript" src="http://www.google.com/jsapi"></script>

    <script type="text/javascript">

    	google.load("language", "1");
		
		function translate()
		{
			txt=document.getElementById('content').innerHTML;
			google.language.translate(txt,'en','%s', function(result){ if(!result.error) document.getElementById('content').innerHTML=result.translation;});			
						
		}
		
		google.setOnLoadCallback(translate);
	</script>""" % lang)
	
def actualLanguage():
 if environ:
  lang = environ['HTTP_ACCEPT_LANGUAGE']
  return lang[0:2]