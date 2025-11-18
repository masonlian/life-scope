import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from flask import Blueprint, request, jsonify
from analyzer.Service.match_data import match_location_data
from dataclasses import dataclass
import json
import copy


analyzer_bp = Blueprint("analysis", __name__,url_prefix="/api/analysis")

data_bp = Blueprint("data", __name__,url_prefix="/api/data")

@analyzer_bp.route("/match_data",methods=["GET"])



#之後這邊要記得jsonfy
def match_data():

    data = match_location_data()
    data_json = jsonify(data)
    
   
    if data is None :
       return jsonify({ "result" : "城市匹配失敗！" })
    else : 
         return data_json 




#@analyzer_bp.route("/matchRegion", methods=["GET"])
#def matchRegion():
    
#    match_data()


@data_bp.route("/data_cleanup", methods=["GET"])

def data_cleanup():
   
   data = match_location_data()
   
   @dataclass
   class a_matrix:
      poi:list
      probility:float
       
   m_list = data.return_steady_matrix 
   
   matrix_list = []
   
   original_total_probility = 0.0
   for item in m_list:
        
      if item.poi[0]=="[":
         item.poi.replace("[","")
      if item.poi[-1]=="]":
         item.poi.replace("]","")
      print("原始資料poi:",item.poi,"機率:",item.probility,end="\n")
      list_of_poi = item.poi.split(",")
      probility = item.probility
      original_total_probility += probility
      matrix_list.append(a_matrix(poi=list_of_poi, probility=probility))
      
      
   print("原始資料機率總和為:",original_total_probility,end="\n")
   
      
   total_probility=0.0
   poi_map = {}
   for m in matrix_list:
      poi = m.poi[0]
      if poi in poi_map:
         poi_map[poi] += m.probility 
         total_probility += m.probility
      else:
         poi_map[poi] = m.probility
         total_probility += m.probility
         
      
   print("刪掉重複poi後的資料長度為:",len(poi_map),end=" ")
   print("總機率為:",total_probility,end="\n")
   
   sorted_poi = sorted(poi_map.items() , key = lambda x:x[1], reverse = True )
   top_5_poi = sorted_poi[0:5]
   final = copy.deepcopy(top_5_poi)
   print("前五大POI及機率為:",final,end="\n")
   data_for_return = jsonify(final)
   
   if final is None:
      return ("資料搜索失敗。")
   else:
      return data_for_return 
   
   

   
   #將相同的poi合併
   

    
    