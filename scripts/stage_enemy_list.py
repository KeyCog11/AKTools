import os
import json
files = os.popen('find ./src/assets/data/en-US/gamedata/levels/obt/ -type f').read().split('\n')
filtered = ["training", "guide", "rune"]
file_list = []
enemy_stages = {}
stage_enemies = {}
for fname in files:
    if not any(word for word in filtered if word in fname):
        try:
            with open(fname, "r") as f:
                fdata = json.loads(f.read())
                stage_id = fname.split("/")[-1].split(".")[0]
                stage_enemies[stage_id] = []
                for e in fdata["enemyDbRefs"]:
                    eid = e["id"]
                    stage_enemies[stage_id].append(eid)
                    try: 
                        enemy_stages[eid].append(stage_id)
                    except:
                        enemy_stages[eid] = [stage_id]
                stage_enemies[stage_id] = sorted(stage_enemies[stage_id])
        except:
            continue
for i in enemy_stages:
    enemy_stages[i] = sorted(enemy_stages[i])

with open('./src/assets/processed/stage_enemies.json', "w") as se:
    se.write(json.dumps(stage_enemies))
with open('./src/assets/processed/enemy_stages.json', "w") as es:
    es.write(json.dumps(enemy_stages))
    
        
