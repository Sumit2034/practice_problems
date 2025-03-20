# Enter your code here. Read input from STDIN. Print output to STDOUT
# [{user_id, clock_in, clock_out}, {}]
# {user_id:{clock_in}, user_id:{clock_in, clock_out, status: active/inactive}}
from datetime import datetime
import datetime as dt
class LabourService:
    
    def __init__(self):
        self.daily_employee_tracker = {}
        self.employee_tracker = {}
    
    def clock_in(self, user_id, clock_in_time):
        if user_id not in self.daily_employee_tracker:
            entry = { 
                "clock_in": clock_in_time,
                "status": "active",
                "clock_out": None,
                "total_hours": 0
            }
            self.daily_employee_tracker[user_id]= entry
            self.employee_tracker[user_id] = [entry]
        else:
            user_details = self.daily_employee_tracker[user_id]
            if user_details["clock_out"] and not user_details["clock_out"] < clock_in_time:
                return "Please clockout first if you need re clockin"
            if not user_details["clock_out"]:
                return "Please clockout first if you need re clockin"
                
            entry = { 
                "clock_in": clock_in_time,
                "status": "active",
                "clock_out": None,
                "total_hours": user_details["total_hours"]
            }
            self.daily_employee_tracker[user_id]["clock_in"] = clock_in_time
            self.daily_employee_tracker[user_id]["status"] = "active" 
            self.employee_tracker[user_id].append(entry)
        
        return clock_in_time
    
    def clock_out(self, user_id, clockout_time): 
        if user_id not in self.daily_employee_tracker:
            return "User not clockedin yet"
        if self.daily_employee_tracker[user_id]["status"]=="inactive":
            return "User not clockedin yet"
            
        clockin_time = self.daily_employee_tracker[user_id]["clock_in"]
        self.daily_employee_tracker[user_id]["clock_out"] = clockout_time
        self.daily_employee_tracker[user_id]["total_hours"] = clockout_time-clockin_time
        self.daily_employee_tracker[user_id]["status"] = "inactive"
        
        user_entries = self.employee_tracker[user_id]
        user_entries[-1]["clockout"] = clockout_time
        user_entries[-1]["total_hours"] = clockout_time-clockin_time
        user_entries[-1]["status"] = "inactive"
        
        return self.daily_employee_tracker[user_id]
        
    
    def get_clocked_in_users(self):
        if len(self.daily_employee_tracker) ==0:
            return "Not clocked in yet"
        list_of_users = []
        
        for key, values in self.daily_employee_tracker.items():
            if values["status"]=="active":
                user_values = values
                user_values["user_id"] = key
                list_of_users.append(user_values)
        
        return list_of_users
        
    
    def working_hours_for_emp(self, user_id):
        if user_id not in self.employee_tracker:
            return "user is not clockedin. yet"
        last_sevendays_hours = 0.0
        last_seven_today = datetime.now() - dt.timedelta(days=7)
        user_entries = self.employee_tracker[user_id]
        for i in range(len(user_entries)-1, -1, -1):
            if user_entries[i]["clock_in"] >= last_seven_today:
                last_sevendays_hours += user_entries[i]["total_hours"]
            else:
                break
        
        return last_sevendays_hours
        
print("time",datetime.now()-dt.timedelta(days=5))  
labour_class = LabourService()
print(labour_class.get_clocked_in_users())
print("t1",labour_class.clock_in(user_id="1", clock_in_time=datetime.now()))
print("t2",labour_class.clock_in(user_id="2", clock_in_time=datetime.now()))
print("t3",labour_class.clock_in(user_id="3", clock_in_time=datetime.now()))
print("t4",labour_class.clock_out(user_id="2", clockout_time=datetime.now()))
print("t5",labour_class.clock_in(user_id="1", clock_in_time=datetime.now()))
print("t6",labour_class.clock_out(user_id="2", clockout_time=datetime.now()))
print("t7",labour_class.get_clocked_in_users())
print("t8",labour_class.clock_in(user_id="4", clock_in_time=datetime.now()-dt.timedelta(days=5)))
print("pre condition",labour_class.clock_out(user_id="4", clockout_time=datetime.now()))
print("t9", labour_class.working_hours_for_emp(user_id="4"))

