# -*- coding: utf-8 -*-
r"""PyQtGraph를 이용하여 plot하는 util

[Description]

Example
-------
[example]

Notes
-----
[Notes]

References
----------
.. [] 책: 저자명. (발행년). Title of chapter. In 편집자명 (역할), title of book (쪽). 발행지 : 발행사
.. [] 학위 논문: 학위자명, "논문제목", 대학원 이름 석사 학위논문, 1990 
.. [] 저널 논문: 저자. "논문제목". 저널명, . pp.

:File name: plot_pg.py
:author: ok97465
:Date created: 2018-11-16 오후 5:28
"""
import pyqtgraph as pg
from numpy import ndarray, linspace, arange
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QApplication


def _imagesc_pg_colormap(colormap_str):
    r"""imagesc_pg 에서 사용할 colormap 을 계산 한다.

    Parameters
    ----------
    colormap_str : str
        ['Grey', 'Grey_r', 'jet', parula']

    Returns
    -------
    (ndarray, Tuple[Tuple[int]])
        position, colors

    """
    if colormap_str.lower() == 'parula':
        colors = (
            (62, 39, 169),
            (64, 42, 181),
            (66, 47, 192),
            (68, 51, 204),
            (69, 55, 214),
            (70, 60, 223),
            (71, 66, 230),
            (72, 71, 236),
            (72, 77, 241),
            (72, 83, 245),
            (72, 88, 249),
            (71, 94, 252),
            (69, 100, 254),
            (67, 106, 255),
            (62, 112, 255),
            (56, 118, 255),
            (50, 124, 253),
            (47, 130, 251),
            (46, 135, 248),
            (45, 141, 244),
            (43, 146, 240),
            (39, 151, 236),
            (37, 156, 232),
            (35, 161, 230),
            (32, 165, 227),
            (28, 170, 224),
            (24, 174, 220),
            (18, 178, 215),
            (8, 181, 209),
            (1, 184, 203),
            (2, 187, 196),
            (11, 190, 189),
            (25, 192, 182),
            (36, 194, 175),
            (44, 196, 168),
            (50, 199, 160),
            (55, 201, 152),
            (63, 203, 143),
            (74, 204, 133),
            (87, 205, 123),
            (100, 206, 111),
            (114, 205, 100),
            (129, 205, 89),
            (144, 203, 78),
            (158, 202, 67),
            (172, 199, 57),
            (185, 197, 49),
            (198, 195, 42),
            (210, 192, 39),
            (221, 190, 41),
            (231, 188, 45),
            (240, 187, 54),
            (249, 187, 61),
            (255, 190, 61),
            (255, 196, 56),
            (255, 202, 52),
            (253, 208, 48),
            (251, 215, 45),
            (248, 221, 42),
            (246, 228, 39),
            (246, 234, 36),
            (246, 240, 32),
            (248, 246, 27),
            (250, 252, 21))
    elif colormap_str.lower() == 'jet':
        colors = (
            (0, 0, 144),
            (0, 0, 160),
            (0, 0, 176),
            (0, 0, 192),
            (0, 0, 208),
            (0, 0, 224),
            (0, 0, 240),
            (0, 0, 255),
            (0, 16, 255),
            (0, 32, 255),
            (0, 48, 255),
            (0, 64, 255),
            (0, 80, 255),
            (0, 96, 255),
            (0, 112, 255),
            (0, 128, 255),
            (0, 144, 255),
            (0, 160, 255),
            (0, 176, 255),
            (0, 192, 255),
            (0, 208, 255),
            (0, 224, 255),
            (0, 240, 255),
            (0, 255, 255),
            (16, 255, 240),
            (32, 255, 224),
            (48, 255, 208),
            (64, 255, 192),
            (80, 255, 176),
            (96, 255, 160),
            (112, 255, 144),
            (128, 255, 128),
            (144, 255, 112),
            (160, 255, 96),
            (176, 255, 80),
            (192, 255, 64),
            (208, 255, 48),
            (224, 255, 32),
            (240, 255, 16),
            (255, 255, 0),
            (255, 240, 0),
            (255, 224, 0),
            (255, 208, 0),
            (255, 192, 0),
            (255, 176, 0),
            (255, 160, 0),
            (255, 144, 0),
            (255, 128, 0),
            (255, 112, 0),
            (255, 96, 0),
            (255, 80, 0),
            (255, 64, 0),
            (255, 48, 0),
            (255, 32, 0),
            (255, 16, 0),
            (255, 0, 0),
            (240, 0, 0),
            (224, 0, 0),
            (208, 0, 0),
            (192, 0, 0),
            (176, 0, 0),
            (160, 0, 0),
            (144, 0, 0),
            (128, 0, 0))
    elif colormap_str.lower() in ['gray', 'grey']:
        colors = ((0, 0, 0), (255, 255, 255))
    elif colormap_str.lower() in ['grey_r', 'grey_r']:
        colors = ((255, 255, 255), (0, 0, 0))
    else:
        colors = []

    pos = linspace(0.0, 1.0, len(colors))

    return pos, colors


