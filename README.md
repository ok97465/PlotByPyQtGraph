# PlotByPyQtGraph
PyqtGraph를 이용하여 Plot을 가속화한다.  
PyQt5가 Backend로 동작되어야 한다.

## imagesc
- left double click으로 전체화면을 그린다.
- Data를 도시하고 Cursor Marker를 표시한다. (shift + left click)
![Example Cursor Marker](images/imagsc_data_cursor.png?raw=true)
- colormap 지원 ( 'jet', 'gray', 'parula' )
- Cursor Marker 설정 시 생기는 네모 상자를 우클릭하여 Cursor Marker 삭제
![Example Remove Cursor Marker](images/imagsc_data_cursor_remove.png?raw=true)