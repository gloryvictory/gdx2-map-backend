from datetime import datetime

from pydantic import BaseModel


class BaseTable(BaseModel):
    class Config:
        from_attributes = True


class S_FIELD(BaseTable):    
    id:         int
    year:       int
    tip:        str
    areaoil:    float
    nom:        int
    oil:        str
    gas:        str
    condensat:  str
    name_ru:    str
    oblast:     str
    stadia:     str
    note:       str
    istochnik:  str
    ftype:      str


class S_LU(BaseTable):
    id:         int 
    areaoil:    float
    area_lic:   str 
    year:       int 
    nom_zsngp:  int 
    nom_list:   str 
    nom:        int 
    data_start: str 
    data_end:   str 
    vid:        str 
    ftype:      str 
    name_rus:   str 
    anumber:    str 
    sostiyanie: str 
    priznak:    str 
    nom_lic:    str 
    head_nedro: str 
    oblast:     str 
    zngp:       str 
    nedropolz:  str 
    nedropol:   str 
    nom_urfo:   int 
    authority:  str 
    
        
class S_STA(BaseTable):
    id:         int
    web_uk_id:  str
    vid_iz:     str
    tgf:        str
    n_uk_tgf:   str
    n_uk_rosg:  str
    name_otch:  str
    name_otch1: str
    avts:       str
    god_nach:   str
    god_end:    str
    org_isp:    str
    in_n_tgf:   str
    in_n_rosg:  str
    nom_1000:   str
    method:     str
    scale:      str
    
class S_STL(BaseTable):  
    id:         int
    web_uk_id:  str
    vid_iz:     str
    tgf:        str
    n_uk_tgf:   str
    n_uk_rosg:  str
    name_otch:  str
    name_otch1: str
    avts:       str
    god_nach:   str
    god_end:    str
    org_isp:    str
    in_n_tgf:   str
    in_n_rosg:  str
    nom_1000:   str
    method:     str
    scale:      str
    

class S_STP(BaseTable):
    id:         int
    web_uk_id:  str
    vid_iz:     str
    tgf:        str
    n_uk_tgf:   str
    n_uk_rosg:  str
    name_otch:  str
    name_otch1: str
    avts:       str
    god_nach:   str
    god_end:    str
    org_isp:    str
    in_n_tgf:   str
    in_n_rosg:  str
    nom_1000:   str
    method:     str
    scale:      str

    