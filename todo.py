import json
with open('data/userdata.json', 'r', encoding = "utf8") as f:
    data = json.load(f)
mm={"幹你娘","去你的","操你媽","去你媽","靠北","我操"}
    
def helps():
    return "```k.當開頭\n\njoin:加入所在語音頻道\nleave:叫他滾\nhi:跟他說hi\n好喔:好喔\n```||幹你娘:幹你娘||"

def levelch(count,level):
    if count <50:
        return 1,False
    elif level*50-50>=0:
        if count>=level*50:
            return level+1,True
        else:
            return level,False
        
def mch(tx):
    if tx in mm:
        return True
def lvch(user):
    temp=data[f"{user}"]
    level=temp['level']
    count=temp['saytime']-(level-1)*50
    ch=level*50
    return f"你現在等級是:{level}\n經驗值還差:{count}/{ch}"
        
def save(user):
    try:
        temp=data[f"{user}"]
        count=temp['saytime']+1
    except:
        count=1
    temp=data[f"{user}"]
    levelc=temp['level']
    level=levelch(count,levelc)
    
    userdata = {
    f"{user}": {
        "id": f"{user.id}",
        "username": f"{user.name}",
        "saytime": count,
        "level": level[0]
    }
    }
    data.update(userdata)
    with open("data/userdata.json", "w") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    return level[1]
