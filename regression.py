import statistics as sta
import math
import matplotlib.pyplot as plt

# Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and  Neptune
orbital_period = [88, 225, 365, 687, 4331, 10_756, 30_687, 60_190]    # days
dist_from_sun = [58, 108, 150, 228, 778, 1_400, 2_900, 4_500] # million km

# Show that a perfect monotonic relationship exists
sta.correlation(orbital_period, dist_from_sun, method='ranked')


# Observe that a linear relationship is imperfect
corr = round(sta.correlation(orbital_period, dist_from_sun), 4)
print(corr)

# Demonstrate Kepler's third law: There is a linear correlation
# between the square of the orbital period and the cube of the
# distance from the sun.
period_squared = [p * p for p in orbital_period]
dist_cubed = [d * d * d for d in dist_from_sun]
corr = round(sta.correlation(period_squared, dist_cubed), 4)
print(corr)


year = [1971, 1975, 1979, 1982, 1983]
films_total = [1, 2, 3, 4, 5]
slope, intercept = sta.linear_regression(year, films_total)
f_pred = round(slope * 2019 + intercept)
print(f_pred)

model = sta.linear_regression(period_squared, dist_cubed, proportional=True)
slope = model.slope

# Dwarf planets:   Pluto,  Eris,    Makemake, Haumea, Ceres
orbital_periods = [90_560, 204_199, 111_845, 103_410, 1_680]  # days
predicted_dist = [math.cbrt(slope * (p * p)) for p in orbital_periods]
print(list(map(round, predicted_dist)))

print('actual:', [5_906, 10_152, 6_796, 6_450, 414])  # actual distance in million km

# plot orbital peroid vs. dist from sum
plt.scatter(dist_from_sun, orbital_period)
plt.show()
