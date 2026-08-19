# ---- Black Hole Measuring ----

def black_hole_Event_Horizon_size():
    print("Calculating the Event Horizon Size of a Black Hole...")
    M = float(input("Enter the mass of the black hole (in kg): "))
    event_horizon_size = 2 * (6.67430e-11) * M / (299792458 ** 2)
    return event_horizon_size

def black_hole_central_mass():
    print("Calculating the Central Mass of a Black Hole...")
    v = float(input("Enter the orbital velocity (in m/s): "))
    r = float(input("Enter the orbital radius (in m): "))
    Central_mass = (v ** 2) * (r*149597870.7) / (6.67430e-11)
    return Central_mass

def Black_hole_photon_ring_radius():
    print("Calculating the Photon Ring Radius of a Black Hole...")
    M = float(input("Enter the mass of the black hole (in kg): "))
    Event_horizon_size = 2 * (6.67430e-11) * M / (299792458 ** 2)
    photon_ring_radius = 1.5 * Event_horizon_size
    return photon_ring_radius

choice = int(input("Enter the number corresponding to your choice (1=Event Horizon, 2=Central Mass, 3=Photon Ring): "))
if choice == 1:
    result = black_hole_Event_Horizon_size()
elif choice == 2:
    result = black_hole_central_mass()
elif choice == 3:
    result = Black_hole_photon_ring_radius()
else:
    print("Invalid choice.")
    result = None

if result is not None:
    print("Result:", result)
