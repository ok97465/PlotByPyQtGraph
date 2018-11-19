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
from typing import Tuple
from numpy import ndarray, linspace, array, arange
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QApplication


def _imagesc_pg_colormap(colormap_str):
    r"""imagesc_pg 에서 사용할 colormap 을 계산 한다.

    Parameters
    ----------
    colormap_str : str
        ['Grey', 'Grey_r', 'jet', parula', 'viridis', ...]

    Returns
    -------
    (ndarray, Tuple[Tuple[int]])
        position, colors

    """
    if colormap_str.lower() == 'parula':
        colors = (
            (62,  39, 169),
            (63,  39, 172),
            (63,  40, 175),
            (64,  41, 178),
            (64,  42, 181),
            (65,  43, 184),
            (65,  44, 187),
            (65,  45, 189),
            (66,  46, 192),
            (66,  47, 195),
            (67,  48, 198),
            (67,  49, 200),
            (68,  50, 203),
            (68,  51, 206),
            (69,  53, 209),
            (69,  54, 211),
            (69,  55, 214),
            (70,  56, 216),
            (70,  57, 218),
            (70,  58, 220),
            (70,  60, 223),
            (71,  61, 224),
            (71,  62, 226),
            (71,  64, 228),
            (71,  65, 230),
            (71,  67, 231),
            (72,  68, 233),
            (72,  69, 234),
            (72,  71, 236),
            (72,  72, 237),
            (72,  74, 238),
            (72,  75, 239),
            (72,  76, 241),
            (72,  78, 242),
            (72,  79, 243),
            (72,  81, 244),
            (72,  82, 245),
            (72,  83, 246),
            (72,  85, 247),
            (72,  86, 248),
            (72,  88, 248),
            (71,  89, 249),
            (71,  90, 250),
            (71,  92, 251),
            (71,  93, 251),
            (71,  95, 252),
            (70,  96, 252),
            (70,  97, 253),
            (69,  99, 253),
            (69, 100, 254),
            (68, 102, 254),
            (68, 103, 254),
            (67, 105, 255),
            (66, 106, 255),
            (65, 108, 255),
            (64, 109, 255),
            (63, 111, 255),
            (62, 112, 255),
            (61, 114, 255),
            (59, 115, 255),
            (58, 117, 255),
            (56, 118, 255),
            (54, 120, 255),
            (53, 121, 254),
            (51, 123, 254),
            (50, 124, 253),
            (49, 126, 253),
            (48, 127, 252),
            (47, 129, 251),
            (47, 130, 251),
            (47, 132, 250),
            (46, 133, 249),
            (46, 134, 249),
            (46, 136, 248),
            (46, 137, 247),
            (45, 138, 246),
            (45, 140, 245),
            (45, 141, 244),
            (45, 142, 243),
            (45, 143, 241),
            (44, 145, 240),
            (43, 146, 240),
            (42, 147, 239),
            (41, 149, 238),
            (40, 150, 237),
            (39, 151, 236),
            (39, 152, 235),
            (38, 154, 234),
            (38, 155, 233),
            (37, 156, 232),
            (37, 157, 232),
            (37, 158, 231),
            (36, 159, 230),
            (35, 161, 230),
            (35, 162, 229),
            (34, 163, 229),
            (33, 164, 228),
            (32, 165, 228),
            (31, 166, 227),
            (30, 167, 226),
            (29, 169, 225),
            (29, 170, 225),
            (28, 171, 224),
            (27, 172, 223),
            (26, 173, 222),
            (25, 174, 220),
            (23, 175, 219),
            (22, 176, 218),
            (20, 177, 217),
            (18, 178, 215),
            (16, 178, 214),
            (14, 179, 212),
            (11, 180, 211),
            (8, 181, 209),
            (6, 182, 208),
            (4, 183, 206),
            (2, 183, 205),
            (1, 184, 203),
            (0, 185, 202),
            (0, 186, 200),
            (0, 186, 198),
            (1, 187, 197),
            (2, 188, 195),
            (4, 188, 193),
            (6, 189, 192),
            (9, 189, 190),
            (13, 190, 188),
            (16, 191, 187),
            (20, 191, 185),
            (23, 192, 183),
            (26, 192, 181),
            (29, 193, 180),
            (32, 193, 178),
            (35, 194, 176),
            (37, 194, 174),
            (39, 195, 173),
            (41, 195, 171),
            (43, 196, 169),
            (45, 197, 167),
            (46, 197, 165),
            (47, 198, 163),
            (49, 198, 161),
            (50, 199, 159),
            (51, 199, 157),
            (53, 200, 155),
            (54, 200, 153),
            (56, 201, 151),
            (57, 201, 149),
            (59, 202, 147),
            (61, 202, 144),
            (64, 203, 142),
            (66, 203, 140),
            (69, 204, 137),
            (72, 204, 135),
            (75, 204, 132),
            (78, 204, 130),
            (81, 205, 127),
            (85, 205, 125),
            (88, 205, 122),
            (91, 205, 120),
            (94, 205, 117),
            (97, 205, 114),
            (100, 206, 111),
            (104, 206, 108),
            (107, 206, 106),
            (111, 206, 103),
            (114, 205, 100),
            (118, 205,  97),
            (122, 205,  94),
            (125, 205,  92),
            (129, 205,  89),
            (133, 204,  86),
            (136, 204,  84),
            (140, 204,  81),
            (144, 203,  78),
            (147, 203,  75),
            (151, 203,  73),
            (154, 202,  70),
            (158, 202,  67),
            (161, 201,  65),
            (165, 201,  62),
            (168, 200,  60),
            (172, 200,  57),
            (175, 199,  55),
            (178, 198,  53),
            (182, 198,  51),
            (185, 197,  49),
            (188, 197,  47),
            (191, 196,  46),
            (194, 195,  44),
            (197, 195,  42),
            (200, 194,  41),
            (203, 193,  40),
            (206, 193,  40),
            (209, 192,  39),
            (212, 192,  39),
            (215, 191,  40),
            (217, 190,  40),
            (220, 190,  41),
            (223, 189,  41),
            (225, 189,  42),
            (228, 188,  43),
            (230, 188,  45),
            (233, 187,  46),
            (235, 187,  48),
            (237, 187,  51),
            (240, 187,  53),
            (242, 186,  55),
            (244, 186,  57),
            (246, 186,  59),
            (248, 187,  61),
            (250, 187,  62),
            (252, 188,  63),
            (253, 189,  62),
            (255, 190,  61),
            (255, 191,  60),
            (255, 192,  59),
            (255, 194,  58),
            (255, 195,  57),
            (255, 197,  56),
            (255, 198,  55),
            (255, 200,  54),
            (255, 201,  53),
            (255, 203,  52),
            (254, 204,  51),
            (254, 206,  50),
            (254, 207,  49),
            (253, 209,  48),
            (252, 210,  47),
            (252, 212,  47),
            (251, 214,  46),
            (250, 215,  45),
            (250, 217,  44),
            (249, 218,  43),
            (248, 220,  43),
            (248, 222,  42),
            (247, 223,  41),
            (247, 225,  40),
            (246, 226,  40),
            (246, 228,  39),
            (246, 229,  39),
            (246, 231,  38),
            (246, 233,  37),
            (246, 234,  36),
            (246, 236,  35),
            (246, 237,  34),
            (246, 239,  33),
            (247, 240,  32),
            (247, 242,  31),
            (247, 243, 30),
            (248, 245,  29),
            (248, 246,  27),
            (249, 247,  26),
            (249, 249,  24),
            (250, 250,  22),
            (250, 252, 21)
            )
    elif colormap_str.lower() in ['gray', 'grey']:
        colors = ((0, 0, 0), (255, 255, 255))
    elif colormap_str.lower() in ['grey_r', 'grey_r']:
        colors = ((255, 255, 255), (0, 0, 0))
    else:
        try:
            from matplotlib import cm
            cm_matplotlib = cm.get_cmap(colormap_str)
            colors = uint8(cm_matplotlib(range(256))[:, 0:3] * 256)
        except ValueError:
            colors = []

    pos = linspace(0.0, 1.0, len(colors))

    return pos, colors


