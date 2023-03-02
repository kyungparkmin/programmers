def solution(id_pw, db):
    for id, pw in db:
        if id_pw[0] in id:
            if id_pw[1] == pw:
                return 'login'
            else:
                return 'wrong pw'   
    return 'fail'
            
        
    
        


print(solution(["programmer01", "15789"], [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))