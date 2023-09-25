"""
topshiriqlar
ro`yxatlar ustida ishlash
"""

davlatlar= ["O`zbekiston",'Rossiya', 'Xitoy', 'Amerika', 'Germaniya']
print(len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse=True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

sonlar=list(range(120,1200,2))
print(sonlar)
print(sum(sonlar))

print(max(sonlar)-min(sonlar))
print(len(sonlar))

print(sonlar[:20])
print(sonlar[len(sonlar)//2:len(sonlar)//2+20])
print(sonlar[len(sonlar)-20:])


taomlar=['osh','sho`rva','msnti','jarkob', 'pilmin']
print(taomlar)
nounushta=taomlar[:]
nounushta.remove('osh')
nounushta.pop(1)
print(nounushta)
nounushta.append('tuxumvarak')
nounushta.append('do`lma')

nonushta=tuple(nounushta)
nonushta=list(nonushta)
nonushta[0]=('qaymoq va non')
nonushta=tuple(nonushta)
print(nonushta)