class PgImageViewROI(pg.ImageView):
    r"""ImageView 에 Mouse 명령을 추가 한다."""

    def __init__(self, *args, **kwargs):
        r"""PgImageViewOk를 초기화한다."""
        super().__init__(*args, **kwargs)
        self.font_family: str = 'Courier New'
        self.font_size: str = '4'
        self.value_color: str = '#0581FF'
        self.scale_x: float = 1.0
        self.scale_y: float = 1.0
        self.axis_x: ndarray = array([])
        self.axis_y: ndarray = array([])
        self.ui.roiBtn.hide()
        self.ui.menuBtn.hide()

    def set_scale(self, scale_x: float, scale_y: float):
        self.scale_x = scale_x
        self.scale_y = scale_y

    def set_axis(self, axis_x: ndarray, axis_y: ndarray):
        self.axis_x = axis_x
        self.axis_y = axis_y

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
                    self.html_of_data_marker_name('PIXEL[X,Y]') +
                    self.html_of_data_marker_value(f'[{data_point_x} {data_point_y}]') + '<br>' +
                    self.html_of_data_marker_name('AXIS [X,Y]') +
                    self.html_of_data_marker_value(f'[{self.axis_x[data_point_x]:6g} {self.axis_y[data_point_y]:6g}]') + '<br>' +
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


