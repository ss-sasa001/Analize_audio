import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import glob
import os

#file_path_head = "/content/drive/MyDrive/音声/Mean_collection/fft_amplitude_result_mean_"
file_path_head = "/content/drive/MyDrive/音声/Mean_collection/"
#folder = "dann10"
folder = "なし"
file_path_first = file_path_head+"fft_amplitude_result_mean_ppdan15_なし.csv"
file_path_second = file_path_head+"fft_amplitude_result_mean_ppdan10_なし.csv"
#file_path_third = file_path_head+"fft_amplitude_result_mean_pp10_なし.csv"
#file_path_first = file_path_head+ folder +"_なし.csv"
#file_path_second = file_path_head+ folder +"_布.csv"
#file_path_third = file_path_head+ folder +"_金属.csv"
#file_path_fourth = file_path_head+ folder +"_粘土.csv"
df = pd.read_csv(file_path_first)
df2 = pd.read_csv(file_path_second)
#df3 = pd.read_csv(file_path_third)
#df4 = pd.read_csv(file_path_fourth)

plt.figure(figsize=(10, 6))
plt.plot(df['Frequency (Hz)'] ,df['Amplitude'], "-",label='15cm FFT')
plt.plot(df2['Frequency (Hz)'] ,df2['Amplitude'], "--",label='10cm FFT')
#plt.plot(df3['Frequency (Hz)'] ,df3['Amplitude'],"-.",label='10cm FFT')
#plt.plot(df4['Frequency (Hz)'] ,df4['Amplitude'], ":",label='Mean Clay FFT')
plt.xlim(0,4000)
plt.ylim(1)
#plt.xscale("")
plt.yscale("log")
plt.title("Mean_FFT")
plt.xlabel("(Hz)")
plt.ylabel("Amp")
plt.grid(True)
plt.legend()
#plt.savefig(os.path.join("/content/drive/MyDrive/音声/picture_mean", f'{folder}.png'))
