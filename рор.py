from OTXv2 import OTXv2, IndicatorTypes

# This is the API key for the user "api_example"
otx = OTXv2('8c3b1fd2add0a2325e7edd39eeb9a0e7cd577238a65fc83f67c4b1d2c08ee625')
pulses = otx.getall()
print('title,reference,created')

def clean(s):
    return s.replace(',','')

def cleanDate(s):
    return s.split('T')[0]

for i in range(0,len(pulses)-1):
    try:

        pulse = pulses[i]
        url = "https://otx.alienvault.com/pulse/" + pulse["id"]
        indicators = pulse["indicators"]
        references = pulse["references"]
        adversary = pulse["adversary"]
        title = clean(pulse["name"])
        created = cleanDate(pulse["created"])

        if references != None and adversary != None:
            if len(references) > 0 and len(adversary) > 0:
                reference = references[0]
                print(title + ',' + reference + ',' + created)
    except Exception as ex:
        pass
        #sprint str(ex)