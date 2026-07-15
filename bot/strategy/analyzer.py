from .models import Situation
def analyze(agent_view):
    hp=getattr(agent_view.self,'hp',100); max_hp=max(getattr(agent_view.self,'maxHp',100),1)
    ep=getattr(agent_view.self,'ep',100); max_ep=max(getattr(agent_view.self,'maxEp',100),1)
    enemies=len(getattr(agent_view,'visibleEnemies',[]) or [])
    loot=len(getattr(agent_view,'visibleLoot',[]) or [])
    turn=getattr(agent_view,'turn',0)
    phase='early' if turn<50 else 'mid' if turn<100 else 'late'
    return Situation(hp/max_hp,ep/max_ep,enemies,loot,False,0.0,phase)
