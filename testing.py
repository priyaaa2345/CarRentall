import unittest
from dao.customer_service import CustomerService
from dao.vehicle_service import VehicleService
from entity.customer import Customer
from entity.vehicle import Vehicle
from exception.authentication_exception import AuthenticationException

class TestCustomerService(unittest.TestCase):
    def setUp(self):
        self.customer_service = CustomerService()
# # 1)
    def test_customer_authentication_with_invalid_credentials(self):
        # Arrange
        customer_id = 1
        invalid_password = "day"

        # Act
        authentication_result = self.customer_service.Authenticate(customer_id, invalid_password)

        # Assert

        self.assertFalse(authentication_result, " invalid credentials.")

#    #2) 
    def test_update_customer_information(self):
        # for creating..
        self.customer_service.RegisterCustomer(
            16,"kavya","rocky","jkadhir@gmail.com",3434827882,'wes st,kanput',"jjays","rasd","2022-03-01"
           
        )
       
        self.customer_service.UpdateCustomer(
            222222,"Ras st,chennai","summa@gmail.com",16   
        )

        # # Assert: Retrieving the data to check if itsi true...
        updated_customer = self.customer_service.GetCustomerById(16)
        if updated_customer:
            self.assertEqual(updated_customer[5], "Ras st,chennai")
            self.assertEqual(updated_customer[3], "summa@gmail.com")
        else:
            self.fail("Customer with ID 16 not found")
        
    def tearDown(self):
    
        self.customer_service.DeleteCustomer(16)

      




#3) 4)Test1::

class TestVehicleService(unittest.TestCase):

    # def setUp(self):
    #     self.vehicle_service = VehicleService()

    # # def test_add_vehice(self):
    #     added_vehicle=self.vehicle_service.AddVehicle(113, "Series", "Audi", 2018, "blue", 33, 1, 5000)
    #     print("Vehicle 113 added successfully.")
    #     self.assertEqual(added_vehicle[1], "Series")  # Availability
    #     self.assertEqual(added_vehicle[2], "Audi") 

    # def tearDown(self):
    #     self.vehicle_service.RemoveVehicle(113)
    #     print("Vehicle 112 removed successfully.")

    # def test_update_vehicle(self):
    #     print("Running test_update_vehicle")

    #     self.vehicle_service.UpdateVehicle(6000, 0, 113)
    #     print("Vehicle 112 updated successfully.")

    #     retrieved_vehicle = self.vehicle_service.GetVehicleById(113)

    #     self.assertIsNotNone(retrieved_vehicle, "Vehicle not found in database after updating.")
    #     self.assertEqual(retrieved_vehicle[6], 0)  # Availability
    #     self.assertEqual(retrieved_vehicle[7], 6000)  # DailyRate
        
    # def tearDown(self):
    #     self.vehicle_service.RemoveVehicle(113)


#op is fine but not exactt..::
#3) 4)
        def setUp(self):
            self.vehicle_service = VehicleService()

            print("Adding a new vehicle🚗")
            add_success = self.vehicle_service.AddVehicle(112, "Series", "Audi", 2018, "blue", 12323, 1, 5000)
            self.assertTrue(add_success, "Added")

        def tearDown(self):

            remove_success = self.vehicle_service.RemoveVehicle(112)
            self.assertTrue(remove_success, "Failed to remove vehicle")

        def test_update_vehicle(self):
            print("Running test_update_vehicle")

            update_success = self.vehicle_service.UpdateVehicle(6000, 0, 112)
            self.assertTrue(update_success, "Failed to update vehicle.")

            retrieved_vehicle = self.vehicle_service.GetVehicleById(112)

            # Assert: 
            self.assertIsNotNone(retrieved_vehicle, "Vehicle not found in database after updating.")
            self.assertEqual(retrieved_vehicle[6], 0)  # Availability
            self.assertEqual(retrieved_vehicle[7], 6000)  # DailyRate








#5) 6)

        def test_get_available_vehicles(self):
            vehicles = self.vehicle_service.GetAvailableVehicles()

            self.assertEqual(len(vehicles),7)  #len value needs to be changed because we are adding vehicles on top..



        def test_get_all_vehicles(self):
            all_vehicles = self.vehicle_service.GetAllVehicles()

            self.assertTrue(all_vehicles, "The list of all vehicles is empty.")

            self.assertEqual(len(all_vehicles), 12)


if __name__=="__main__":
    unittest.main()