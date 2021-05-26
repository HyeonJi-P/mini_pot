import threading
from threading import Thread
import time
import smbus
import RPi_I2C_driver
import RPi.GPIO as GPIO
import spidev
import Adafruit_DHT #Adafruit 기능을 가져옴

wLevel=[0,0,0,0,0] #수위센서 5개값을 담을 리스트
tds=[0,0,0,0,0] #TDS 5개값을 담을 리스트
temp=[0,0,0,0,0] #온도 리스트
hum=[0,0,0,0,0] #습도 리스트
illuminance=[0,0,0,0,0] #조도센서 리스트

#온도 평균계산용 
tempAvg=0
#습도 평균계산용
humAvg=0
#수위 평균계산용 
wLevelAvg=0
#수위 평균계산용 
tdsAvg=0
#광량 평균계산
illumAvg=0

State=[0,0,0,0,0] #현재상태리스트 [온도,습도,조도,양액농도,수위] 정상=0,이상=1
preState=[0,0,0,0,0] #이전 사이클 상태리스트 
stResult=[0,0,0,0,0] #현재 과거 둘다이상시 1로기록

checkFlag=False #RGB LED용 센서값 읽는중인지 상태정리중인지 확인하는 변수
DHT11_sensor=True #센서상태가 정상인지 확인용
TDS_sensor=True
BH1750_sensor=True
wLevel_sensor=True

######조건들##################
RPI_REST = 100 #초단위, 프로그램이 한번 돌아가고 다음 시간까지 휴식..?
Senser_interver=1.0 #센서 읽는주기
Max_Hum = 50.0 #습도
Min_Hum = 10.0
Max_Temp = 30.0 #온도
Min_Temp = 15.0
Max_illum = 10000 #조도
Min_illum = 300
Max_TDS = 1000 #양액농도
Min_TDS = 300
Max_wLevel = 600 #수위
Min_wLevel = 450

DHT11=Adafruit_DHT.DHT11

#사용하는 핀 번호들(BCM)

GPIO.setmode(GPIO.BCM)

FAN1_1 = 17 #팬1
FAN1_2 = 18 #팬1
FAN2_1 = 27 #팬2
FAN2_2 = 22 #팬2

WATER_PUMP = 20 #워터펌프2

RGB_LED_R=5 #RGB LED
RGB_LED_G=6
RGB_LED_B=13
DHT11_PIN = 4 #온습도센서
LED_Bar=16 #릴레이 연결

tdsChannel=0 #adc채널 설정
wLevChannel=0 #adc채널 설정

I2C_CH = 1 #Light sensor 
BH1750_DEV_ADDR = 0x23
CONT_H_RES_MODE = 0X10
CONT_H_RES_MODE2 = 0X11
CONT_L_RES_MODE = 0X13
ONETIME_H_RES_MODE = 0x20
ONETIME_H_RES_MODE2 = 0x21
ONETIME_L_RES_MODE = 0x23
i2c = smbus.SMBus(I2C_CH)

spi=spidev.SpiDev() #아날로그컨버터(수위&TDS) 설정
spi.open(0,0)
spi.max_speed_hz=500000

#출력으로 설정

