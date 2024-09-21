prviucenikmetri=int(input("unesite metre 1. djaka do skole: "))
prviucenikvreme=int(input("koliko vremena treba do skole(u minutima): "))
drugiucenikmetri=int(input("unesite metre 2. djaka do skole: "))
drugiucenikvreme=int(input("koliko vremena treba do skole(u minutima): "))
sekunde1=prviucenikvreme*60
sekunde2=drugiucenikvreme*60
v1=prviucenikmetri/sekunde1
v2=drugiucenikmetri/sekunde2
print("prvi ucenik se krece brzinom od", v1,"metara u sekundi")
print("drugi ucenik se krece brzinom od", v2,"metara u sekundi")
if(v1>v2):
    print("prvi decak se krece brze za", v1-v2,"metara u sekundi")
else:
    print("drugi decak se krece brze za", v2-v1,"metara u sekundi")
