def pick_peaks(arr):
    #your code here
    tmp_pos=None
    tmp_peak=None
    pos=[]
    peaks=[]
    inc=0
    inc_res=0
    for i in range(1,len(arr)):
        inc=arr[i]-arr[i-1]
        print(arr[i-1],arr[i],inc,inc_res)
        if inc>0:
            tmp_pos=i
            tmp_peak=arr[i]
            print('may by')
        #Фиксация, только если переход в -1
        if tmp_pos and inc<0:
            pos.append(tmp_pos)
            peaks.append(tmp_peak)
            tmp_pos=None
            tmp_peak=None
            print('fix')
        inc_res=inc
    print(pos)
    print(peaks)

    result=dict()
    result['pos']=pos
    result['peaks']=peaks
    print(pos)
    print(peaks)
    print(result)
    return(result)

arr = [3, 6, 13, 5, 5, 19, -2, 11, 18, 6, 15, 9, 3, 19, 10, 4, 13]
pick_peaks(arr)
