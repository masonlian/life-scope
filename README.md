<h1>一、網站簡介：</h1>
主要的功能為追蹤使用者的裝置地理位置，分析三種指標數據，藉此找出適合使用者居住的都市環境，並提供視覺形象。
<br>
<h1>二、執行環境</h1>
前端：瀏覽器可直接運行<br>
後端： JDK17, Python 3.9, Maven4.0, Spring Boot 3.5, Flask, MySQL 9.3 
外部API: Google Geolocation API 
<br>

<h1>三、系統架構概述</h1>
<p>透過瀏覽器原生的API追蹤裝置的經緯度，藉由WatchPosition與Timer的搭配追蹤裝置是否有離開特定場所，若無則傳送經緯到後端Spring會回傳場所細節讓使用者確認場所，一套流程下來搜集使用者生活數據。
使用者確認場所後Spring會整理資訊並且登載，被登載的資訊則將被提交給Flask去計算取得三項主要的統計指標，規律度熵值，平均移動距離與興趣點穩定狀態矩陣。這三項指標用來判斷使用者的生活狀態，並且匹配相對應的城市形態。
  匹配的結果被提交到前台後，網頁會根據其城市形態生成相對應的虛擬人物。
</p>




<h1>四、系統架構圖:</h1>
<img width="981" height="611" alt="life_scope drawio" src="https://github.com/user-attachments/assets/dfb28f7d-24b3-4295-905a-90c28b1017e0" />


<br>
<br>

<h1>五、網頁展示</h1>

<img width="1280" height="3869" alt="Untitled (2)" src="https://github.com/user-attachments/assets/6ec51063-7488-43c4-babc-7e8c4a524c15" />


