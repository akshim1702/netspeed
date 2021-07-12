import speedtest

wifi = speedtest.Speedtest()

ping = print('Ping:- ',wifi.results.ping,' ms')
download = wifi.download()
upload = wifi.upload()
print('Download Speed :- ',round(download/(10**6)/2),'mb/s')
print('Upload Speed :- ',round(upload/(10**6)/2),'mb/s')
