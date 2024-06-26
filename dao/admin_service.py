from exception.admin_not_found_exception import AdminNotFoundException
from exception.authentication_exception import AuthenticationException
from exception.database_connection_exception import DatabaseConnectionException
from util.DBConn import DBConnection

class AdminService(DBConnection):

    def GetAdminById(self,ad_id):
        try:
            self.cursor.execute("""
select * from Admin
                       where AdminID=?
                       """,(ad_id))
            details= self.cursor.fetchall()
            if len(details)==0:
                raise AdminNotFoundException()
            else:
                print(details)
        except Exception as e:
            print("oops an error..",e)

    def GetAdminByUsername(self,ad_name):
        self.cursor.execute("""select * from Admin
                       where Username=?""",(ad_name))
        return self.cursor.fetchall()

    def RegisterAdmin(self,add_id,firs_name,las_name,email,ph,usrnm,paswd,role,jndate):
        self.cursor.execute("""
insert into Admin values(?,?,?,?,?,?,?,?,?)
                       """,(add_id,firs_name,las_name,email,ph,usrnm,paswd,role,jndate))
        self.conn.commit()
        

    def UpdateAdmin(self,firs_namee,las_namee,emaill,phh,usrnmm,paswdd,rolee,jndatee,add_idd):
        self.cursor.execute("""
update Admin
                       set FirstName=?,
                       LastName=?,
                       Email=?,
                       PhoneNumber=?,
                       Username=?,
                       Password=?,
                       Role=?,
                       JoinDate=?
                       where AdminId=?
                       """,(firs_namee,las_namee,emaill,phh,usrnmm,paswdd,rolee,jndatee,add_idd))
        self.conn.commit()
        

    def DeleteAdmin(self,a_id):
        self.cursor.execute("""
                       delete from Admin 
                       where AdminID=?
                       """,(a_id))
        self.conn.commit()

    def view_admin(self):
        try:
            self.cursor.execute("""select * from Admin""")
            return self.cursor.fetchall()
        except Exception as e:
            raise DatabaseConnectionException() 
        
    def Authentication(self,admin_id,password):
        try:
            self.cursor.execute(
            """
                        select AdminID,Password from Admin
                        where AdminID=? and Password=?
                       """,
            (admin_id, password),
        )
            result = self.cursor.fetchone()
            if not result:
                raise AuthenticationException()
            print("Authentication successful!!")

        except AuthenticationException as e:
            print(e)
        return result


