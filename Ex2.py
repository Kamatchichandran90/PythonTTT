import numpy as np

climate_data = np.genfromtxt('climate.txt', delimiter=',', skip_header=1)
print(climate_data)
print(climate_data.shape)
weights = np.array([0.3, 0.2, 0.5])
yields = climate_data @ weights
print(yields)
print(yields.shape)
#Let's add the `yields` to `climate_data` as a fourth column using
#the [`np.concatenate`]  function
climate_results = np.concatenate((climate_data, yields.reshape(10000, 1)), axis=1)
print(climate_results)
print(climate_data)
np.savetxt('climate_results.txt', 
           climate_results, 
           fmt='%.2f', 
           delimiter=',',
           header='temperature,rainfall,humidity,yeild_apples', 
           comments='')

