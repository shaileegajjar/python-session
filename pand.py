# inport pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

table_imported = pd.read_csv('sensor_data.csv')
light = table_imported['LIGHT']
time = table_imported['Time']
sound = table_imported['SOUND']

plt.plot(time, light, 'b')
plt.ylabel('Light level')
plt.xlabel('Time')
plt.title('Lighting of my phone')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()

plt.plot(time, sound, 'g')
plt.ylabel('Sound level')
plt.xlabel('Time')
plt.title('Sound of my phone')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

plt.show()

av_light = sum(light) / len(light)
av_sound = sum(sound) / len(sound)

print("Average lighting is %.1f Lux" % av_light)
print("Average sound level is %.1f dB" % av_sound)
input("Press enter for exit.")
