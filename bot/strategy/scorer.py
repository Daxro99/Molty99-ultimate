def score(s):
    d={'heal':0,'attack':0,'loot':0,'explore':0,'retreat':0}
    if s.hp_percent<0.3:
        d['heal']+=100; d['retreat']+=80
    if s.enemy_count==0:
        d['loot']+=80; d['explore']+=60
    if s.loot_count:
        d['loot']+=30
    if s.phase=='late':
        d['retreat']+=30
    return d