class PgImageViewOk(pg.ImageView):
    r"""ImageView 에 Mouse 명령을 추가 한다."""

    def __init__(self, *args, **kwargs):
        r"""PgImageViewOk를 초기화한다."""
        super().__init__(*args, **kwargs)
        self.font_family = 'Courier New'
        self.font_size = '4'
        self.value_color = '#0581FF'
        self.ui.roiBtn.hide()
        self.ui.menuBtn.hide()
        self.scale_x = 1.0
        self.scale_y = 1.0

    def set_scale(self, scale_x: float, scale_y: float):
        self.scale_x = scale_x
        self.scale_y = scale_y

    def size_of_roi(self):
        r"""그림의 Pixel을 1로 계산 했을 때 화면에 그릴 Data Marker(ROI)의 크기를 계산한다."""
        size_x = self.scale_x
        size_y = self.scale_y
        return pg.Point(size_x, size_y)

    def html_of_data_marker_name(self, string):
        r"""Data Marker의 Text에 항목을 HTML로 변환하여 반환한다."""
        return f'<font size="{self.font_size}"; color="black">{string} </font>'

    def html_of_data_marker_value(self, string):
        r"""Data Marker의 Text에 값을 HTML로 변환하여 반환한다."""
        return f'<strong><font size="{self.font_size}"; color=#0581FF>{string}</font></strong>'

    def func_shift_left_click(self, event):
        """Shift를 누르고 마우스 왼쪽을 클릭하면 Data Marker를 표시한다.

        Parameters
        ----------
        event

        """
        modifiers = QApplication.keyboardModifiers()
        if event.button() == Qt.LeftButton and modifiers == Qt.ShiftModifier:
            pos = event.scenePos()
            data_point = self.getImageItem().mapFromScene(pos)

            data_point_x = int(data_point.x())
            data_point_y = int(data_point.y())

            # view_rect = self.getImageItem().viewRect()
            # text_size = self.size_text(view_rect.width(), view_rect.height())
            if self.image.ndim > 2:
                val_point = f'{self.image[data_point_y, data_point_x, :]}'
            else:
                val_point = f'{self.image[data_point_y, data_point_x]}'

            rgb_hex = hex(self.getImageItem().getPixmap().toImage().pixel(data_point_x, data_point_y))
            rgb = f'[{int(rgb_hex[4:6], 16)} {int(rgb_hex[6:8], 16)} {int(rgb_hex[8:], 16)}]'

            roi = pg.ROI(
                pos=(data_point_x*self.scale_x, data_point_y*self.scale_y),
                size=self.size_of_roi(), movable=False, removable=True)

            roi.addTranslateHandle((0.5, 0.5))
            roi.setAcceptedMouseButtons(Qt.LeftButton)
            text = pg.TextItem(
                html=(
                    f'<span style="font-family: {self.font_family};">' +
                    self.html_of_data_marker_name('[X,Y]') +
                    self.html_of_data_marker_value(f'[{data_point_x} {data_point_y}]') + '<br>' +
                    self.html_of_data_marker_name('Value') +
                    self.html_of_data_marker_value(val_point) + '<br>' +
                    self.html_of_data_marker_name('[R,G,B]') +
                    self.html_of_data_marker_value(rgb) +
                    '</span>'
                ),
                border={'color': "000000", 'width': 1},
                anchor=(0, 1),
                fill=(250, 250, 255, 255))
            text.setParentItem(roi)
            roi.sigClicked.connect(self.roi_click)
            roi.sigRemoveRequested.connect(self.roi_remove)

            self.addItem(roi)
            event.accept()
        else:
            event.ignore()

    def roi_remove(self, roi):
        """ROI를 제거한다."""
        self.removeItem(roi)

    def roi_click(self, roi, event):
        """클릭된 ROI를 앞에 표시한다."""
        for item in self.view.items:
            if isinstance(item, pg.ROI):
                item.setZValue(0)
        roi.setZValue(1)

    def func_double_click(self, event):
        """Double 클릭 시 이미지를 전체 뷰로 본다."""
        # self.view.autoRange()
        self.view.setRange(QRectF(0.0, 0.0, float(self.image.shape[1]), float(self.image.shape[0])))


def imagesc_pg(*arg, colormap=None, title='', xlabel='', ylabel='', colorbar=False):
    r"""Implement Imagesc using pyqtgraph

    return을 받지 않으면 figure 창이 사라진다.

    Parameters
    ----------
    colormap : str, optional
        ['Grey', 'Grey_r', ,'jet', 'parula', None] (the default is 'None')
    title : str
        title
    xlabel : str
        xlabel
    ylabel : str
        ylabel
    colorbar : bool
        colobar

    Returns
    -------
    pg.ImageView
        return을 받지 않으면 Figure가 사라진다.

    """
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    pg.setConfigOptions(imageAxisOrder='row-major')

    if len(arg) == 1:
        data = arg[0]
        nr = data.shape[0]
        nc = data.shape[1]
        col_axis = arange(nc)
        row_axis = arange(nr)
    elif len(arg) == 3 and type(arg[2]) == ndarray:
        data = arg[2]
        col_axis = arg[0]
        row_axis = arg[1]
    else:
        print('Plz Check argument of imagesc_pg')
        return

    if colormap and data.ndim > 2:
        import sys
        print('Ignored colormap (data ndim > 2)', file=sys.stderr)
        colormap = None

    diff_x = col_axis[1] - col_axis[0]
    diff_y = row_axis[1] - row_axis[0]

    if diff_x > diff_y:
        scale = (1.0, diff_y/diff_x)
    else:
        scale = (diff_x/diff_y, 1.0)

    imv = PgImageViewOk(
        view=pg.PlotItem(
            title=title,
            labels={'left': ylabel, 'bottom': xlabel}
        ))

    imv.set_scale(*scale)

    imv.show()

    imv.setImage(data, scale=scale)
    if colormap:
        imv.setColorMap(pg.ColorMap(*_imagesc_pg_colormap(colormap), mode=pg.ColorMap.RGB))
    imv.getImageItem().mouseDoubleClickEvent = imv.func_double_click
    imv.getImageItem().mouseClickEvent = imv.func_shift_left_click

    if colorbar:
        imv.ui.histogram.show()
    else:
        imv.ui.histogram.hide()

    return imv
