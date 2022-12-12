# <p class="text-center"><font size=6 class="text-center" >操作步驟教學</font></p>

## 資料集準備
因為官方提供的labels與yolov5訓練格式不同，所以需要使用transform資料夾中的official_to_yolov5.py轉換labels，使用前有兩部分需要注意，第一是檔案中的三個路徑要視需求做更改，第二是圖片編號也同樣需要照需求做更改。修改後將資料集的位置移至Team_2055/data/drone.yaml中的路徑，或者將drone.yaml中設定的路徑進行修改。

## 訓練與預測
我們的指令是在
Linux Ubuntu 20.04.4 LTS
GPU: NVIDIA Tesla V100 32GB * 8
Memory: 360GB memory + 360GB share memory
的環境下操作的，倘若硬體規格無法匹配的話請自行調整
1.--nproc_per_node
2.--device
3.--batch-size
4.--cache ram
等參數，或改成單GPU指令


<b><font size="4">訓練指令:</font></b>

```python -m torch.distributed.run --nproc_per_node 8 train.py --device 0,1,2,3,4,5,6,7 --epochs 3000 --batch-size 64 --data drone.yaml --img 1280 --weights '' --cfg yolov5x.yaml --name yolov5-drone_nopretrained --sync-bn --cache ram```

<b><font size="4">預測指令:</font></b>


```python detect.py --weight runs/train/yolov5-drone_nopretrained/weights/best.pt --source ../drone_dataset/test/ --img 1280 --iou-thres 0.4 --name yolov5_mul_0.5_0.5_0.5_0.3_iou0.4 --save-txt```

<b><font size="4">關於confidence threshold</font></b>


由於修改source code的關係，原先的--conf-thres選項已不可用，請至Team_2055/utils/general.py修改non_max_suppression函式的變數conf_thres1，可以用該list設定不同類別有不同的confidence threshold

## 產生結果
使用transform資料夾中的yolov5_to_official.py轉換labels，使用注意事項同資料集準備，轉換成功後再使用同資料夾中的trasTocsv.py將labels的txt檔轉成csv檔。
