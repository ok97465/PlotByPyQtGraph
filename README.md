# PlotByPyQtGraph
PyqtGraph를 이용하여 Python의 Plot을 가속화한다.  
PyQt5가 Backend로 동작되어야 한다.

## imagesc
- left double click으로 전체화면을 그린다.
- Data를 도시하고 Cursor Marker를 표시한다. (shift + left click)
- Shift+S 를 이용하여 Mouse 클릭 시 행동을 변경한다.
<img src="images/imagsc_data_cursor.png?raw=true" alt="Example Cursor Marker" width="420"/>

- colormap 지원 ( 'jet', 'gray', 'parula', 'viridis', matplotlib colormap )
- Cursor Marker 설정 시 생기는 네모 상자를 우클릭하여 Cursor Marker 삭제
<img sc="images/imagsc_data_cursor_remove.png?raw=true" alt="Example Remove Cursor Marker" width="420"/>

## plot
- left double click으로 전체화면을 그린다.
- Data를 도시하고 Cursor Marker를 표시한다. (shift + left click)
- Shift+S 를 이용하여 Mouse 클릭 시 행동을 변경한다.
- 좌측 하단에 Mouse가 가르키는 축의 값을 표시한다.
<img sc="images/plotqt_data_cursor.png?raw=true" alt="Example Plot" width="420"/>