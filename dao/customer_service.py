from util.DBConn import DBConnection
from exception.Exceptions import AuthenticationException

class CustomerService(DBConnection):

    def Authenticate(self, customerid, password):
        try:
            self.cursor.execute(
            """
                        select customerid,password from customer
                        where customerid=? and password=?
                       """,
            (customerid, password),
        )
            result = self.cursor.fetchone()
            if not result:
                raise AuthenticationException()
        except AuthenticationException as e:
            print(e)
        return result

    def GetCustomerById(self, custom_id):
        self.cursor.execute(
            """
                     select * from customer
                     where customerid = ?
                       """,
            (custom_id),
        )
        return self.cursor.fetchall()

    def GetCustomerByUsername(self, custom_name):
        self.cursor.execute(
            """
                       select * from customer
                       where Username = ?
                       """,
            (custom_name), 
        )
        return self.cursor.fetchall()

    def RegisterCustomer(
        self, cus_id, Firs_name, las_name, mail, Phon, addr, Usernam, passwo, reg_date
    ):
        self.cursor.execute(
            """
                            insert into Customer values(
                            ?,?,?,?,?,?,?,?,?                       
                            )
                       """,
            (cus_id, Firs_name, las_name, mail, Phon, addr, Usernam, passwo, reg_date),
        )
        self.conn.commit()

    def UpdateCustomer(self, phoon, addre, emai, cust_id):  # error
        self.cursor.execute(
            """
                       update customer set PhoneNumber=?,
                       Address= ?,
                       Email=?,
                       where CustomerID = ?

                       """,
            (phoon, addre, emai, cust_id),
        )
        self.conn.commit()

    def DeleteCustomer(self, custu_id):
        self.cursor.execute(
            """
                       delete from customer
                       where customerid= ?
                       """,
            (custu_id),
        )
        self.conn.commit()

    def display_all(self):
        self.cursor.execute(
            """
select* from customer
                       """
        )
        result = self.cursor.fetchall()
        return result