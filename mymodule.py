print("Modules start here");

def make_album(artist_name,album_title, num_of_tracks=""):
    """This function takes two mandatory parameters:
    artist_name,
    album_title, 
    and one optional parameter
    num_of_tracks
     
    it will return a  dictionary whose keys will be
    artist and album
    whose value will be the arguemnt provided by the user during function call
    """
    album_dic ={'artist':artist_name, 'album':album_title}
    if num_of_tracks:
        album_dic['tracks']=num_of_tracks
    return album_dic

def square_of_a_num(num):
    '''This function takes one mandatory parameter:
    number.
    
     it will return a square root'''
    square = num**2
    print('i am in the code')  # print before return
    return square , f"i am square of {num}"

def meter_to_km(distance_in_meters):
    distane_in_km = distance_in_meters/1000
    return distane_in_km
    
print("Modules interprated successfully..");       