import phonenumbers

#Add your phone number
number='+910000000000'

#Find location of the phone number
from phonenumbers import geocoder
number=phonenumbers.parse(num ,"CH") #parse used to collect details of each digit #C-Country,H=History
print(geocoder.description_for_number(ch_number,'en'))


#Find the service provider
from phonenumbers import carrier
sevice=phonenumbers.parse(num,'RO')
print(carrier.name_for_number(ch_number,'en'))
