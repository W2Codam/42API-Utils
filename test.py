from intra import ic
import enum

class Campus(enum.Enum):
	Vienna = 53
	Berlin = 51
	Kocaeli = 50
	Istanbul = 49
	Mulhouse = 48
	Lausanne = 47
	Barcelona = 46
	Alicante = 45
	Wolfsburg = 44
	Abu_Dhabi = 43
	Network = 42
	Nice = 41
	Urduliz = 40
	Heilbronn = 39
	Lisboa = 38
	Malaga = 37
	Adelaide = 36
	Amman = 35
	Kuala_Lumpur = 34
	Bangkok = 33
	Yerevan = 32
	Angouleme = 31
	Rome = 30
	Seoul = 29
	Rio_de_Janeiro = 28
	Hack_High_School_Fremont  = 27
	Tokyo = 26
	Quebec = 25
	Novosibirsk = 24
	Kazan = 23
	Madrid = 22
	Benguerir = 21
	SaoPaulo = 20
	CoderDojoSV = 19
	iTouchUP = 18
	Moscow = 17
	Khouribga = 16
	CapeTown = 15
	Amsterdam = 14
	Helsinki = 13
	Brussels = 12
	Montrouge = 11
	Bucharest = 10
	Lyon = 9
	Kyiv = 8
	Fremont = 7
	Chisinau = 6
	Johannesburg = 5
	Cluj = 2
	Paris = 1

# res = ic.getall("campus")
# for elem in res:
# 	print("{0} = {1}".format(elem['name'], elem['id']))

print(Campus['Vienna'].value)

