<h1>一、網站簡介：</h1>
主要的功能為追蹤使用者的裝置地理位置，分析三種指標數據，藉此找出適合使用者居住的都市環境，並提供視覺形象。
<br>
<h1>二、執行環境:</h1>
前端：瀏覽器可直接運行<br>
後端： JDK17, Python 3.9, Maven4.0, Spring Boot 3.5, Flask, MySQL 9.3 
外部API: Google Places API
<br>

<h1>三、系統架構概述:</h1>
<p>透過瀏覽器原生的API追蹤裝置的經緯度，藉由WatchPosition與Timer的搭配追蹤裝置是否有離開特定場所，若無則傳送經緯到後端Spring會將從Google Places API得到的細節回傳到前端，讓使用者去做確認，一套流程下來搜集使用者生活數據。使用者確認場所後Spring會整理資訊並且登載，Spring會以REST API將資訊交給Flask去計算，藉以取得三項主要的統計指標，行為熵值、平均移動距離與興趣點穩定向量。這三項指標用來判斷使用者的生活狀態，並加以匹配出相對應的城市形態，最後網頁會根據匹配的結果動態更新UI，變換虛擬角色的圖片。
</p>
<br>
<h1>四、系統架構圖:</h1>
<img width="981" height="611" alt="life_scope drawio" src="https://github.com/user-attachments/assets/dfb28f7d-24b3-4295-905a-90c28b1017e0" />


<br>
<br>

<h1>五、網頁展示:</h1>

<img width="1280" height="3869" alt="Untitled (2)" src="https://github.com/user-attachments/assets/6ec51063-7488-43c4-babc-7e8c4a524c15" />

<h1>六、未來擴充方向:</h1>
<h4>
    1.加入測試確保功能完善<br>
    2.建立新功能擴充數據指標增加角色層次 （ex.記帳功能)。<br>
    3.將角色拆分為人物原型以及裝備配件，根據指標貼給人物穿著樣式。<br>
    4.加上JWT身份驗證並建立帳戶功能。<br>
    5.對後端資訊加上遮罩，初步建立資安防護。<br>
    6.長期規劃:允許不同帳戶間進行交流或訊息互動。<br>
    7.使用Docker將伺服器打包起來建立標準系統。<br>
    8.進一步優化前端使用者體<br>
    9.加上瀏覽器推播功能<br>
</h4>