class PgUserAxisItem(pg.AxisItem):
    """입력받은 Axis가 표시되도록 linkedViewChanged을 Overide한다."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.offset: float = 0.0  # pixel의 중앙에 axis 값이 표시되도록 보정
        self.delta: float = 1.0
        self.value_of_view_axis_0: float = 0.0

    def set_axis(self, value_of_view_axis_0, delta, scale):
        self.value_of_view_axis_0 = value_of_view_axis_0
        self.delta = delta * scale
        self.offset = -delta/2

    def custom_range(self, newRange, inverted: bool):
        value_first = newRange[0] * self.delta + self.value_of_view_axis_0 + self.offset
        value_end = newRange[1] * self.delta + self.value_of_view_axis_0 + self.offset

        if inverted:
            return value_end, value_first
        else:
            return value_first, value_end

    def linkedViewChanged(self, view, newRange=None):
        if self.orientation in ['right', 'left']:
            newRange = view.viewRange()[1]
            self.setRange(*self.custom_range(newRange, view.yInverted()))
        else:
            newRange = view.viewRange()[0]
            self.setRange(*self.custom_range(newRange, view.xInverted()))


def imagesc_pg(*arg, colormap='viridis', title='', xlabel='', ylabel='', , colorbar=False):
    r"""Implement Imagesc using pyqtgraph

    return을 받지 않으면 figure 창이 사라진다.

    Parameters
    ----------
    colormap : str, optional
        ['Grey', 'Grey_r', ,'jet', 'parula', 'viridis', ..., None] (the default is 'viridis')
    title : str
        title
    xlabel : str
        xlabel
    ylabel : str
        ylabel
    colorbar : bool
        colorbar

    Returns
    -------
    pg.ImageView
        return을 받지 않으면 Figure가 사라진다.

    """
    pg.setConfigOption('background', 'w')
    pg.setConfigOption('foreground', 'k')
    pg.setConfigOptions(imageAxisOrder='row-major')

    if (len(arg) == 1) or isinstance(arg[1], str) or arg[1] is None:
        data = arg[0]
        nr = data.shape[0]
        nc = data.shape[1]
        col_axis = arange(nc)
        row_axis = arange(nr)
        title_idx = 1
    elif len(arg) >= 3 and isinstance(arg[2], ndarray):
        data = arg[2]
        nr = data.shape[0]
        nc = data.shape[1]
        col_axis = arg[0]
        row_axis = arg[1]
        title_idx = 3
    else:
        print('Plz Check argument of imagesc_pg')
        return

    if len(col_axis) != nc or len(row_axis) != nr:
        print('check size of axis and data')
        return

    try:
        title = arg[title_idx]
        xlabel = arg[title_idx + 1]
        ylabel = arg[title_idx + 2]
        colormap = arg[title_idx + 3]
        colorbar = arg[title_idx + 4]
    except IndexError:
        pass

    if colormap and data.ndim > 2:
        import sys
        print('Ignored colormap (data ndim > 2)', file=sys.stderr)
        colormap = None

    diff_x = col_axis[1] - col_axis[0]
    diff_y = row_axis[1] - row_axis[0]

    if diff_x > diff_y:
        scale = (1.0, abs(diff_y/diff_x))
    else:
        scale = (abs(diff_x/diff_y), 1.0)

    axis_bottom = PgUserAxisItem(orientation='bottom')
    axis_bottom.set_axis(col_axis[0], diff_x, 1.0/scale[0])

    axis_left = PgUserAxisItem(orientation='left')
    axis_left.set_axis(row_axis[0], diff_y, 1.0/scale[1])

    imv = PgImageViewROI(
        view=pg.PlotItem(
            title=title,
            labels={'left': ylabel, 'bottom': xlabel},
            axisItems={
                'left': axis_left,
                'bottom': axis_bottom}
        ))

    imv.set_scale(*scale)
    imv.set_axis(col_axis, row_axis)

    imv.show()

    imv.setImage(data, scale=scale)

    if colormap:
        color_pos, color = _imagesc_pg_colormap(colormap)
        if len(color) > 0:
            imv.setColorMap(pg.ColorMap(color_pos, color, mode=pg.ColorMap.RGB))
        else:
            print('check colormap')

    imv.getImageItem().mouseDoubleClickEvent = imv.func_double_click
    imv.getImageItem().mouseClickEvent = imv.func_shift_left_click

    if colorbar:
        imv.ui.histogram.show()
    else:
        imv.ui.histogram.hide()

    return imv
