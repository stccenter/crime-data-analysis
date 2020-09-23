import math
import pandas as pd
import numpy as np
import scipy.stats


# Geodistance between ci and cf (WGS84)
def geodistance(ci , cf , m):
    r = []
            
    lambda1 = ci[1] * math.pi / 180 #longitude
    phi1 = ci[0] * math.pi / 180 #latitude    
    lambda2 = cf[1] * math.pi / 180
    phi2 = cf[0] * math.pi / 180
    
    L = lambda2 - lambda1    
    
    if (lambda1 == lambda2) & (phi1 == phi2):    
        return 0.0
    
    a = 6378137.0
    f = 1/298.257223563    
    b = a * (1 - f)
    axa = a**2
    bxb = b**2
    
    U1 = math.atan((1 - f) * math.tan(phi1))
    U2 = math.atan((1 - f) * math.tan(phi2))
    
    lambda_cur = L
    lambda_old = 1 - 1j # There is no way a complex number is going to coincide with a real number!
    
    ntrials = 0 # Just in case...
    
    while (abs(lambda_cur - lambda_old) > 1e-9):           
        ntrials = ntrials + 1
        
        lambda_old = lambda_cur
        sin_sigma = math.sqrt((math.cos(U2) * math.sin(lambda_cur))**2 + 
                              (math.cos(U1) * math.sin(U2) - 
                               math.sin(U1) * math.cos(U2) * math.cos(lambda_cur))**2)
        cos_sigma = math.sin(U1) * math.sin(U2) + math.cos(U1) * math.cos(U2) * math.cos(lambda_cur)
        sigma = math.atan2(sin_sigma, cos_sigma)
        sin_alpha = math.cos(U1) * math.cos(U2) * math.sin(lambda_cur) / sin_sigma
        cos2_alpha = 1 - sin_alpha**2
        cos_2sigmam = cos_sigma - 2 * math.sin(U1) * math.sin(U2) / cos2_alpha
        
        C = (f/16) * cos2_alpha * (4 + f * (4 - 3 * cos2_alpha))
        
        lambda_cur = L + (1 - C) * f * sin_alpha * (sigma + C * sin_sigma * 
                         (cos_2sigmam + C * cos_sigma * (-1 + 2 * (cos_2sigmam)**2)))
        
        #Stop the function if convergence is not achieved:
        if ntrials > 1000:
            print('Convergence failure...')
            return
            
        # Convergence achieved? get the distance:
        uxu = cos2_alpha * (axa - bxb) / bxb;
        A = 1 + (uxu/16384) * (4096 + uxu * (-768 + uxu * (320 - 175 * uxu)))
        B = (uxu/1024) * ( 256 + uxu * (-128 + uxu * (74 - 47 * uxu)))
        delta_sigma = B * sin_sigma * (cos_2sigmam + (B/4) * (cos_sigma * (-1 + 2 * cos_2sigmam**2) - (B/6)*cos_2sigmam * (-3 + 4 * sin_sigma**2) * ( 3 + 4 * cos_2sigmam**2)))
        r = b * A * (sigma - delta_sigma)
    return r


# minimum distance for every point to other points
def min_distance(coors):
    distance_dir = {}
    for i, coor_i in enumerate(coors):
        for j, coor_j in enumerate(coors):
            if i >= j:
                continue
            dis = geodistance(coor_i , coor_j , 6)/1000
            distance_dir.setdefault(i,[]).append(dis)
            distance_dir.setdefault(j,[]).append(dis)
    min_dis_list = [min(distance_dir[i]) for i in distance_dir]
    return min_dis_list


# Average nearest neighbor 
def ANN(coors, n, area):    
    min_dis_list = min_distance(coors)
    
    de = 0.5/(np.sqrt(n/area))
    do = np.sum(min_dis_list)/n
    se = 0.26136/(np.sqrt(n*n/area))
    ann = do/de
    z = (do-de)/se    
    p = scipy.stats.norm.cdf(z)
    return ann, z, p


def main():
    rows = []
    df = pd.read_csv(input_file, sep=',')
    dates = df['Date'].unique()
    for date in dates:
        df_day = df.loc[df['Date']==date]
        df_crime = df_day.loc[df_day['Crime']==crime_type]
        coors = [[lat,lon] for lat, lon in zip(df_crime['X'],df_crime['Y'])]
        ann, z, p = ANN(coors, len(df_crime), area)
        rows.append([date[:-8], round(ann,3), round(z,3), round(p,3)])
    
    # output the results of ann
    headers = ['Date','ANN','Z_value','P_value']
    data_dir = {h:v for h,v in zip(headers,zip(*rows))}
    outputdata = pd.DataFrame(data_dir)
    outputdata.to_csv(output_file,sep=',',index=False,header=True)
    
    
if __name__ == '__main__':
    input_file = './data/dc-washington.txt'
    output_file = './result/ann-dc-washington.csv'    
    area = 177
    crime_type = 'Burglary'
    
    main()