def deduplicate_latest(records:list[dict],key:str,updated_at:str)->list[dict]:
 latest={}
 for row in records:
  identity=row[key]
  if identity not in latest or row[updated_at]>latest[identity][updated_at]:latest[identity]=row
 return [latest[k] for k in sorted(latest)]
def sessionize(timestamps:list[int],gap_seconds:int=1800)->list[int]:
 sessions=[];session=0;previous=None
 for current in sorted(timestamps):
  if previous is None or current-previous>gap_seconds:session+=1
  sessions.append(session);previous=current
 return sessions