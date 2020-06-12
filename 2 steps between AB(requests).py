import requests
from lxml import html

first_link = input()
second_link = input()

def gettheref(ref): # using lxml lib
    try:
        parsed_body_in = html.fromstring(ref.text) #reforming a body of the doc into tree of elements (DOM)
        ref_inside = parsed_body_in.xpath('//a/@href') # now we can get the list of references from the inside of the given doc
        return ref_inside 
    except:
        return [] # if no refs were found return []

def IfRefInside(url1, url2): # to check if we can get from url1 to url2 with exactly 2 steps
    ref1 = requests.get(url1)
    if ref1.status_code == 200: #if no mistakes
        ref_inside = gettheref(ref1) # getting the list of founded links/references

        for i in ref_inside: # for each item in list
            ref_in = requests.get(i)
            if ref_in.status_code == 200:
                ref_inside2 = gettheref(ref_in)# get the link/links that are in the item
            if url2 in ref_inside2: #check if any of them match utl2
                return 'Yes'
    return 'No'

print(IfRefInside(first_link, second_link))