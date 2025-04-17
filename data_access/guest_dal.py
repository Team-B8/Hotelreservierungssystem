from data_access.base_dal import BaseDal
from model.guest import Guest
from model.booking import Booking

class GuestDal(BaseDal):
  def create_guest(self, guest_id:int, first_name:int, last_name:int, email:str):
    sql = """
      INSERT INTO Guest (guest_id, first_name, last_name, email)
      VALUES(?, ?, ?, ?)
    """
    params = (guest_id, first_name, last_name, email)
    last_id, _ = self.execute(sql, params)
    return Guest(last_id, guest_id, first_name, last_name, email)
    
