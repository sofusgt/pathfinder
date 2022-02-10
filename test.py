from pyrosm import get_data, OSM
import matplotlib.pyplot as plt

region = "Copenhagen"
fp = get_data(region, directory="data")

# Initialize the OSM parser object
print("Initializing OSM object...")
osm = OSM(fp)

# Read all drivable roads
# =======================
print("Getting driving network...")
drive_net = osm.get_network(network_type="driving")
""" print("Plotting...")
drive_net.plot() """
print("Done")
""" plt.show() """
