def solution(T):
  counter = dict()
  for c in T:
    cs1 = c[1]+c[0]+c[2]
    cs2 = c[0]+c[2]+c[1]
    #all.append([c,cs1,cs2])
    done = dict()

    for x in (c, cs1, cs2):
      if x not in done.keys():
        if x in counter.keys():
          counter[x] += 1
        else:
          counter[x] = 1
      done[x] = 1

  return sorted(counter.items(), key=lambda kv: kv[1]).pop()[1]
