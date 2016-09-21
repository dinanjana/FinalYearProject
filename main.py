import ImageAnalyzer as ia
import time
import RESTClient as rest

url = 'http://localhost:9090/AnalyticsServer/data'
while True:
    payload = ia.histogramCalc('coc1.jpg')
    #print ia.imageToBase64()
    payload = 'data='+payload
    rest.sendPOST(url,payload)
    time.sleep(1)