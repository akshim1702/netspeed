import speedtest

wifi = speedtest.Speedtest()

ping = print(wifi.results.ping)
download = wifi.download()
upload = wifi.upload()
print('Download Speed :- ',round(download/(10**6)/2),'mb/s')
print('Upload Speed :- ',round(upload/(10**6)/2),'mb/s')
