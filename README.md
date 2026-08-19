# Black Hole Measuring

A small interactive Python script for computing basic black hole
properties from simple physical inputs.

## What it does

Run the script and pick one of three calculations:

1. **Event Horizon Size (Schwarzschild radius)**
   Enter the black hole's mass (kg) → returns the Schwarzschild
   radius in meters, using:

   ```
   r_s = 2GM / c^2
   ```

2. **Central Mass**
   Enter an orbital velocity (m/s) and orbital radius → returns the
   mass (kg) of the central object, using:

   ```
   M = v^2 * r / G
   ```

3. **Photon Ring Radius**
   Enter the black hole's mass (kg) → returns the photon ring
   radius (1.5x the Schwarzschild radius).

Constants used:
- G = 6.67430e-11 m^3 kg^-1 s^-2
- c = 299,792,458 m/s

## Requirements

- Python 3.x (no external libraries needed)

## Usage

```bash
python3 black_hole_measuring.py
```

You'll be prompted to choose a calculation (1, 2, or 3), then enter
the required values. The result prints to the console.

### Example

```
Enter the number corresponding to your choice (1=Event Horizon, 2=Central Mass, 3=Photon Ring): 1
Calculating the Event Horizon Size of a Black Hole...
Enter the mass of the black hole (in kg): 1.989e30
Result: 2952.99...
```

## Known issue

In `black_hole_central_mass()`, the orbital radius input is
multiplied by `149597870.7` (the AU-to-meters conversion factor),
but the prompt asks for the radius "in m". If you enter a value
already in meters, the result will be off by that factor. Either
enter the radius in AU, or remove the multiplication if you intend
to enter meters directly.

## License

MIT — see [LICENSE](LICENSE).
