import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt  
import glob
import os
import sys
  #下記はGoogle Colabで行った場合
#from google.colab import drive
#drive.mount('/content/drive')

def pict(file_path):
    # 音声データの読み込み
    data, fs = sf.read(file_path)

    # ステレオの場合はモノラルデータにする
    if len(data.shape) > 1:
        data = data.mean(axis=1)

    d_length = len(data)
    hope_length = 50000
    #データの長さを揃える(適宜len(data)で長さを確認し変更する)
    if d_length < hope_length:
        data = np.pad(data, (0, hope_length - d_length), mode='constant')
    elif d_length > hope_length:
        data = data[:hope_length]
        sys.exit(file_path+"のデータ時間が長すぎます")

    # フーリエ変換(もとの音声データの標本化周波数を用いる)
    y_fft = np.fft.fft(data)
    freq = np.fft.fftfreq(len(data), d=1/fs)

    return freq, y_fft

def normalize_mean(after_fft_data):
    mean_amp = np.mean(after_fft_data)
    if mean_amp != 0:
        return after_fft_data / mean_amp

    return after_fft_data

'''平方二乗根で正規化を行う方法も有る
def normalize_RMS(after_fft_data):
    rms = np.sqrt(np.mean(np.square(after_fft_data)))
    if rms != 0:
        return after_fft_data / rms

    return after_fft_data
'''
def main():
  # 任意のpathを入力
    folder_path_head = (input("フォルダーのpathを入力:"))
    folder_path_foot = (input("ファイルパスの末尾2つ")  #csvファイルの保存時に用います 例)pp15/なし　
    file_name = folder_path_foot.replace('/','_')
    folder_path = os.path.join(folder_path_head, folder_path_foot)
    wavefiles = glob.glob(folder_path+"/*")
'''
単純に
folder_path = ("任意のpath")
file_name = folder_path.replace('/','_')
wavefiles = glob.glob(folder_path+"/*")　
  でも良い
'''
    '''fft_results_rms = []'''
    fft_results_mean = []
    r_freq = None
    '''min_length1 = float('inf')'''
    min_length2 = float('inf')

    for wave_path in wavefiles:
        freq, y_fft = pict(wave_path)
        if r_freq is None:
            r_freq = freq
"""
        # RMSで正規化
        normalized_fft_rms = normalize_RMS(np.abs(y_fft))
        if len(normalized_fft_rms) < min_length1:
            min_length1 = len(normalized_fft_rms)
        fft_results_rms.append(normalized_fft_rms)
"""
        # 平均で正規化
        normalized_fft_mean = normalize_mean(np.abs(y_fft))
        fft_results_mean.append(np.abs(normalized_fft_mean))

    # 平均の計算
    '''average_fft_rms = np.mean(fft_results_rms, axis=0)'''
    average_fft_mean = np.mean(fft_results_mean, axis=0)
    if r_freq is not None:
        aim_index = np.where((r_freq <20000)&(r_freq>0))[0][-1] #0Hzから20000Hzの周波数のインデックスを求める
    else:
      print("None")

    output_folder_path = input("任意のフォルダーパス:")
    output_file_mean = f'/worn_fft_amplitude_result_mean_{file_name}.csv'
    #「f"任意のフォルダーのpath/worn_fft_amplitude_result_mean_{file_name}.csv"」のようにしてください
    with open(output_file_mean, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Frequency (Hz)', 'Amplitude'])
        for f, a_rms in zip(freq[:aim_index],average_fft_mean): #0Hzから20000Hzのデータを保存
            writer.writerow([f, a_mean])

#任意のファイル名で設定してよい
'''
    output_file_rms = f'/content/drive/MyDrive/音声/dann10/worn_fft_amplitude_result_rms_{file_name}.csv'
    with open(output_file_rms, mode='w') as file:
        writer = csv.writer(file)
        writer.writerow(['Frequency (Hz)', 'Amplitude'])
        for f, a_rms in zip(freq[:aim_index],average_fft_rms):  #0Hzから20000Hzのデータを保存
            writer.writerow([f, a_rms])
'''
main()
