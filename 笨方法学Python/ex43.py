import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/word.txt"
WORDs = []

PHRASES = {
	"class ###(###):":
	"Make a class named ### that is-a ###.",
	"class ###(object):\n\tdef __init__(self, ***)":
	"class ### has-a __init__ that takes self and *** parameters.",
	"class ###(object):\n\tdef ***(self, @@@)":
	"class ### has-a function named *** that takes self and @@@ parameters.",
	"*** = ###()":
	"Set *** to an instance of class ###.",
	"***.***(@@@)":
	"From *** get the *** function, and call it with parameters self, @@@.",
	"***.*** = '***'":
	"From *** get the *** attribute and set it to '***'."
	
}

# do they want to drill phrases first
PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
	PHRASES_FIRST = True
	
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDs.append(word.strip())
	
	
def convert(snippet, pharse):
	class_names = [w.capitalize() for w in
					random.sample(WORDs, snippet.count("###"))]
	other_names = random.sample(WORDs, snippet.count("***")
	result = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3)
		param_names.append(', '.join(random.sample(WORDs, param_count)))
		
	for sentence in snippet, pharse:
		result = sentence[:]
		
		# fake clase names
		for word in class_names:
			result = result.replase("###", word, 1)
			
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lisrs
		for word in param_names:
			result = result.replace("@@@", word, 1)