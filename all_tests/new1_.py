n = 1000

def odd_generator(n):
    list_of_odd = []

    for n in range(n*2):
        if n%2==1:
            list_of_odd.append(n)

    return list_of_odd

list_of_odd = odd_generator(n)
print(list_of_odd)


"""Whatsapp product->
    Auth Service->
        
        -> Authorize the user
        -> login the User(web/ ios)
        -> authtype -> business/ normal

    Search_service->
        -> searching the user
        -> 

    User Service->
        -> add_user
            -> preference
        -> add_status
        -> get_user
            -> user chat
            -> groups
        -> get_status

    Chat Service->
        -> user1 and user2
        -> group_id

    Data Service
    ->video/audio
        ->chat_ids
        ->groups_ids
"""