GPIO.setup(FAN1_1,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(FAN1_2,GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(FAN2_1,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(FAN2_2,GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(RGB_LED_R,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RGB_LED_G,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(RGB_LED_B,GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(WATER_PUMP,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(LED_Bar,GPIO.OUT, initial = GPIO.LOW)

#사용하는 클래스들
class temp_hum(Thread): #온습도 클레스
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global temp,hum, tempAvg,humAvg,DHT11_sensor,DHT11_PIN
        try:
            for i in range(5):
                #DHT11 sensor read 10times
                h, t = Adafruit_DHT.read_retry(DHT11, DHT11_PIN) #센서정보를 읽어오기 위한 코드
                print("temp&hum read")
                hum[i]=h #리스트에 저장
                temp[i]=t            
                time.sleep(Senser_interver) #센서 읽는 주기. 
                if i==4:
                    tsum=0 #온도 합산용 지역변수
                    hsum=0 #습도 합산용 지역변수
                    for j in range(5): #평균내기
                        tsum+=temp[j]
                        hsum+=hum[j]
                    tempAvg=tsum/5
                    humAvg=hsum/5
                    DHT11_sensor=True    #정상작동
                
        except :
            print("DHT11 sensor Error")
            DHT11_sensor=False #센서 에러
            preState[1]=1 #빠르게 오류를 출력하기 위해 preState값 변경
            preState[0]=1

            
class Water(Thread): #수분관련 클레스
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global wLevel,tds,wLevelAvg,tdsAvg,wLevel_sensor,TDS_sensor
        try:
            for i in range(5):
                adcValue=read_spi_adc(tdsChannel) #수분값 adc 읽기
                tdsV=100-int(map(adcValue,0,1023,0,1000)) #몇퍼센트인지 변환
                print("tds read ")
                tds[i]=tdsV #리스트에 저장
                
                adcValue=read_spi_adc(wLevChannel) #수분값 adc 읽기
                wLevV=100-int(map(adcValue,0,1023,0,1000)) #몇퍼센트인지 변환
                print("wLevel read ")
                wLevel[i]=wLevV #리스트에 저장
                if i==4:
                    tdsSum=0 #합산용 지역변수
                    wlevSum=0 #합산용 지역변수
                    for j in range(5): #평균내기
                        wlevSum+=wLevel[j]
                        tdsSum+=wLevel[j]
                    wLevelAvg=wlevSum/5
                    tdsAvg=tdsSum/5
                    wLevel_sensor=True #센서 작동 정상
                    TDS_sensor=True #센서 작동 정상
                time.sleep(Senser_interver) #센서 주기    
        except:
            wLevel_sensor=False #센서 오작동의심
            TDS_sensor=False 
            preState[3]=1
            preState[4]=1 #빠르게 표시하기 위해 preState값 바꾸기

#빛센서 클레스
class light(Thread): 
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        global illuminance, BH1750_sensor, illumAvg
        try: 
            for i in range(5):
                #조도센서
                luxBytes = i2c.read_i2c_block_data(BH1750_DEV_ADDR, CONT_H_RES_MODE,2)
                lux = int.from_bytes(luxBytes, byteorder='big')
                print('{0} lux'.format(lux))

                print("illuminance read ")
                illuminance[i]=lux #리스트에 저장
                if i==4:
                    illum =0 #illuminance 합산용 지역변수
                    for j in range(5):
                        illum+= illuminance[j]
                    illumAvg=illum/5
                    BH1750_sensor=True #조도센서 작동 정상
                time.sleep(Senser_interver) #센서 주기    
        except:
            BH1750_sensor=False #조도센서 작동 비정상
            preState[2]=1 #빠르게 표시하기 위해 preState값 바꾸기
     
#사용되는 함수

def read_spi_adc(Channel): #adc 읽는 함수
    adcValue=0
    buff=spi.xfer2([1,(8+Channel)<<4,0])
    adcValue = ((buff[1]&3)<<8)+buff[2]
    return adcValue
def map(value,min_adc,max_adc,min_v,max_v): #0에서1024를 보기편하게 퍼센트로 변환
    adc_range=max_adc-min_adc
    v_range=max_v-min_v
    scale_factor=float(adc_range)/float(v_range)
    return min_v+((value-min_adc)/scale_factor)

def prt(): #테스트 출력
    global tdsAvg,wLevelAvg,tempAvg,humAvg,illumAvg
    print('tds avg is: {}'.format(tdsAvg))
    print('wlevel avg is: {}'.format(wLevelAvg))
    print('illum avg is: {}'.format(illumAvg))
    print('temp is: {} hum is: {}'.format(tempAvg,humAvg))
    

def led_bar(mode): #LED 바 설정함수
    if mode == 1:
        #ON
        GPIO.output(LED_Bar,GPIO.HIGH) 
        print("led bar: ON")
        
    else : 
        #OFF
        GPIO.output(LED_Bar,GPIO.LOW)
        print("led bar: OFF")
        
    
def RGB_LED_light( temp, hum, lighting): #RGBLED 함수
    while True:
        GPIO.output(RGB_LED_R,GPIO.LOW) #초기화
        GPIO.output(RGB_LED_G,GPIO.LOW) #불끄기
        GPIO.output(RGB_LED_B,GPIO.LOW)
        
        if checkFlag==False: #모두 join될때 중지
            print("RGB function Break!")
            break
        else:
            #각 기능별 이상에 대한 led색 지정 필요, 혹은 led의 필요성에 대한 논의 필요
            print("led working")
                
def WaterPump (): #워터펌프 함수
    #n초간 워터펌프 작동==급수
    
    GPIO.output(WATER_PUMP,GPIO.HIGH) #작동
    print("WaterPump: ON")
    time.sleep(3) #임의의 값. 이후 식물 흙 량에 맞추어 조정 필요
    GPIO.output(WATER_PUMP,GPIO.LOW) #멈춤
    print("WaterPump: OFF")

#실질적인 동작부분 코드
while True: #실행
    try:
        sensor_list=[] #두 센서를 넣을 리스트
        water_ss=Water() #수위&TDS센서
        tempHum_ss=temp_hum() #온습도센서
        illum_ss=light() #조도센서
        sensor_list.append(water_ss) #센서리스트에 추가
        sensor_list.append(tempHum_ss) #센서리스트에 추가
        sensor_list.append(illum_ss) #센서리스트에 추가
        water_ss.start() #시작
        tempHum_ss.start() #시작
        illum_ss.start() #시작
        checkFlag=True #RGB LED 체크확인용

        #RGBLED 표시 시작 (LCD상태를 기반, 첫 표시는 초록)
        RGBLED=threading.Thread(target=RGB_LED_light, args=(stResult[0],stResult[1],stResult[2]))
        RGBLED.start()

        for sensor in sensor_list: #센서 일끝날때까지 기다리기 (RGB LED도 종료될 것)
            sensor.join()
        checkFlag=False #RGB LED 체크확인용
        
        prt() # 확인하기위한 함수(테스트용)

        #평균값과 기준값 비교, 센서이상여부
        #온습도센서
        if DHT11_sensor==False: #센서이상
            State[0]=1 # 온도문제
            State[1]=1 # 습도문제
        else:   
            if (tempAvg<Max_Temp) and (Min_Temp<tempAvg) : #온도조건, 최저와 최고사이에 있을때 정상
                State[0]=0
            else :
                State[0]=1
            
            if (humAvg<Max_Hum) and (Min_Hum<humAvg) : #습도조건, 최저와 최고사이
                State[1]=0
            else :
                State[1]=1

        #조도센서
        if BH1750_sensor == False : #센서이상
            State[2]=1 
        else:    
            if illumAvg < Min_illum :
                # 어두움
                State[2]=1
            elif illumAvg >= Max_illum :
                #너무밝음?
                State[2]=1
            else : #정상범위
                State[2]=0
   
        if TDS_sensor == False:
            #양액농도센서이상
            State[3]=1
        else:
            if (tdsAvg<Max_TDS) and (tdsAvg<Min_TDS): 
                State[3]=0 #이상없음
            else:
                State[3]=1
        
        if wLevel_sensor == False:
            #양액농도센서이상
            State[4]=1
        else:
            if (wLevelAvg<Max_wLevel) and (wLevelAvg<Min_wLevel): 
                State[4]=0 #이상없음
            else:
                State[4]=1

        #state 리스트 정리
        for i in range(5):
            if State[i]==1 and preState[i]==1: #과거도 이상,현재도 이상이면 ,result상태배열에 갱신
                #Error
                stResult[i]=1
            else: #둘중에 하나라도 아니면 잠시 오류라 생각하고 패스
                stResult[i]=0
        
        print('State Update State[0]:{},[1]:{},[2]:{},[3]:{},[4]:{}'.format(State[0],State[1],State[2],State[3],State[4]))    
        print('result Update stResult[0]:{},[1]:{},[2]:{},[3]:{},[4]:{}'.format(stResult[0],stResult[1],stResult[2],stResult[3],stResult[4]))    


        ########## 장치가 해결할수있는 범위 내의 문제처리(영양액은 사람의 도움이 필요하므로 여기선 제외)###        
        if stResult[1]==1 and stResult[0]==1 and stResult[2]==1 : #온도,습도,빛 모두문제
            print("Temp,Hum,Illuminance Error")
            led_bar(1)#LED Bar On 
            if(wLevel_sensor==True): #센서가 정상인 경우에만 워터펌프 작동
                     WaterPump()
            if(DHT11_sensor==True): #센서가 정상일 경우
                if (tempAvg>Max_Temp) or (humAvg>Max_Hum): #온도가 높거나 습도가 높을때작동, 춥거나 건조한것은 x(실내&양액재배이므로 고려x)
                    #팬 가동
                    print("Fan ON")
                    GPIO.output(FAN1_1,GPIO.HIGH)
                    GPIO.output(FAN1_2,GPIO.LOW)
                    GPIO.output(FAN2_1, GPIO.HIGH)
                    GPIO.output(FAN2_2, GPIO.LOW)

        elif stResult[1]==0 and stResult[0]==0 and stResult[2]==0: #정상          
            led_bar(0)#LED Bar On =>OFF
            #팬 멈춤, 정상
            print("Fan OFF")
            GPIO.output(FAN1_1,GPIO.LOW)
            GPIO.output(FAN1_2,GPIO.LOW)
            GPIO.output(FAN2_1, GPIO.LOW)
            GPIO.output(FAN2_2, GPIO.LOW)    
                
            print("ALL OK")
            
            
        else:
            if stResult[0]==1 : #온도
                print("Temp Error")
                            
                if(DHT11_sensor==True): #센서가 정상인 경우
                    print("Fan ON")
                    GPIO.output(FAN1_1,GPIO.HIGH)
                    GPIO.output(FAN1_2,GPIO.LOW)
                    GPIO.output(FAN2_1, GPIO.HIGH)
                    GPIO.output(FAN2_2, GPIO.LOW)
                else: #센서가 비정상인 경우 중지
                    print("Sensor Err?")
                    GPIO.output(FAN1_1,GPIO.LOW)
                    GPIO.output(FAN1_2,GPIO.LOW)
                    GPIO.output(FAN2_1, GPIO.LOW)
                    GPIO.output(FAN2_2, GPIO.LOW)    
            else:
                #팬 멈춤, 정상
                GPIO.output(FAN1_1,GPIO.LOW)
                GPIO.output(FAN1_2,GPIO.LOW)
                GPIO.output(FAN2_1, GPIO.LOW)
                GPIO.output(FAN2_2, GPIO.LOW)    
                
            if stResult[1]==1 : #습도
                print("Hum Error")
                #fan function
                if(DHT11_sensor==True): #센서가 정상일 경우
                    print("Fan ON")
                    GPIO.output(FAN1_1,GPIO.HIGH)
                    GPIO.output(FAN1_2,GPIO.LOW)
                    GPIO.output(FAN2_1, GPIO.HIGH)
                    GPIO.output(FAN2_2, GPIO.LOW)
                    
                else: #센서가 비정상인 경우 중지
                    print("Sensor Err?")
                    GPIO.output(FAN1_1,GPIO.LOW)
                    GPIO.output(FAN1_2,GPIO.LOW)
                    GPIO.output(FAN2_1, GPIO.LOW)
                    GPIO.output(FAN2_2, GPIO.LOW)    
            else:
                #팬 멈춤, 정상
                GPIO.output(FAN1_1,GPIO.LOW)
                GPIO.output(FAN1_2,GPIO.LOW)
                GPIO.output(FAN2_1, GPIO.LOW)
                GPIO.output(FAN2_2, GPIO.LOW)    
                

            if stResult[2]==1 :
                print("Light Error")
                #led bar function
                led_bar(1) #LED바 작동
            else:
                led_bar(0) #LED바 끄기
                   
#move
        #move 현재상태를 과거상태로 옮기고 다음 사이클 준비
        print("State --> preState")
        for k in range(5): 
            preState[k]=State[k]
        time.sleep(RPI_REST) #한 사이클 후 잠시 휴식(?)
    except KeyboardInterrupt: #ctrl+C 누르면 긴급 종료
        print("KeyboardInterrupt")
        break
#중지
print("STOP")
GPIO.cleanup() #all stop

