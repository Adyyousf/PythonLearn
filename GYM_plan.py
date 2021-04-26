Chest = ["Bench Press 'rod' ", "Decline Press 'Dumbell' ", "Pec Fly" ]
Shoulder = ["Raise 'Side' ", "Plate"]
Triceps = ["Pull Down", "Rope Doen"]
Legs = ["Body Squats", "Weigh Squats", "Lenges", "Leg Press", "Extention , Curl", "Calf"]
Back = ["Pull back", "Pull Down", "Pull ups"]
Trap = ["Weigh", "No name"]
Biceps = ["Curl", "Pull", "Reverse Pull"]

Plan  = {
    'Monday' : [Chest, Shoulder, Triceps],
    'Tuesday' : Legs, 
    'Wednesday' : [Back, Trap, Biceps],
    'Thursday' : 'OFF',
    'Friday' : [Back, Trap, Biceps]
}

for day in Plan :
    print ("%s\t"%day )  
    print Plan[day]
